# advisor/chat_views.py

import random
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import logging
from .models import AIConversation, AIMessage
from .gemini_service import GeminiService
from majors.models import Major

logger = logging.getLogger(__name__)

class AIChatService:
    def __init__(self):
        # Use Gemini instead of OpenAI
        self.gemini = GeminiService()
        
    def get_response(self, message, context=None):
        """Get a response from the AI model"""
        
        # Use Gemini to get a smart response
        if self.gemini.is_configured:
            try:
                # Build context from the database
                enhanced_context = self._build_enhanced_context(context)
                
                # Get response from Gemini
                ai_response = self.gemini.chat_response(message, enhanced_context)
                
                # Extract majors from the response
                suggested_majors = self._extract_majors_from_response(ai_response)
                
                # Generate smart follow-up questions
                follow_up = self._generate_smart_follow_up(message, ai_response)
                
                return {
                    'response': ai_response,
                    'suggested_majors': suggested_majors,
                    'follow_up_questions': follow_up,
                    'ai_powered': True
                }
            except Exception as e:
                logger.error(f"Gemini Chat Error: {str(e)}")
                # Fall back to simulated system
        
        # Simulated system (fallback)
        responses = [
            "Based on your answers, I can see you have strong analytical skills. Have you considered Engineering or Science majors?",
            "Your interests indicate creative tendencies. What do you think about exploring Design or Media majors?",
            "I noticed you have excellent social skills. Humanities majors might suit you well.",
            "Your organizational skills are strong. Have you thought about Business Administration or Accounting?",
            "Based on your practical personality, Medical or Applied Engineering majors could be a great fit for you."
        ]
        
        return {
            'response': random.choice(responses),
            'suggested_majors': self.get_suggested_majors(message),
            'follow_up_questions': self.generate_follow_up_questions(),
            'ai_powered': False
        }
    
    def _build_enhanced_context(self, context):
        """Build enhanced context from the database"""
        enhanced = {}
        
        if context:
            enhanced.update(context)
        
        # Add information about available majors
        try:
            majors = Major.objects.all()[:10]
            major_names = [m.name for m in majors]
            enhanced['available_majors'] = major_names
        except:
            pass
        
        return enhanced
    
    def _extract_majors_from_response(self, response_text):
        """Extract major names from the response"""
        # Try to find major names in the text
        try:
            majors = Major.objects.all()
            mentioned_majors = []
            
            for major in majors:
                if major.name in response_text:
                    mentioned_majors.append(major.name)
            
            return mentioned_majors[:5] if mentioned_majors else []
        except:
            return []
    
    def _generate_smart_follow_up(self, user_message, ai_response):
        """Generate smart follow-up questions based on context"""
        questions = [
            "Would you like to know more about this major's requirements?",
            "What is your preferred learning style?",
            "Do you have any concerns or reservations about this major?",
            "Do you prefer theoretical or practical study fields?"
        ]
        
        return random.sample(questions, min(2, len(questions)))
    
    def get_suggested_majors(self, user_message):
        """Extract suggested majors from the user's message"""
        keywords = {
            'programming': ['Computer Engineering', 'Computer Science'],
            'medicine': ['Human Medicine', 'Dentistry', 'Pharmacy'],
            'engineering': ['Civil Engineering', 'Mechanical Engineering'],
            'art': ['Graphic Design', 'Fine Arts'],
            'business': ['Business Administration', 'Accounting', 'Marketing'],
        }
        
        suggestions = []
        for keyword, majors in keywords.items():
            if keyword in user_message.lower():
                suggestions.extend(majors)
        
        return suggestions[:3] if suggestions else []
    
    def generate_follow_up_questions(self):
        """Generate follow-up questions"""
        questions = [
            "Which subjects do you enjoy studying the most?",
            "Do you prefer working individually or in a team?",
            "What are your hobbies outside of studying?",
            "Do you have any previous work experience?",
            "What are your future professional ambitions?"
        ]
        
        return random.sample(questions, 2)

@login_required
@csrf_exempt
def chat_with_ai(request):
    """AI chat interface"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            conversation_id = data.get('conversation_id')
            
            # Create or retrieve the conversation
            if conversation_id:
                conversation = AIConversation.objects.get(
                    id=conversation_id,
                    user=request.user
                )
            else:
                conversation = AIConversation.objects.create(
                    user=request.user,
                    title=message[:50]
                )
            
            # Save the user's message
            user_message = AIMessage.objects.create(
                conversation=conversation,
                role='user',
                content=message
            )
            
            # Build context from previous conversation
            context = {
                'conversation_history': [
                    {'role': msg.role, 'content': msg.content}
                    for msg in conversation.messages.all()[:10]
                ]
            }
            
            # Get response from AI
            chat_service = AIChatService()
            ai_response = chat_service.get_response(message, context)
            
            # Save AI response
            ai_message = AIMessage.objects.create(
                conversation=conversation,
                role='assistant',
                content=ai_response['response']
            )
            
            return JsonResponse({
                'success': True,
                'conversation_id': conversation.id,
                'response': ai_response['response'],
                'suggested_majors': ai_response.get('suggested_majors', []),
                'follow_up_questions': ai_response.get('follow_up_questions', []),
                'ai_powered': ai_response.get('ai_powered', False)
            })
            
        except Exception as e:
            logger.error(f"Chat Error: {str(e)}")
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Method not allowed'})

@login_required
def get_conversations(request):
    """Get user conversations"""
    conversations = AIConversation.objects.filter(
        user=request.user
    ).order_by('-updated_at')
    
    conversations_data = []
    for conv in conversations:
        conversations_data.append({
            'id': conv.id,
            'title': conv.title,
            'updated_at': conv.updated_at.strftime('%Y-%m-%d %H:%M'),
            'message_count': conv.messages.count()
        })
    
    return JsonResponse({
        'success': True,
        'conversations': conversations_data
    })