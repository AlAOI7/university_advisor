# advisor/chat_views.py

import json
import logging
import random

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import AIConversation, AIMessage
from .gemini_service import GeminiService
from majors.models import Major

logger = logging.getLogger(__name__)

# ── Module-level singleton so GeminiService is built once per process ──────────
_gemini_service = None

def _get_gemini_service() -> GeminiService:
    """Return a cached GeminiService instance (lazy init, thread-safe enough for Django)."""
    global _gemini_service
    if _gemini_service is None:
        try:
            _gemini_service = GeminiService()
        except Exception as e:
            logger.error(f"Failed to create GeminiService singleton: {e}")
            _gemini_service = GeminiService.__new__(GeminiService)
            # Manually set safe defaults in the worst case
            _gemini_service.client = None
            _gemini_service.model = None
            _gemini_service.is_configured = False
            _gemini_service._fallback_ai = None
            _gemini_service._hf_service = None
    return _gemini_service


# ── AIChatService ──────────────────────────────────────────────────────────────

class AIChatService:
    """Thin wrapper around GeminiService that handles context building and DB lookups."""

    def __init__(self):
        self.gemini = _get_gemini_service()

    def get_response(self, message: str, context: dict = None) -> dict:
        """
        Get an AI response for *message*.
        Always returns a dict with at least 'response', never raises.
        """
        try:
            enhanced_context = self._build_enhanced_context(context)
            ai_response = self.gemini.chat_response(message, enhanced_context)

            # Guard: ensure we always have a non-empty string
            if not ai_response or not ai_response.strip():
                ai_response = self._static_fallback(message)

            suggested_majors = self._extract_majors_from_response(ai_response)

            return {
                'response': ai_response,
                'suggested_majors': suggested_majors,
                'follow_up_questions': [],
                'ai_powered': self.gemini.is_configured,
            }

        except Exception as e:
            logger.error(f"AIChatService.get_response error: {e}", exc_info=True)
            return {
                'response': self._static_fallback(message),
                'suggested_majors': self._get_keyword_majors(message),
                'follow_up_questions': [],
                'ai_powered': False,
            }

    # ── Context helpers ────────────────────────────────────────────────────────

    def _build_enhanced_context(self, context: dict) -> dict:
        """Merge caller-supplied context with available_majors from DB."""
        enhanced = dict(context) if context else {}
        try:
            major_names = list(Major.objects.values_list('name', flat=True)[:10])
            if major_names:
                enhanced['available_majors'] = major_names
        except Exception as e:
            logger.warning(f"Could not fetch majors for context: {e}")
        return enhanced

    def _extract_majors_from_response(self, response_text: str) -> list:
        """Find major names mentioned in the AI response."""
        try:
            majors = Major.objects.all()
            return [m.name for m in majors if m.name in response_text][:5]
        except Exception as e:
            logger.warning(f"_extract_majors_from_response error: {e}")
            return []

    def _get_keyword_majors(self, message: str) -> list:
        """Simple keyword → major suggestions for the static fallback path."""
        keyword_map = {
            'programming': ['Computer Engineering', 'Computer Science'],
            'medicine':    ['Human Medicine', 'Dentistry', 'Pharmacy'],
            'engineering': ['Civil Engineering', 'Mechanical Engineering'],
            'art':         ['Graphic Design', 'Fine Arts'],
            'business':    ['Business Administration', 'Accounting', 'Marketing'],
        }
        msg = message.lower()
        suggestions = []
        for kw, majors in keyword_map.items():
            if kw in msg:
                suggestions.extend(majors)
        return suggestions[:3]

    @staticmethod
    def _static_fallback(message: str) -> str:
        """Last-resort response — never empty, always helpful."""
        return (
            "I'm your academic advisor. I'm here to help you with university majors, "
            "career paths, and academic planning. Could you please rephrase your question?"
        )


# ── Django views ───────────────────────────────────────────────────────────────

