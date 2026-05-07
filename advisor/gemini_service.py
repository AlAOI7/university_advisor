# advisor/gemini_service.py

import json
import logging
from typing import Dict, List, Optional

from django.conf import settings

logger = logging.getLogger(__name__)

# ── Optional dependency ────────────────────────────────────────────────────────
try:
    from google import genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    genai = None
    logger.warning("google-genai package not installed. Gemini will be disabled.")

# ── Internal imports (guarded so a broken sub-module never kills the service) ──
try:
    from .training_examples import format_examples_for_prompt, get_examples_for_language
    TRAINING_EXAMPLES_AVAILABLE = True
except Exception as _te_err:
    TRAINING_EXAMPLES_AVAILABLE = False
    logger.warning(f"training_examples import failed: {_te_err}")

try:
    from .rule_based_ai import RuleBasedAI
    RULE_BASED_AVAILABLE = True
except Exception as _rb_err:
    RULE_BASED_AVAILABLE = False
    RuleBasedAI = None
    logger.warning(f"rule_based_ai import failed: {_rb_err}")

try:
    from .huggingface_service import HuggingFaceService
    HF_AVAILABLE = True
except Exception as _hf_err:
    HF_AVAILABLE = False
    HuggingFaceService = None
    logger.warning(f"huggingface_service import failed: {_hf_err}")


