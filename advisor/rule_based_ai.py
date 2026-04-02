# advisor/rule_based_ai.py
"""
RuleBasedAI - Secondary AI model for the University Advisor System.
Works fully offline without any API key, using weighted scoring and
rich bilingual responses for both Arabic and English inputs.
"""

import random
import re


class RuleBasedAI:
    """
    A comprehensive rule-based AI engine that serves as:
    1. A standalone personality + major recommender
    2. A fallback when Google Gemini API is unavailable
    3. A bilingual advisor (Arabic + English)
    """

    def __init__(self):
        # Personality type definitions
        self.personality_profiles = {
            # ---- Arabic ----
            'تحليلي': {
                'en': 'Analytical',
                'majors': ['علوم الحاسب', 'هندسة البرمجيات', 'الذكاء الاصطناعي', 'الإحصاء', 'هندسة الشبكات'],
                'strengths_ar': ['التفكير المنطقي', 'حل المشكلات المعقدة', 'تحليل البيانات', 'الدقة العلمية', 'التركيز العالي'],
                'strengths_en': ['Logical thinking', 'Complex problem solving', 'Data analysis', 'Scientific precision', 'High focus'],
            },
            'إبداعي': {
                'en': 'Creative',
                'majors': ['التصميم الجرافيكي', 'الإعلام الرقمي', 'العمارة', 'الأدب', 'إنتاج الأفلام'],
                'strengths_ar': ['التفكير الإبداعي', 'التعبير الفني', 'الخيال الواسع', 'رؤية مبتكرة', 'التكيف السريع'],
                'strengths_en': ['Creative thinking', 'Artistic expression', 'Wide imagination', 'Innovative vision', 'Quick adaptation'],
            },
            'اجتماعي': {
                'en': 'Social',
                'majors': ['التمريض', 'علم النفس', 'التربية', 'العلاقات العامة', 'الخدمة الاجتماعية'],
                'strengths_ar': ['التواصل الممتاز', 'التعاطف', 'حب مساعدة الآخرين', 'العمل الجماعي', 'الاستماع الفعّال'],
                'strengths_en': ['Excellent communication', 'Empathy', 'Helping others', 'Teamwork', 'Active listening'],
            },
            'تنظيمي': {
                'en': 'Organized',
                'majors': ['إدارة الأعمال', 'المحاسبة', 'الاقتصاد', 'القانون', 'إدارة المشاريع'],
                'strengths_ar': ['التخطيط والتنظيم', 'الانتباه للتفاصيل', 'الالتزام', 'إدارة الوقت', 'القرارات المحسوبة'],
                'strengths_en': ['Planning and organization', 'Attention to detail', 'Commitment', 'Time management', 'Calculated decisions'],
            },
            'عملي': {
                'en': 'Practical',
                'majors': ['الهندسة الميكانيكية', 'الهندسة المدنية', 'هندسة الطاقة', 'التقنيات الصناعية', 'هندسة التصنيع'],
                'strengths_ar': ['المهارات العملية القوية', 'حل المشاكل الواقعية', 'التعلم بالتجربة', 'الدقة التقنية', 'العمل الميداني'],
                'strengths_en': ['Strong practical skills', 'Real-world problem solving', 'Learning by doing', 'Technical precision', 'Field work'],
            },
            # ---- English equivalents ----
            'analytical': {'ar': 'تحليلي', 'majors': ['Computer Science', 'Software Engineering', 'AI & Data Science', 'Statistics', 'Cybersecurity']},
            'creative':   {'ar': 'إبداعي', 'majors': ['Graphic Design', 'Digital Media', 'Architecture', 'Literature', 'Film Production']},
            'social':     {'ar': 'اجتماعي', 'majors': ['Nursing', 'Psychology', 'Education', 'Public Relations', 'Social Work']},
            'organized':  {'ar': 'تنظيمي', 'majors': ['Business Administration', 'Accounting', 'Economics', 'Law', 'Project Management']},
            'practical':  {'ar': 'عملي', 'majors': ['Mechanical Engineering', 'Civil Engineering', 'Energy Engineering', 'Industrial Technology', 'Manufacturing']},
        }

        # Interest → personality type mapping
        self.interest_personality_map = {
            # Arabic interests
            'التكنولوجيا': 'تحليلي', 'البرمجة': 'تحليلي', 'الرياضيات': 'تحليلي', 'العلوم': 'تحليلي',
            'الفيزياء': 'تحليلي', 'الكيمياء': 'تحليلي', 'البحث العلمي': 'تحليلي',
            'الفنون': 'إبداعي', 'التصميم': 'إبداعي', 'الإعلام': 'إبداعي', 'الأدب': 'إبداعي',
            'الموسيقى': 'إبداعي', 'التصوير': 'إبداعي',
            'الطب': 'اجتماعي', 'التواصل': 'اجتماعي', 'التعليم': 'اجتماعي', 'المساعدة الاجتماعية': 'اجتماعي',
            'التجارة': 'تنظيمي', 'المال والأعمال': 'تنظيمي', 'الإدارة': 'تنظيمي', 'القانون': 'تنظيمي',
            'الهندسة': 'عملي', 'البناء': 'عملي', 'الميكانيكا': 'عملي', 'التطبيق العملي': 'عملي',
            # English interests
            'technology': 'analytical', 'programming': 'analytical', 'mathematics': 'analytical',
            'science': 'analytical', 'physics': 'analytical', 'research': 'analytical',
            'arts': 'creative', 'design': 'creative', 'media': 'creative', 'literature': 'creative',
            'music': 'creative', 'photography': 'creative',
            'medicine': 'social', 'communication': 'social', 'education': 'social', 'social_help': 'social',
            'business': 'organized', 'finance': 'organized', 'management': 'organized', 'law': 'organized',
            'engineering': 'practical', 'construction': 'practical', 'mechanics': 'practical',
        }

        # Rich chat responses — Arabic
        self.arabic_chat_responses = [
            "بناءً على إجاباتك أرى أن لديك إمكانات رائعة! دعنا نستكشف التخصصات التي تناسب شخصيتك المميزة.",
            "اختيار التخصص قرار مهم وأنا هنا لمساعدتك. ما الذي يجعلك سعيداً ومستمتعاً بما تفعله؟",
            "استناداً إلى تحليل شخصيتك، أنصحك بالتعمق في المجالات التي تشعر فيها بالتدفق والإبداع.",
            "كل طالب لديه مسار خاص به. دعنا نجد ما يناسبك تحديداً بناءً على قدراتك واهتماماتك.",
            "التخصص الجيد هو الذي يجمع بين شغفك وقدراتك وفرص سوق العمل. سأساعدك في إيجاد هذا التوازن.",
            "لا تقلق إذا لم تكن متأكداً بعد، كثير من الطلاب الناجحين مروا بنفس الشعور. معاً سنصل للإجابة!",
            "أرى في إجاباتك شخصاً لديه قدرات متنوعة. هذا يفتح أمامك خيارات عديدة ومثيرة.",
            "أفضل التخصصات هي التي تجعلك ترغب في التعلم حتى خارج أوقات الدراسة. ما الذي يولّه اهتمامك؟",
            "البيانات والشغف معاً يصنعان مساراً مهنياً ناجحاً. دعنا نوظف كليهما في نصيحتي لك.",
            "التوجيه المهني الجيد لا يعطيك إجابة واحدة، بل يرشدك نحو الخيارات الأفضل. هنا لأساعدك تماماً.",
        ]

        # Rich chat responses — English
        self.english_chat_responses = [
            "Based on your answers, I can see you have remarkable potential! Let's explore the majors that best match your unique personality.",
            "Choosing a major is a major decision, and I'm here to guide you. What activities make you feel happy and in the zone?",
            "Based on your personality analysis, I recommend exploring fields where you feel creative flow and deep engagement.",
            "Every student has their own unique path. Let's find exactly what suits YOU based on your strengths and interests.",
            "The best major combines your passion, your abilities, and job market opportunities. I'll help you find that balance.",
            "Don't worry if you're not sure yet — many successful students felt the same way. Together we'll find the answer!",
            "I see in your answers someone with diverse abilities. That opens many exciting possibilities for you.",
            "The best majors are those that make you want to learn even outside class hours. What captures your curiosity?",
            "Data and passion together create a successful career path. Let's use both to guide our recommendation for you.",
            "Good career guidance doesn't give you just one answer — it helps you navigate toward the best options. I'm here exactly for that.",
        ]

        # Fallback major recommendations — Arabic
        self.fallback_majors_ar = [
            {"name": "علوم الحاسب", "match_percentage": 80, "reasons": ["مجال تقني حيوي", "فرص عمل عالمية واسعة", "رواتب تنافسية"]},
            {"name": "إدارة الأعمال", "match_percentage": 75, "reasons": ["مجال شامل ومتنوع", "مهارات قابلة للتطبيق في كل الصناعات", "فرص ريادة أعمال"]},
            {"name": "الطب البشري", "match_percentage": 72, "reasons": ["مهنة إنسانية راقية", "طلب دائم في سوق العمل", "استقرار مهني"]},
            {"name": "الهندسة الميكانيكية", "match_percentage": 70, "reasons": ["أساس الصناعة الحديثة", "تطبيقات واسعة", "تفكير عملي وتحليلي"]},
            {"name": "التصميم الجرافيكي", "match_percentage": 68, "reasons": ["إبداع ومهارة", "سوق رقمي متنامٍ", "استقلالية مهنية"]},
        ]

        # Fallback major recommendations — English
        self.fallback_majors_en = [
            {"name": "Computer Science", "match_percentage": 80, "reasons": ["Vital tech field", "Wide global career opportunities", "Competitive salaries"]},
            {"name": "Business Administration", "match_percentage": 75, "reasons": ["Comprehensive and diverse", "Skills applicable everywhere", "Entrepreneurship opportunities"]},
            {"name": "Medicine", "match_percentage": 72, "reasons": ["Noble humanitarian profession", "Permanent market demand", "Professional stability"]},
            {"name": "Mechanical Engineering", "match_percentage": 70, "reasons": ["Foundation of modern industry", "Wide applications", "Analytical thinking"]},
            {"name": "Graphic Design", "match_percentage": 68, "reasons": ["Creativity and skill", "Growing digital market", "Professional independence"]},
        ]

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze(self, user_data: dict, language: str = None) -> dict:
        """
        Full analysis: detect language, determine personality type,
        score interests, and return recommendations.
        """
        if language is None:
            language = self._detect_language(user_data)

        personality_scores = user_data.get('personality_scores', {})
        interests_data = user_data.get('interests', {})
        academic_prefs = user_data.get('academic_preferences', [])

        personality_type = self._determine_personality_type(personality_scores, language)
        strengths = self._get_strengths(personality_type, language)
        top_interests = self._get_top_interests(interests_data)
        recommended = self._recommend_majors(personality_type, interests_data, academic_prefs, language)
        skills = self._suggest_skills(personality_type, language)
        learning_style = self._get_learning_style(personality_type, language)
        environment = self._get_study_environment(personality_type, language)

        return {
            'personality_analysis': {
                'personality_type': personality_type,
                'strengths': strengths,
                'learning_style': learning_style,
                'suitable_environment': environment,
                'top_interests': top_interests,
            },
            'recommendations': recommended,
            'suggested_skills': skills,
            'language': language,
            'ai_powered': False,
            'model': 'RuleBasedAI v2.0',
        }

    def chat(self, message: str, language: str = None) -> str:
        """Return a rich contextual chat response."""
        if language is None:
            language = self._detect_language_from_text(message)

        # Keyword-based contextual responses
        contextual = self._get_contextual_response(message, language)
        if contextual:
            return contextual

        # Generic rich fallback
        if language == 'arabic':
            return random.choice(self.arabic_chat_responses)
        return random.choice(self.english_chat_responses)

    def get_fallback_majors(self, language: str = 'arabic') -> list:
        """Return fallback major recommendations when no match is found."""
        return self.fallback_majors_ar if language == 'arabic' else self.fallback_majors_en

    # ------------------------------------------------------------------
    # Language Detection
    # ------------------------------------------------------------------

    def _detect_language(self, data: dict) -> str:
        text = str(data)
        arabic_chars = len(re.findall(r'[\u0600-\u06ff]', text))
        return 'arabic' if arabic_chars > 5 else 'english'

    def _detect_language_from_text(self, text: str) -> str:
        arabic_chars = len(re.findall(r'[\u0600-\u06ff]', text))
        return 'arabic' if arabic_chars > 2 else 'english'

    # ------------------------------------------------------------------
    # Personality Analysis
    # ------------------------------------------------------------------

    def _determine_personality_type(self, scores: dict, language: str) -> str:
        if not scores:
            return 'متوازن' if language == 'arabic' else 'Balanced'

        best_trait = max(scores, key=lambda k: scores[k])
        best_val = scores[best_trait]

        # Check for compound type (two high traits)
        sorted_traits = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_traits) >= 2:
            t1, v1 = sorted_traits[0]
            t2, v2 = sorted_traits[1]
            if v1 >= 7 and v2 >= 6:
                if language == 'arabic':
                    return f"{t1} {t2}"
                else:
                    return f"{t1.title()}-{t2.title()}"

        return best_trait

    def _get_strengths(self, personality_type: str, language: str) -> list:
        for key, profile in self.personality_profiles.items():
            if key in personality_type:
                if language == 'arabic' and 'strengths_ar' in profile:
                    return profile['strengths_ar']
                if language == 'english' and 'strengths_en' in profile:
                    return profile['strengths_en']

        if language == 'arabic':
            return ['التفكير المنهجي', 'التعلم المستمر', 'حل المشكلات', 'التكيف مع الظروف', 'روح الفريق']
        return ['Systematic thinking', 'Continuous learning', 'Problem solving', 'Adaptability', 'Team spirit']

    def _get_top_interests(self, interests_data: dict) -> list:
        if not interests_data:
            return []
        sorted_interests = sorted(interests_data.items(), key=lambda x: x[1], reverse=True)
        return [k for k, v in sorted_interests[:5] if v >= 5]

    # ------------------------------------------------------------------
    # Major Recommendations
    # ------------------------------------------------------------------

    def _recommend_majors(self, personality_type: str, interests: dict, prefs: list, language: str) -> list:
        recommendations = []
        base_score = 60

        for key, profile in self.personality_profiles.items():
            if key in personality_type and 'majors' in profile:
                for i, major in enumerate(profile['majors']):
                    score = base_score + max(0, (5 - i) * 6)
                    # Boost by matching interests
                    for interest, val in interests.items():
                        mapped = self.interest_personality_map.get(interest, '')
                        if mapped and key in mapped:
                            score += min(val * 1.5, 10)
                    score = min(int(score), 98)
                    reasons = self._generate_reasons(major, personality_type, language)
                    recommendations.append({
                        'name': major,
                        'match_percentage': score,
                        'reasons': reasons,
                    })
                break

        if not recommendations:
            return self.get_fallback_majors(language)

        recommendations.sort(key=lambda x: x['match_percentage'], reverse=True)
        return recommendations[:5]

    def _generate_reasons(self, major: str, personality_type: str, language: str) -> list:
        reason_map_ar = {
            'تحليلي': [f"يتطلب {major} تفكيراً منطقياً ودقيقاً",
                       "يناسب شغفك بالبيانات والتحليل",
                       "سوق عمل واسع ورواتب تنافسية"],
            'إبداعي': [f"يمنحك {major} مساحة للتعبير الإبداعي",
                       "مجال حيوي ومتطور باستمرار",
                       "يجمع بين الفن والتقنية"],
            'اجتماعي': [f"في {major} ستعمل مباشرة مع الناس",
                        "يناسب شخصيتك الإنسانية المتعاطفة",
                        "تأثير إيجابي حقيقي على المجتمع"],
            'تنظيمي': [f"يحتاج {major} إلى تخطيط ودقة عالية",
                       "مهنة مستقرة ومطلوبة",
                       "يتوافق مع منهجيتك التنظيمية"],
            'عملي':   [f"يمنحك {major} فرصاً للعمل الميداني",
                       "نتائج ملموسة وتطبيق عملي مباشر",
                       "صناعة متطورة ومطلوبة عالمياً"],
        }
        reason_map_en = {
            'analytical': [f"{major} demands logical, precise thinking",
                           "Matches your passion for data and analysis",
                           "Wide job market with competitive salaries"],
            'creative':   [f"{major} gives you space for creative expression",
                           "A vibrant, constantly evolving field",
                           "Blends art with technology"],
            'social':     [f"In {major} you'll work directly with people",
                           "Suits your empathetic, human-centered personality",
                           "Real positive impact on the community"],
            'organized':  [f"{major} requires planning and high precision",
                           "Stable and in-demand profession",
                           "Aligns with your organized methodology"],
            'practical':  [f"{major} gives you field and hands-on opportunities",
                           "Tangible results and direct application",
                           "Advanced and globally needed industry"],
        }

        lang = 'arabic' if language == 'arabic' else 'english'
        map_ = reason_map_ar if lang == 'arabic' else reason_map_en
        for key in map_:
            if key in personality_type.lower():
                return map_[key]

        if language == 'arabic':
            return [f"{major} يناسب مهاراتك المتنوعة", "فرص عمل جيدة", "مجال مطلوب"]
        return [f"{major} suits your diverse skills", "Good career opportunities", "In-demand field"]

    # ------------------------------------------------------------------
    # Skills & Environment
    # ------------------------------------------------------------------

    def _suggest_skills(self, personality_type: str, language: str) -> list:
        skill_map_ar = {
            'تحليلي':  ['التفكير النقدي', 'تحليل البيانات', 'البرمجة', 'الرياضيات', 'حل المشكلات'],
            'إبداعي':  ['التصميم الجرافيكي', 'التفكير الإبداعي', 'سرد القصص', 'التصوير', 'الكتابة الإبداعية'],
            'اجتماعي': ['التواصل الفعّال', 'الاستماع النشط', 'التعاطف', 'القيادة', 'العمل الجماعي'],
            'تنظيمي':  ['إدارة الوقت', 'التخطيط الاستراتيجي', 'إدارة المشاريع', 'التفاوض', 'التحليل المالي'],
            'عملي':    ['مهارات تقنية', 'تشغيل المعدات', 'الصيانة', 'إدارة الموارد', 'السلامة الصناعية'],
        }
        skill_map_en = {
            'analytical':  ['Critical thinking', 'Data analysis', 'Programming', 'Mathematics', 'Problem solving'],
            'creative':    ['Graphic design', 'Creative thinking', 'Storytelling', 'Photography', 'Creative writing'],
            'social':      ['Effective communication', 'Active listening', 'Empathy', 'Leadership', 'Teamwork'],
            'organized':   ['Time management', 'Strategic planning', 'Project management', 'Negotiation', 'Financial analysis'],
            'practical':   ['Technical skills', 'Equipment operation', 'Maintenance', 'Resource management', 'Industrial safety'],
        }
        for key in (skill_map_ar if language == 'arabic' else skill_map_en):
            if key in personality_type:
                return (skill_map_ar if language == 'arabic' else skill_map_en)[key]
        if language == 'arabic':
            return ['التعلم الذاتي', 'التفكير النقدي', 'التواصل', 'إدارة الوقت', 'حل المشكلات']
        return ['Self-learning', 'Critical thinking', 'Communication', 'Time management', 'Problem solving']

    def _get_learning_style(self, personality_type: str, language: str) -> str:
        styles = {
            'arabic': {
                'تحليلي': 'التعلم من خلال البيانات والتحليل والمنطق',
                'إبداعي': 'التعلم من خلال التجريب والاستكشاف الحر',
                'اجتماعي': 'التعلم التعاوني مع الآخرين من خلال النقاش',
                'تنظيمي': 'التعلم المنظم خطوة بخطوة وفق خطة واضحة',
                'عملي': 'التعلم بالممارسة والتطبيق الميداني المباشر',
            },
            'english': {
                'analytical': 'Learning through data, analysis, and logic',
                'creative': 'Learning through experimentation and free exploration',
                'social': 'Collaborative learning with others through discussion',
                'organized': 'Structured step-by-step learning with a clear plan',
                'practical': 'Learning by doing and direct hands-on application',
            }
        }
        lang_styles = styles.get(language, styles['english'])
        for key, style in lang_styles.items():
            if key in personality_type:
                return style
        return styles.get(language, {}).get('balanced', 'Flexible, multi-style learning')

    def _get_study_environment(self, personality_type: str, language: str) -> str:
        envs = {
            'arabic': {
                'تحليلي': 'بيئة هادئة تتيح التركيز العميق مع توفر الأدوات التحليلية',
                'إبداعي': 'بيئة مفتوحة وملهمة تشجع على التجريب والابتكار',
                'اجتماعي': 'بيئة تعاونية غنية بالتفاعل الإنساني والفريقي',
                'تنظيمي': 'بيئة منظمة ذات هياكل واضحة وأهداف محددة',
                'عملي': 'بيئة ميدانية وعملية تجمع بين المختبر والتطبيق',
            },
            'english': {
                'analytical': 'Quiet environment allowing deep focus with analytical tools',
                'creative': 'Open, inspiring environment encouraging experimentation',
                'social': 'Collaborative environment rich in human and team interaction',
                'organized': 'Structured environment with clear frameworks and goals',
                'practical': 'Hands-on field environment combining lab and application',
            }
        }
        lang_envs = envs.get(language, envs['english'])
        for key, env in lang_envs.items():
            if key in personality_type:
                return env
        return 'A balanced, flexible academic environment'

    # ------------------------------------------------------------------
    # Contextual Chat Responses
    # ------------------------------------------------------------------

    def _get_contextual_response(self, message: str, language: str) -> str:
        msg = message.lower()
        if language == 'arabic':
            if any(w in msg for w in ['حاسب', 'برمجة', 'تقنية', 'كمبيوتر', 'ذكاء']):
                return ("علوم الحاسب والبرمجة مجال رائع! الطلب عليه مرتفع جداً في كل أنحاء العالم. "
                        "إذا كنت تحب حل المشكلات المنطقية والرياضيات، فهذا المجال مثالي لك. "
                        "من أبرز التخصصات: علوم الحاسب، هندسة البرمجيات، والذكاء الاصطناعي.")
            if any(w in msg for w in ['طب', 'صيدلة', 'تمريض', 'صحة']):
                return ("المجال الطبي يجمع بين العلم والإنسانية! يحتاج إلى صبر وتفانٍ كبيرين. "
                        "إذا كنت تحب العلوم وتريد مساعدة الناس، فهو مسار مثالي. "
                        "تخصصات رائعة: الطب البشري، الصيدلة، طب الأسنان، والتمريض التخصصي.")
            if any(w in msg for w in ['هندسة', 'بناء', 'معماري', 'مدني', 'ميكانيك']):
                return ("الهندسة من أشمل وأهم التخصصات! تحتاج إلى تفكير تحليلي وعملي معاً. "
                        "هندسة مدنية، ميكانيكية، كهربائية، معمارية — كل منها يفتح آفاقاً واسعة. "
                        "فرص العمل ممتازة محلياً وعالمياً في مشاريع ضخمة.")
            if any(w in msg for w in ['أعمال', 'تجارة', 'محاسبة', 'اقتصاد', 'إدارة']):
                return ("مجال إدارة الأعمال والتجارة متنوع وواعد جداً! "
                        "يناسب الشخصيات القيادية المحبة للتخطيط. "
                        "تخصصات رائدة: إدارة الأعمال، المحاسبة، التسويق، والاقتصاد.")
            if any(w in msg for w in ['فن', 'تصميم', 'رسم', 'إبداع', 'موسيقى']):
                return ("الفنون والتصميم مجال يزدهر في العصر الرقمي! "
                        "إذا كنت شخصاً مبدعاً ولديك رؤية فريدة للأشياء، هذا مكانك. "
                        "أبرز التخصصات: التصميم الجرافيكي، الإعلام الرقمي، العمارة، والفنون البصرية.")
            if any(w in msg for w in ['قانون', 'حقوق', 'محامي']):
                return ("مجال القانون والحقوق من أكثر المجالات تأثيراً في المجتمع! "
                        "يحتاج إلى تفكير نقدي قوي وقدرة على الحجج والإقناع. "
                        "فرص عمل في القضاء، المحاماة، المستشارية، والسياسة.")
            if any(w in msg for w in ['أفضل', 'أنسب', 'أختار', 'ماذا', 'اقترح']):
                return ("لاختيار أفضل تخصص، أنصحك بالإجابة على أسئلة الاختبار الشخصي في النظام. "
                        "سيحلل النظام اهتماماتك وشخصيتك ويوصيك بالتخصصات الأنسب لك تحديداً. "
                        "اضغط على 'ابدأ الاختبار' للحصول على توصيات مخصصة!")
        else:
            if any(w in msg for w in ['computer', 'programming', 'coding', 'tech', 'ai', 'data']):
                return ("Computer Science and programming is an amazing field with sky-high demand worldwide! "
                        "If you love logical problem solving and mathematics, this field is ideal for you. "
                        "Top majors: Computer Science, Software Engineering, and Artificial Intelligence.")
            if any(w in msg for w in ['medicine', 'medical', 'pharmacy', 'nursing', 'health']):
                return ("Medicine combines science with humanity! It requires patience and great dedication. "
                        "If you love science and want to help people, it's a perfect path. "
                        "Great majors: Medicine, Pharmacy, Dentistry, and Specialized Nursing.")
            if any(w in msg for w in ['engineering', 'civil', 'mechanical', 'architect', 'build']):
                return ("Engineering is one of the most comprehensive fields! It needs both analytical and practical thinking. "
                        "Civil, Mechanical, Electrical, Architectural — each opens vast horizons. "
                        "Excellent career opportunities locally and globally on large projects.")
            if any(w in msg for w in ['business', 'accounting', 'economics', 'management', 'finance']):
                return ("Business and management is a diverse and very promising field! "
                        "Perfect for leadership personalities who love planning. "
                        "Leading majors: Business Administration, Accounting, Marketing, and Economics.")
            if any(w in msg for w in ['art', 'design', 'creative', 'music', 'drawing']):
                return ("Arts and Design thrive in the digital age! "
                        "If you're a creative person with a unique vision, this is your place. "
                        "Top majors: Graphic Design, Digital Media, Architecture, and Visual Arts.")
            if any(w in msg for w in ['law', 'legal', 'lawyer', 'rights']):
                return ("Law is one of the most impactful fields in society! "
                        "Needs strong critical thinking and persuasive argumentation. "
                        "Career in judiciary, law practice, consultancy, and politics.")
            if any(w in msg for w in ['best', 'suitable', 'recommend', 'what', 'suggest', 'which']):
                return ("To choose the best major, I recommend taking the personality test in the system. "
                        "It will analyze your interests and personality, then recommend the most suitable majors specifically for you. "
                        "Click 'Start Test' to get personalized recommendations!")
        return None