@csrf_exempt
@login_required
def chat_with_ai(request):
    """
    POST /advisor/api/chat/
    Body (JSON): { "message": "...", "conversation_id": <int|null> }
    Returns JSON.
    """
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Method not allowed. Use POST.'}, status=405)

    # ── Parse request body ────────────────────────────────────────────────────
    try:
        data = json.loads(request.body or '{}')
    except (json.JSONDecodeError, ValueError) as e:
        logger.warning(f"chat_with_ai: invalid JSON body — {e}")
        return JsonResponse({'success': False, 'error': 'Invalid JSON in request body.'}, status=400)

    message = (data.get('message') or '').strip()
    if not message:
        return JsonResponse({'success': False, 'error': 'Message cannot be empty.'}, status=400)

    conversation_id = data.get('conversation_id')

    # ── Retrieve or create conversation ──────────────────────────────────────
    try:
        if conversation_id:
            try:
                conversation = AIConversation.objects.get(
                    id=int(conversation_id),
                    user=request.user,
                )
            except (AIConversation.DoesNotExist, ValueError, TypeError):
                # Conversation not found or bad ID → start a new one
                logger.warning(
                    f"Conversation {conversation_id} not found for user {request.user}. "
                    "Creating a new conversation."
                )
                conversation = AIConversation.objects.create(
                    user=request.user,
                    title=message[:50],
                )
        else:
            conversation = AIConversation.objects.create(
                user=request.user,
                title=message[:50],
            )
    except Exception as e:
        logger.error(f"Conversation lookup/create error: {e}", exc_info=True)
        return JsonResponse({'success': False, 'error': 'Failed to create conversation. Please try again.'}, status=500)

    # ── Save user message ─────────────────────────────────────────────────────
    try:
        AIMessage.objects.create(
            conversation=conversation,
            role='user',
            content=message,
        )
    except Exception as e:
        logger.error(f"Failed to save user message: {e}", exc_info=True)
        # Non-fatal — continue to get AI response

    # ── Build context from recent history ────────────────────────────────────
    try:
        recent_messages = list(
            conversation.messages.order_by('-created_at')[:10]
        )
        recent_messages.reverse()
        context = {
            'conversation_history': [
                {'role': msg.role, 'content': msg.content}
                for msg in recent_messages
            ]
        }
    except Exception as e:
        logger.warning(f"Could not load conversation history: {e}")
        context = {}

    # ── Get AI response ───────────────────────────────────────────────────────
    try:
        chat_service = AIChatService()
        ai_result = chat_service.get_response(message, context)
    except Exception as e:
        logger.error(f"AIChatService failed completely: {e}", exc_info=True)
        ai_result = {
            'response': (
                "I'm experiencing a technical issue right now. "
                "Please try again in a moment."
            ),
            'suggested_majors': [],
            'follow_up_questions': [],
            'ai_powered': False,
        }

    # ── Save AI response ──────────────────────────────────────────────────────
    try:
        AIMessage.objects.create(
            conversation=conversation,
            role='assistant',
            content=ai_result['response'],
        )
    except Exception as e:
        logger.error(f"Failed to save assistant message: {e}", exc_info=True)
        # Non-fatal

    return JsonResponse({
        'success': True,
        'conversation_id': conversation.id,
        'response': ai_result['response'],
        'suggested_majors': ai_result.get('suggested_majors', []),
        'follow_up_questions': ai_result.get('follow_up_questions', []),
        'ai_powered': ai_result.get('ai_powered', False),
    })


@login_required
def get_conversations(request):
    """GET /advisor/api/conversations/ — list conversations for the logged-in user."""
    try:
        conversations = AIConversation.objects.filter(
            user=request.user
        ).order_by('-updated_at')

        data = [
            {
                'id': conv.id,
                'title': conv.title,
                'updated_at': conv.updated_at.strftime('%Y-%m-%d %H:%M'),
                'message_count': conv.messages.count(),
            }
            for conv in conversations
        ]

        return JsonResponse({'success': True, 'conversations': data})

    except Exception as e:
        logger.error(f"get_conversations error: {e}", exc_info=True)
        return JsonResponse({'success': False, 'error': 'Failed to retrieve conversations.'}, status=500)