class GeminiService:
    """
    Central service for communicating with Google Gemini API.
    Always returns a response — never raises to the caller.
    Fallback chain: Gemini → RuleBasedAI → HuggingFace → static message.
    """

    # ── Initialisation ─────────────────────────────────────────────────────────

    def __init__(self):
        """Initialize with ALL attributes set to safe defaults FIRST."""

        # --- Safe defaults (set unconditionally so AttributeError is impossible) ---
        self.client = None
        self.model = None
        self.is_configured = False
        self._fallback_ai = None
        self._hf_service = None

        # --- Fallback AI engines ---
        if RULE_BASED_AVAILABLE and RuleBasedAI is not None:
            try:
                self._fallback_ai = RuleBasedAI()
                logger.info("RuleBasedAI initialized successfully.")
            except Exception as e:
                logger.error(f"RuleBasedAI init failed: {e}")

        if HF_AVAILABLE and HuggingFaceService is not None:
            try:
                self._hf_service = HuggingFaceService()
                logger.info("HuggingFaceService initialized successfully.")
            except Exception as e:
                logger.error(f"HuggingFaceService init failed: {e}")

        # --- Gemini API ---
        if not GEMINI_AVAILABLE:
            logger.warning("Gemini library unavailable. Running on fallback only.")
            return

        try:
            api_key = getattr(settings, 'GEMINI_API_KEY', '') or ''
            api_key = api_key.strip()

            if not api_key or api_key in ('your_api_key_here', 'your-api-key-here'):
                logger.warning("GEMINI_API_KEY not set. Running on fallback only.")
                return

            self.client = genai.Client(api_key=api_key)
            self.is_configured = True
            logger.info("Gemini API configured successfully.")

        except Exception as e:
            logger.error(f"Gemini configuration error: {e}")
            self.client = None
            self.is_configured = False

    # ── Public API ─────────────────────────────────────────────────────────────

    def generate_content(self, prompt: str) -> str:
        """Generate content from Gemini, falling back gracefully on any error."""
        if not self.is_configured or not self.client:
            return self._get_fallback_response(prompt)

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text or self._get_fallback_response(prompt)
        except Exception as e:
            logger.error(f"generate_content error: {e}")
            return self._get_fallback_response(prompt)

    def analyze_test_results(self, user_answers: Dict) -> Dict:
        """Analyze test results using Gemini with fallback."""
        if not self.is_configured or not self.client:
            return self._get_fallback_analysis()

        prompt = self._build_analysis_prompt(user_answers)

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return self._parse_analysis_response(response.text or '')
        except Exception as e:
            logger.error(f"analyze_test_results error: {e}")
            return self._get_fallback_analysis()

    def recommend_majors(self, personality_analysis: Dict, user_interests: List[str]) -> List[Dict]:
        """Recommend majors based on personality analysis with fallback."""
        if not self.is_configured or not self.client:
            return self._get_fallback_recommendations()

        prompt = f"""
You are an expert academic advisor specializing in guiding students to choose the right university major.

Personality Analysis:
{json.dumps(personality_analysis, ensure_ascii=False, indent=2)}

Interests:
{', '.join(user_interests)}

Required:
Provide 5 recommended university majors with:
1. Major name
2. Match percentage (0-100%)
3. 3 clear reasons for the recommendation
4. Required skills
5. Expected career opportunities

Provide the response in JSON format as follows:
{{
  "recommendations": [
    {{
      "major_name": "Major Name",
      "match_percentage": 95,
      "reasons": ["reason 1", "reason 2", "reason 3"],
      "required_skills": ["skill 1", "skill 2"],
      "career_opportunities": ["job 1", "job 2"]
    }}
  ]
}}
"""
        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return self._parse_recommendations_response(response.text or '')
        except Exception as e:
            logger.error(f"recommend_majors error: {e}")
            return self._get_fallback_recommendations()

    def chat_response(self, message: str, context: Optional[Dict] = None) -> str:
        """
        Respond to a chat message.
        Always returns a non-empty string — never raises.
        """
        if not message or not message.strip():
            return "Please send a message and I'll be happy to help!"

        if not self.is_configured or not self.client:
            return self._get_fallback_chat_response(message)

        prompt = self._build_chat_prompt(message, context)

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            text = response.text if response and response.text else ''
            return text.strip() or self._get_fallback_chat_response(message)
        except Exception as e:
            logger.error(f"chat_response error: {e}")
            return self._get_fallback_chat_response(message)

    # ── Prompt builders ────────────────────────────────────────────────────────

    def _build_analysis_prompt(self, user_answers: Dict) -> str:
        """Build prompt for test result analysis."""
        language = self._detect_language(user_answers)

        examples = ''
        if TRAINING_EXAMPLES_AVAILABLE:
            try:
                examples = format_examples_for_prompt(language, max_examples=2)
            except Exception:
                pass

        prompt = f"""
You are an expert in personality analysis and career guidance for university students.

**Your Task:** Analyze the student's answers and provide accurate, personalized recommendations.

{examples}

Now, analyze the following student's answers:

**Student Data:**
{json.dumps(user_answers, ensure_ascii=False, indent=2)}

**Required Analysis:**
1. Personality Type (analytical / creative / social / organized / practical)
2. Strengths: list 5 specific strengths
3. Main Interests: top 3 areas
4. Preferred Learning Style
5. Suitable Study Environment

**Response Format (JSON only):**
{{
  "personality_type": "...",
  "strengths": ["...", "...", "...", "...", "..."],
  "interests": ["...", "...", "..."],
  "learning_style": "...",
  "suitable_environment": "..."
}}
"""
        return prompt

    def _build_chat_prompt(self, message: str, context: Optional[Dict]) -> str:
        """Build chat prompt with optional context."""
        context_str = ''
        if context:
            if 'user_profile' in context:
                context_str += f"\nStudent Profile: {context['user_profile']}"
            if 'conversation_history' in context:
                history = context['conversation_history']
                if history:
                    recent = history[-6:]  # last 6 messages only
                    history_text = '\n'.join(
                        f"{m.get('role','user').capitalize()}: {m.get('content','')}"
                        for m in recent
                    )
                    context_str += f"\n\nRecent Conversation:\n{history_text}"
            if 'available_majors' in context:
                majors_list = ', '.join(context['available_majors'][:10])
                context_str += f"\n\nAvailable Majors: {majors_list}"

        prompt = f"""You are a highly intelligent and versatile AI assistant serving as an academic advisor for university students.

Respond logically and comprehensively to ANY topic, question, or input — not just academic ones.
Be direct, friendly, and professional. Do NOT ask unnecessary follow-up questions.
{context_str}

Student Message: {message}

Provide a helpful, direct response in the student's language."""
        return prompt

    # ── Response parsers ───────────────────────────────────────────────────────

    def _parse_analysis_response(self, response_text: str) -> Dict:
        """Extract JSON from analysis response with fallback."""
        try:
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(response_text[start:end])
        except Exception:
            pass
        return self._get_fallback_analysis()

    def _parse_recommendations_response(self, response_text: str) -> List[Dict]:
        """Extract recommendations list from response with fallback."""
        try:
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            if start != -1 and end > start:
                data = json.loads(response_text[start:end])
                recs = data.get('recommendations', [])
                if recs:
                    return recs
        except Exception:
            pass
        return self._get_fallback_recommendations()

    def _detect_language(self, data: Dict) -> str:
        """Detect language from dictionary data."""
        try:
            data_str = json.dumps(data, ensure_ascii=False).lower()
            arabic_keywords = ['تحليلي', 'إبداعي', 'اجتماعي', 'علوم', 'هندسة', 'طب']
            english_keywords = ['analytical', 'creative', 'social', 'science', 'engineering', 'medicine']
            ar = sum(1 for w in arabic_keywords if w in data_str)
            en = sum(1 for w in english_keywords if w in data_str)
            return 'arabic' if ar > en else 'english'
        except Exception:
            return 'english'

    # ── Fallback methods ───────────────────────────────────────────────────────

    def _get_fallback_response(self, prompt: str) -> str:
        """Delegate to RuleBasedAI; if unavailable return a static message."""
        if self._fallback_ai is not None:
            try:
                return self._fallback_ai.chat(prompt)
            except Exception as e:
                logger.error(f"RuleBasedAI.chat error: {e}")
        return (
            "I'm your academic advisor assistant. I'm experiencing a temporary issue "
            "with the AI service. Please try again in a moment, or ask me about "
            "university majors, career paths, and academic guidance."
        )

    def _get_fallback_analysis(self) -> Dict:
        """Return a structured fallback analysis."""
        if self._fallback_ai is not None:
            try:
                result = self._fallback_ai.analyze({})
                pa = result.get('personality_analysis', {})
                return {
                    'personality_type': pa.get('personality_type', 'Balanced'),
                    'strengths': pa.get('strengths', ['Continuous learning', 'Problem solving', 'Adaptability', 'Creativity', 'Teamwork']),
                    'interests': pa.get('top_interests', ['Technology', 'Science', 'Arts']),
                    'learning_style': pa.get('learning_style', 'Flexible and diverse'),
                    'suitable_environment': pa.get('suitable_environment', 'Collaborative academic environment'),
                }
            except Exception as e:
                logger.error(f"RuleBasedAI.analyze error: {e}")

        return {
            'personality_type': 'Balanced',
            'strengths': ['Continuous learning', 'Problem solving', 'Adaptability', 'Creativity', 'Teamwork'],
            'interests': ['Technology', 'Science', 'Arts'],
            'learning_style': 'Flexible and diverse',
            'suitable_environment': 'Collaborative academic environment',
        }

    def _get_fallback_recommendations(self) -> List[Dict]:
        """Return static bilingual major recommendations."""
        return [
            {
                'major_name': 'Computer Science / علوم الحاسب',
                'match_percentage': 80,
                'reasons': ['Vital tech field', 'Wide global career opportunities', 'Competitive salaries'],
                'required_skills': ['Programming', 'Logical thinking', 'Mathematics'],
                'career_opportunities': ['Software Engineer', 'Data Scientist', 'AI Engineer'],
            },
            {
                'major_name': 'Business Administration / إدارة الأعمال',
                'match_percentage': 75,
                'reasons': ['Comprehensive field', 'Universal applicability', 'Leadership opportunities'],
                'required_skills': ['Planning', 'Communication', 'Leadership'],
                'career_opportunities': ['Manager', 'Entrepreneur', 'Business Analyst'],
            },
            {
                'major_name': 'Medicine / الطب البشري',
                'match_percentage': 72,
                'reasons': ['Humanitarian + scientific', 'High market demand', 'Stable career'],
                'required_skills': ['Science', 'Empathy', 'Precision'],
                'career_opportunities': ['Doctor', 'Researcher', 'Medical Specialist'],
            },
            {
                'major_name': 'Engineering / الهندسة',
                'match_percentage': 70,
                'reasons': ['Practical + analytical', 'Wide applications', 'Innovation driven'],
                'required_skills': ['Mathematics', 'Physics', 'Problem solving'],
                'career_opportunities': ['Civil Engineer', 'Mechanical Engineer', 'Project Manager'],
            },
            {
                'major_name': 'Graphic Design / التصميم الجرافيكي',
                'match_percentage': 68,
                'reasons': ['Creativity & skill', 'Growing digital market', 'Professional freedom'],
                'required_skills': ['Design tools', 'Creativity', 'Visual communication'],
                'career_opportunities': ['Designer', 'Brand Specialist', 'UI/UX Designer'],
            },
        ]

    def _get_fallback_chat_response(self, message: str) -> str:
        """Rich bilingual fallback using RuleBasedAI, then static message."""
        if self._fallback_ai is not None:
            try:
                return self._fallback_ai.chat(message)
            except Exception as e:
                logger.error(f"RuleBasedAI fallback chat error: {e}")
        return (
            "I'm here to help with university majors, career guidance, and academic planning. "
            "The AI service is temporarily busy — please try again shortly."
        )
