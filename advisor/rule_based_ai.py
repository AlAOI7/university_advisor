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

        # ---- Knowledge base for dynamic responses ----
        self.major_info = {
            # Arabic keywords → detailed info
            'علوم الحاسب': {
                'desc': 'علوم الحاسب تجمع بين الرياضيات والمنطق والابتكار. تشمل البرمجة، قواعد البيانات، الذكاء الاصطناعي، الأمن السيبراني، وعلوم البيانات.',
                'jobs': ['مطور برمجيات', 'مهندس ذكاء اصطناعي', 'محلل بيانات', 'مهندس أمن سيبراني', 'مهندس سحابي'],
                'salary': 'رواتب تنافسية جداً تبدأ من 8,000 ريال وتصل لأكثر من 25,000 ريال شهرياً للمتخصصين.',
                'duration': '4 سنوات',
                'keywords': ['حاسب', 'برمجة', 'كمبيوتر', 'تقنية', 'ذكاء اصطناعي', 'كودنج', 'بايثون', 'جافا', 'سوفتوير', 'computer science', 'computer', 'programming', 'coding', 'software', 'python', 'java', 'developer', 'information systems', 'information technology', 'it major', 'cs major']
            },
            'الطب البشري': {
                'desc': 'الطب مهنة إنسانية تجمع بين العلم والرحمة. يحتاج إلى شغف حقيقي بمساعدة الناس وقدرة على الصبر والتعلم المستمر.',
                'jobs': ['طبيب عام', 'جراح', 'طبيب متخصص', 'طبيب طوارئ', 'باحث طبي'],
                'salary': 'رواتب مرتفعة جداً تبدأ من 15,000 ريال وقد تتجاوز 50,000 ريال للمتخصصين.',
                'duration': '6-7 سنوات (بالإضافة لسنوات الامتياز والتخصص)',
                'keywords': ['طب', 'طبيب', 'صحة', 'علاج', 'مريض', 'مستشفى', 'جراحة', 'طب بشري', 'medicine', 'medical', 'doctor', 'physician', 'hospital', 'surgery', 'study medicine', 'become a doctor', 'requirements to become a doctor']
            },
            'هندسة البرمجيات': {
                'desc': 'هندسة البرمجيات تركز على تصميم وبناء الأنظمة البرمجية الكبيرة والمعقدة بطريقة منهجية ومنظمة.',
                'jobs': ['مهندس برمجيات', 'مهندس DevOps', 'مهندس نظم', 'مطور تطبيقات'],
                'salary': 'رواتب ممتازة تبدأ من 10,000 ريال وترتفع بسرعة مع الخبرة.',
                'duration': '4 سنوات',
                'keywords': ['هندسة برمجيات', 'سوفتوير انجنيرنج', 'تطوير البرمجيات']
            },
            'إدارة الأعمال': {
                'desc': 'إدارة الأعمال تعلمك كيف تدير المنظمات والمشاريع والأفراد. تشمل التسويق والمالية والاستراتيجية وإدارة الموارد البشرية.',
                'jobs': ['مدير تنفيذي', 'مستشار أعمال', 'مدير تسويق', 'رائد أعمال', 'محلل مالي'],
                'salary': 'رواتب متنوعة تبدأ من 6,000 ريال وترتفع بشكل كبير مع الخبرة والمنصب.',
                'duration': '4 سنوات',
                'keywords': ['أعمال', 'إدارة', 'تجارة', 'ريادة', 'بزنس', 'تسويق', 'مبيعات', 'مدير', 'business administration', 'business', 'management', 'marketing', 'entrepreneurship', 'mba', 'careers in business', 'skills for management']
            },
            'الهندسة المدنية': {
                'desc': 'الهندسة المدنية تعنى ببناء البنية التحتية من طرق وجسور ومبانٍ وسدود وشبكات مياه وصرف صحي.',
                'jobs': ['مهندس مدني', 'مدير مشروع', 'مستشار إنشائي', 'مهندس موقع'],
                'salary': 'رواتب جيدة تبدأ من 7,000 ريال مع نمو مستمر بالخبرة.',
                'duration': '5 سنوات',
                'keywords': ['مدني', 'إنشاء', 'بناء', 'هندسة مدنية', 'طرق', 'جسور']
            },
            'الهندسة الكهربائية': {
                'desc': 'الهندسة الكهربائية تشمل أنظمة الطاقة والإلكترونيات والاتصالات والتحكم الآلي.',
                'jobs': ['مهندس كهربائي', 'مهندس طاقة', 'مهندس اتصالات', 'مهندس تحكم'],
                'salary': 'رواتب تنافسية تبدأ من 8,000 ريال.',
                'duration': '5 سنوات',
                'keywords': ['كهربائية', 'كهرباء', 'إلكترونيات', 'طاقة', 'اتصالات']
            },
            'التصميم الجرافيكي': {
                'desc': 'التصميم الجرافيكي يجمع بين الفن والتقنية لإنشاء محتوى بصري مؤثر. يشمل تصميم الهوية البصرية والإعلانات والمواقع.',
                'jobs': ['مصمم جرافيك', 'مصمم UI/UX', 'مدير إبداعي', 'مصمم مستقل'],
                'salary': 'رواتب متفاوتة تبدأ من 4,000 ريال مع إمكانية العمل الحر بدخل أعلى.',
                'duration': '4 سنوات',
                'keywords': ['تصميم', 'جرافيك', 'فوتوشوب', 'فن', 'إبداع', 'رسم', 'تصوير', 'graphic design', 'graphic', 'design major', 'visual design', 'ui ux', 'creative design', 'drawing', 'art major', 'media degree', 'media major']
            },
            'المحاسبة': {
                'desc': 'المحاسبة ركيزة أساسية لكل منظمة. تشمل المحاسبة المالية، التدقيق، الضرائب، والمحاسبة الإدارية.',
                'jobs': ['محاسب قانوني', 'مدقق حسابات', 'محلل مالي', 'مستشار ضريبي'],
                'salary': 'رواتب مستقرة تبدأ من 6,000 ريال مع نمو ثابت.',
                'duration': '4 سنوات',
                'keywords': ['محاسبة', 'مالية', 'أرقام', 'تدقيق', 'ضرائب', 'محاسب', 'accounting', 'accountant', 'finance', 'numbers', 'audit', 'tax', 'cpa']
            },
            'علم النفس': {
                'desc': 'علم النفس يدرس السلوك البشري والعمليات العقلية. يمكّنك من فهم الناس ومساعدتهم على التعامل مع تحديات الحياة.',
                'jobs': ['معالج نفسي', 'مستشار', 'باحث', 'أخصائي موارد بشرية', 'معالج سلوكي'],
                'salary': 'رواتب متنوعة تبدأ من 5,000 ريال وترتفع بالتخصص والشهادات المهنية.',
                'duration': '4-6 سنوات',
                'keywords': ['نفس', 'نفسي', 'سلوك', 'مشاعر', 'معالج', 'إرشاد', 'توجيه', 'psychology', 'psychologist', 'mental health', 'counseling', 'therapy', 'psychology graduates', 'psychology careers']
            },
            'الصيدلة': {
                'desc': 'الصيدلة تجمع بين الكيمياء والبيولوجيا والرعاية الصحية. الصيدلي متخصص دواء يضمن استخدامه الآمن.',
                'jobs': ['صيدلي سريري', 'صيدلي مجتمعي', 'باحث دوائي', 'مندوب طبي'],
                'salary': 'رواتب ممتازة تبدأ من 8,000 ريال.',
                'duration': '5-6 سنوات',
                'keywords': ['صيدلة', 'دواء', 'أدوية', 'صيدلي', 'كيمياء', 'pharmacy', 'pharmacist', 'drug', 'pharmaceutical', 'pharmacy career']
            },
            'القانون': {
                'desc': 'القانون يدرّبك على التفكير النقدي والمنطقي والدفاع عن الحقوق. يشمل القانون التجاري والجنائي والمدني والدولي.',
                'jobs': ['محامي', 'قاضي', 'مستشار قانوني', 'مدعي عام', 'باحث قانوني'],
                'salary': 'رواتب متفاوتة تبدأ من 7,000 ريال وترتفع كثيراً مع الخبرة.',
                'duration': '4-5 سنوات',
                'keywords': ['قانون', 'حقوق', 'محامي', 'قضاء', 'عدالة', 'تشريع', 'law', 'lawyer', 'legal', 'attorney', 'justice', 'studying law', 'law degree', 'english degree', 'english major']
            },
        }

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
        """Dynamic content-aware chat — always responds in English."""
        language = 'english'
        msg = message.strip()
        msg_lower = msg.lower()

        # 1. Check intent first (handles comparisons, personality, specific questions)
        intent_response = self._detect_intent_and_respond(msg, msg_lower, language)
        if intent_response:
            return intent_response

        # 2. Match against major knowledge base
        major_response = self._match_major_knowledge(msg_lower)
        if major_response:
            return major_response

        # 3. Contextual keyword match
        contextual = self._get_contextual_response(message, language)
        if contextual:
            return contextual

        # 4. Last resort: content-based reply
        return self._compose_generic_reply(msg, language)

    def _match_major_knowledge(self, msg_lower: str) -> str:
        """Return rich English major info if the message asks about a specific major."""
        major_en_data = {
            'علوم الحاسب': {
                'name': 'Computer Science',
                'desc': 'Computer Science combines mathematics, logic, and innovation. It covers programming, databases, AI, cybersecurity, and data science.',
                'jobs': ['Software Developer', 'AI Engineer', 'Data Analyst', 'Cybersecurity Engineer', 'Cloud Architect'],
                'salary': 'Highly competitive salaries — typically $60,000-$150,000+ depending on specialization and experience.',
                'duration': '4 years',
            },
            'الطب البشري': {
                'name': 'Medicine',
                'desc': 'Medicine is a humanitarian profession combining science and compassion. It requires genuine passion for helping people and the ability to commit to lifelong learning.',
                'jobs': ['General Practitioner', 'Surgeon', 'Specialist Doctor', 'Emergency Physician', 'Medical Researcher'],
                'salary': 'Very high salaries — typically $150,000-$400,000+ depending on specialization.',
                'duration': '6-7 years (plus residency and specialization)',
            },
            'هندسة البرمجيات': {
                'name': 'Software Engineering',
                'desc': 'Software Engineering focuses on designing and building large-scale, complex software systems in a systematic and organized manner.',
                'jobs': ['Software Engineer', 'DevOps Engineer', 'Systems Engineer', 'Application Developer'],
                'salary': 'Excellent salaries — typically $80,000-$160,000+.',
                'duration': '4 years',
            },
            'إدارة الأعمال': {
                'name': 'Business Administration',
                'desc': 'Business Administration teaches you how to manage organizations, projects, and people. It covers marketing, finance, strategy, and human resource management.',
                'jobs': ['CEO / Executive', 'Business Consultant', 'Marketing Manager', 'Entrepreneur', 'Financial Analyst'],
                'salary': 'Variable — $50,000-$200,000+ depending on role and experience.',
                'duration': '4 years',
            },
            'الهندسة المدنية': {
                'name': 'Civil Engineering',
                'desc': 'Civil Engineering focuses on building infrastructure — roads, bridges, buildings, dams, and water networks.',
                'jobs': ['Civil Engineer', 'Project Manager', 'Structural Consultant', 'Site Engineer'],
                'salary': 'Good salaries — $60,000-$120,000+.',
                'duration': '5 years',
            },
            'الهندسة الكهربائية': {
                'name': 'Electrical Engineering',
                'desc': 'Electrical Engineering covers power systems, electronics, telecommunications, and automation.',
                'jobs': ['Electrical Engineer', 'Power Engineer', 'Telecommunications Engineer', 'Control Engineer'],
                'salary': 'Competitive — $65,000-$130,000+.',
                'duration': '5 years',
            },
            'التصميم الجرافيكي': {
                'name': 'Graphic Design',
                'desc': 'Graphic Design combines art and technology to create impactful visual content including brand identities, advertisements, and websites.',
                'jobs': ['Graphic Designer', 'UI/UX Designer', 'Creative Director', 'Freelance Designer'],
                'salary': 'Variable — $40,000-$100,000+, with high earning potential as a freelancer.',
                'duration': '4 years',
            },
            'المحاسبة': {
                'name': 'Accounting',
                'desc': 'Accounting is a cornerstone of every organization covering financial reporting, auditing, taxation, and management accounting.',
                'jobs': ['Certified Accountant (CPA)', 'Auditor', 'Financial Analyst', 'Tax Consultant'],
                'salary': 'Stable — $50,000-$120,000+.',
                'duration': '4 years',
            },
            'علم النفس': {
                'name': 'Psychology',
                'desc': 'Psychology studies human behavior and mental processes, enabling you to understand people and help them navigate life challenges.',
                'jobs': ['Therapist', 'Counselor', 'Researcher', 'HR Specialist', 'Behavioral Analyst'],
                'salary': 'Variable — $45,000-$100,000+ depending on specialization.',
                'duration': '4-6 years',
            },
            'الصيدلة': {
                'name': 'Pharmacy',
                'desc': 'Pharmacy combines chemistry, biology, and healthcare. Pharmacists are drug specialists who ensure the safe use of medications.',
                'jobs': ['Clinical Pharmacist', 'Community Pharmacist', 'Drug Researcher', 'Medical Representative'],
                'salary': 'Excellent — $80,000-$130,000+.',
                'duration': '5-6 years',
            },
            'القانون': {
                'name': 'Law',
                'desc': 'Law trains you in critical and logical thinking and defending rights. It covers commercial, criminal, civil, and international law.',
                'jobs': ['Lawyer', 'Judge', 'Legal Consultant', 'Prosecutor', 'Legal Researcher'],
                'salary': 'Variable — $60,000-$200,000+ with experience.',
                'duration': '4-5 years',
            },
        }

        for arabic_key, info in major_en_data.items():
            original = self.major_info.get(arabic_key, {})
            all_keywords = original.get('keywords', [])
            for kw in all_keywords:
                if kw in msg_lower:
                    jobs_str = ', '.join(info['jobs'][:3])
                    return (
                        f"**{info['name']}**\n\n"
                        f"{info['desc']}\n\n"
                        f"**Common Jobs:** {jobs_str}\n"
                        f"**Study Duration:** {info['duration']}\n"
                        f"**Salary Range:** {info['salary']}\n\n"
                        f"Would you like to know more about admission requirements or compare this with other majors?"
                    )
        return None

    def _detect_intent_and_respond(self, msg: str, msg_lower: str, language: str) -> str:
        """Detect what the user wants and give a tailored reply."""
        if language == 'arabic':
            # Greetings
            if any(w in msg_lower for w in ['مرحبا', 'هلا', 'أهلا', 'سلام', 'صباح', 'مساء', 'كيف حالك', 'كيف الحال']):
                return "أهلاً وسهلاً! أنا مساعدك الأكاديمي الذكي. يمكنني مساعدتك في اختيار التخصص المناسب، الإجابة على أسئلتك الأكاديمية، أو تزويدك بمعلومات عن أي مجال دراسي. ما الذي تودّ معرفته؟"
            # Asking who
            if any(w in msg_lower for w in ['من أنت', 'مين انت', 'اسمك', 'شو انت']):
                return "أنا مساعد أكاديمي ذكي مصمم لمساعدة الطلاب في اختيار تخصصاتهم الجامعية. يمكنني إخبارك عن أي تخصص، مجال دراسي، فرص عمل، أو مساعدتك في تحديد ما يناسب اهتماماتك وقدراتك."
            # Thanks
            if any(w in msg_lower for w in ['شكرا', 'شكراً', 'يعطيك العافية', 'تسلم', 'مشكور']):
                return "عفواً! يسعدني دائماً مساعدتك. إذا كان لديك أي سؤال آخر حول التخصصات أو المسار الجامعي، أنا هنا."
            # Best major
            if any(w in msg_lower for w in ['أفضل تخصص', 'افضل تخصص', 'أنسب تخصص', 'أي تخصص', 'ماذا أدرس', 'ماذا ادرس']):
                return (
                    "سؤال مهم! أفضل تخصص هو الذي يجمع ثلاثة عناصر:\n\n"
                    "1. **شغفك** — ما الذي تحب فعله حتى بدون مقابل؟\n"
                    "2. **قدراتك** — ما المواد التي تتفوق فيها؟\n"
                    "3. **سوق العمل** — ما التخصصات ذات الطلب المرتفع؟\n\n"
                    "أخبرني عن اهتماماتك أو المواد التي تحبها، وسأقترح عليك التخصصات الأنسب لك شخصياً."
                )
            # Job/salary questions
            if any(w in msg_lower for w in ['راتب', 'وظيفة', 'توظيف', 'فرص عمل', 'سوق العمل', 'مستقبل']):
                return (
                    "سوق العمل اليوم يتطلب مهارات متنوعة. أكثر التخصصات طلباً حالياً:\n\n"
                    "🔹 **تقنية المعلومات والذكاء الاصطناعي** — طلب عالمي هائل\n"
                    "🔹 **الطب والصحة** — استقرار مهني عالٍ\n"
                    "🔹 **الهندسة** — مشاريع ضخمة محلياً وعالمياً\n"
                    "🔹 **إدارة الأعمال** — مرونة في التطبيق عبر كل القطاعات\n\n"
                    "عن أي تخصص تريد معرفة فرص العمل تحديداً؟"
                )
            # Duration questions
            if any(w in msg_lower for w in ['كم سنة', 'مدة', 'سنوات الدراسة', 'كم تاخذ']):
                return (
                    "مدد الدراسة تتفاوت حسب التخصص:\n\n"
                    "• **4 سنوات:** علوم الحاسب، إدارة الأعمال، المحاسبة، التصميم\n"
                    "• **5 سنوات:** الهندسة المدنية والكهربائية، الصيدلة\n"
                    "• **6-7 سنوات:** الطب البشري وطب الأسنان\n\n"
                    "أي تخصص تريد معرفة مدته بالتحديد؟"
                )
            # Comparison
            if any(w in msg_lower for w in ['مقارنة', 'قارن', 'الفرق بين', 'أيهما أفضل', 'ايهما']):
                return "يسعدني مقارنة أي تخصصين! فقط أخبرني بالتخصصين اللذين تريد المقارنة بينهما وسأشرح الفروق في المحتوى والوظائف والرواتب."
        else:
            # English intents — greetings
            if any(w in msg_lower for w in ['hello', 'hey', 'good morning', 'how are you']) and not any(w in msg_lower for w in ['major', 'study', 'career', 'field', 'university']):
                return "Hello! I'm your smart academic advisor. I can help you choose the right major, answer questions about any field, or match your interests to a career path. What would you like to know?"
            if any(w in msg_lower for w in ['who are you', 'what are you', 'your name']):
                return "I'm an AI academic advisor designed to help university students choose the right major. Ask me about any field, career, salary, or tell me your interests and I'll recommend the best path for you."
            if any(w in msg_lower for w in ['thanks', 'thank you', 'appreciate']):
                return "You're welcome! Always happy to help. Feel free to ask anything else about majors or careers."

            # Personality/interest-based — must come BEFORE generic 'what should i study' check
            if any(w in msg_lower for w in ['helping people', 'working in teams', 'like teamwork', 'in teams', 'like helping', 'help people', 'enjoy helping', 'working with people', 'i like helping']):
                return (
                    "You sound like a **social/empathetic** person — a great trait for many fields!\n\n"
                    "Best majors for you:\n"
                    "🔹 **Psychology** — understand and help people's mental health\n"
                    "🔹 **Nursing** — frontline patient care and support\n"
                    "🔹 **Education** — shape future generations\n"
                    "🔹 **Social Work** — help communities and families\n"
                    "🔹 **Human Resources** — manage and support employees\n"
                    "🔹 **Public Relations** — connect organizations with people\n\n"
                    "These careers are deeply rewarding. Want more info on any of them?"
                )
            if any(w in msg_lower for w in ['someone who likes', 'career for someone', 'who likes analysis', 'likes numbers', 'likes analysis', 'analysis and numbers']):
                return (
                    "You're built for **analytical careers** — here are the best paths:\n\n"
                    "🔹 **Data Science** — find patterns and insights in large datasets\n"
                    "🔹 **Financial Analysis** — analyze markets and investments\n"
                    "🔹 **Actuarial Science** — calculate risk using statistics\n"
                    "🔹 **Economics** — study how markets and money work\n"
                    "🔹 **Accounting** — precise financial management\n"
                    "🔹 **AI & Machine Learning** — building systems that learn from data\n\n"
                    "All of these are high-paying, in-demand, and perfect for analytical thinkers!"
                )
            if any(w in msg_lower for w in ['degree in media', 'media degree', 'with a media degree', 'study media', 'media major', 'communication degree', 'mass communication']):
                return (
                    "A **Media or Mass Communication** degree opens many doors!\n\n"
                    "**Career Options:**\n"
                    "📺 **Broadcast Journalist / News Anchor** — TV and radio reporting\n"
                    "✍️ **Content Creator / Writer** — blogs, articles, social media\n"
                    "📢 **Public Relations Specialist** — managing organizational image\n"
                    "🎬 **Film/Video Producer** — creating video content\n"
                    "📱 **Digital Marketing Manager** — online campaigns and strategy\n"
                    "🎙️ **Podcast / Media Host** — audio and digital media\n\n"
                    "The media industry is rapidly evolving — digital skills are highly valued alongside traditional journalism!"
                )

            # General major/career questions
            if any(w in msg_lower for w in ['best major for my future', 'major for my future', 'major is best', 'what major should', 'which major should', 'what should i study', 'choosing a major', 'choose a major', 'confused about choosing', 'confused about major', 'i am confused about choosing']):
                return (
                    "Choosing the right major is one of the most important decisions you'll make! Here's a simple framework:\n\n"
                    "1. **Passion** — What activities make you lose track of time?\n"
                    "2. **Strengths** — Which school subjects do you excel at?\n"
                    "3. **Market Demand** — Which careers have strong job opportunities?\n\n"
                    "Tell me your interests (e.g., 'I like computers and math' or 'I enjoy helping people') and I'll suggest the best majors for you specifically."
                )
            if any(w in msg_lower for w in ['career path', 'career suits', 'which career suits', 'right career', 'how do i choose a career', 'career for me']):
                return (
                    "Finding the right career path starts with knowing yourself. Ask yourself:\n\n"
                    "• Do you prefer **working with people** → consider Medicine, Psychology, Education\n"
                    "• Do you prefer **working with technology** → consider Computer Science, Engineering, AI\n"
                    "• Do you prefer **creative work** → consider Design, Architecture, Media\n"
                    "• Do you prefer **numbers and analysis** → consider Accounting, Finance, Data Science\n\n"
                    "Share more about your personality and I'll give you a tailored recommendation!"
                )
            if any(w in msg_lower for w in ['most in-demand', 'in demand jobs', 'best jobs', 'job market', 'high salary', 'highest paying', 'future jobs']):
                return (
                    "The most in-demand careers right now (2025–2030):\n\n"
                    "🥇 **AI & Machine Learning Engineer** — fastest growing field globally\n"
                    "🥈 **Cybersecurity Specialist** — critical shortage worldwide\n"
                    "🥉 **Data Scientist / Analyst** — needed in every industry\n"
                    "4️⃣ **Software Developer** — consistently high demand\n"
                    "5️⃣ **Healthcare Professional** — always stable demand\n"
                    "6️⃣ **Financial Analyst / Accountant** — essential in all businesses\n\n"
                    "Would you like details about any of these careers?"
                )

            # Personality-based questions
            if any(w in msg_lower for w in ['enjoy solving problems', 'solving problems and working with computers', 'working with computers', 'love technology', 'interested in tech']):
                return (
                    "Great profile! You're likely a **analytical/technical** person. Based on your interests, the best majors for you are:\n\n"
                    "🔹 **Computer Science** — programming, AI, systems\n"
                    "🔹 **Software Engineering** — building large-scale software\n"
                    "🔹 **Data Science** — analyzing data to find insights\n"
                    "🔹 **Cybersecurity** — protecting systems and networks\n"
                    "🔹 **Electrical Engineering** — hardware + software systems\n\n"
                    "All of these have excellent job markets and competitive salaries. Which one interests you most?"
                )
            if any(w in msg_lower for w in ['helping people', 'working in teams', 'like teamwork', 'social person', 'care about others', 'i like helping', 'enjoy helping', 'like helping', 'help people', 'work in teams', 'in teams']):
                return (
                    "You sound like a **social/empathetic** person — a great trait for many fields!\n\n"
                    "Best majors for you:\n"
                    "🔹 **Psychology** — understand and help people's mental health\n"
                    "🔹 **Nursing** — frontline patient care and support\n"
                    "🔹 **Education** — shape future generations\n"
                    "🔹 **Social Work** — help communities and families\n"
                    "🔹 **Human Resources** — manage and support employees\n"
                    "🔹 **Public Relations** — connect organizations with people\n\n"
                    "These careers are deeply rewarding. Want more info on any of them?"
                )
            if any(w in msg_lower for w in ['prefer creative work', 'creative work like design', 'like design and drawing', 'creative field', 'visual design', 'prefer creative']):
                return (
                    "You're a **creative thinker** — and there are fantastic careers for you!\n\n"
                    "Best majors for creative personalities:\n"
                    "🎨 **Graphic Design** — visual identity, branding, UI/UX\n"
                    "🏛️ **Architecture** — designing buildings and spaces\n"
                    "📱 **Digital Media** — content creation, video, animation\n"
                    "🖥️ **UI/UX Design** — designing apps and websites\n"
                    "🎬 **Film & Media Production** — storytelling through visuals\n\n"
                    "Creative fields are thriving in the digital age. Which area excites you most?"
                )
            if any(w in msg_lower for w in ["don't like math", 'hate math', 'not good at math', 'like communication', 'good at communication', 'like writing', 'like languages']):
                return (
                    "No problem — many great careers don't require heavy math!\n\n"
                    "Best options for you:\n"
                    "🔹 **Mass Communication / Journalism** — writing, reporting, media\n"
                    "🔹 **Public Relations** — managing image and communication\n"
                    "🔹 **Marketing** — creative campaigns and strategy\n"
                    "🔹 **English Language & Literature** — teaching, translation, writing\n"
                    "🔹 **Psychology** — understanding human behavior\n"
                    "🔹 **Law** — argumentation and communication skills\n\n"
                    "These fields value communication and critical thinking over math. Interested in any?"
                )

            # IT questions
            if 'computer science or information' in msg_lower or 'cs or is' in msg_lower or ('information systems' in msg_lower and 'computer science' in msg_lower):
                return (
                    "**Computer Science vs Information Systems:**\n\n"
                    "**Computer Science (CS):**\n"
                    "• Deep focus on programming, algorithms, AI, and theory\n"
                    "• Best for: software engineers, AI developers, researchers\n"
                    "• More technical and math-heavy\n\n"
                    "**Information Systems (IS):**\n"
                    "• Bridges business and technology\n"
                    "• Best for: system analysts, IT managers, business tech roles\n"
                    "• Less coding, more business focus\n\n"
                    "**Recommendation:** If you love coding → CS. If you like both business and tech → IS."
                )
            if any(w in msg_lower for w in ['become a software developer', 'skills for developer', 'skills needed for software', 'skills to become a developer', 'how to become a developer']):
                return (
                    "To become a successful software developer, you need:\n\n"
                    "**Core Technical Skills:**\n"
                    "• Programming languages: Python, JavaScript, Java, or C++\n"
                    "• Data structures and algorithms\n"
                    "• Version control (Git)\n"
                    "• Databases (SQL, NoSQL)\n\n"
                    "**Soft Skills:**\n"
                    "• Problem-solving mindset\n"
                    "• Attention to detail\n"
                    "• Continuous learning\n\n"
                    "**Best major:** Computer Science or Software Engineering. Start with Python — it's the easiest entry point!"
                )
            if any(w in msg_lower for w in ['cybersecurity', 'cyber security']) and 'vs' not in msg_lower and 'or' not in msg_lower and 'computer science' not in msg_lower:
                return (
                    "**Cybersecurity** is one of the hottest fields right now!\n\n"
                    "• **Why it's great:** Critical shortage of experts worldwide, high salaries, remote work options\n"
                    "• **What you'll do:** Protect systems, networks, and data from hackers and threats\n"
                    "• **Key skills:** Networking, ethical hacking, cryptography, incident response\n"
                    "• **Salary:** Very competitive — often $80,000–$150,000+ globally\n"
                    "• **Certifications:** CompTIA Security+, CEH, CISSP are highly valued\n\n"
                    "If you like problem-solving and have an interest in security → absolutely go for it!"
                )
            if any(w in msg_lower for w in ['ai and data science', 'ai vs data', 'difference between ai', 'artificial intelligence vs', 'data science vs', 'ai or data science']):
                return (
                    "**AI vs Data Science — What's the difference?**\n\n"
                    "**Artificial Intelligence (AI):**\n"
                    "• Building intelligent systems that can learn and make decisions\n"
                    "• Covers: machine learning, deep learning, robotics, NLP\n"
                    "• Focus: creating smart algorithms\n\n"
                    "**Data Science:**\n"
                    "• Extracting insights and patterns from large datasets\n"
                    "• Covers: statistics, data analysis, visualization, prediction\n"
                    "• Focus: understanding data to make business decisions\n\n"
                    "They overlap heavily — both require Python and math. AI is more engineering-focused; Data Science is more analytical."
                )

            # Medical questions
            if any(w in msg_lower for w in ['nursing and medicine', 'nursing vs medicine', 'nursing or medicine', 'difference between nursing and medicine']):
                return (
                    "**Nursing vs Medicine:**\n\n"
                    "**Medicine (Doctor):**\n"
                    "• 6–7 years of study + residency (3–7 more years)\n"
                    "• Diagnose and treat diseases, perform surgeries\n"
                    "• Higher authority and responsibility\n"
                    "• Very high salary but very demanding\n\n"
                    "**Nursing:**\n"
                    "• 3–4 years of study\n"
                    "• Direct patient care, monitoring, medication administration\n"
                    "• High demand globally, good salary, faster to enter workforce\n\n"
                    "**Choose Medicine** if you want the highest level of medical responsibility.\n"
                    "**Choose Nursing** if you want to work closely with patients and enter sooner."
                )

            # Business questions
            if any(w in msg_lower for w in ['business administration or accounting', 'business or accounting', 'accounting or business', 'business vs accounting']):
                return (
                    "**Business Administration vs Accounting:**\n\n"
                    "**Business Administration:**\n"
                    "• Broad coverage: management, marketing, HR, strategy, operations\n"
                    "• Best for: managers, entrepreneurs, consultants\n"
                    "• More flexible career paths\n\n"
                    "**Accounting:**\n"
                    "• Specialized in financial records, auditing, taxes\n"
                    "• Best for: accountants, auditors, financial analysts\n"
                    "• Very stable, always in demand\n\n"
                    "**Recommendation:** If you like variety → Business Admin. If you love numbers and financial detail → Accounting."
                )
            if 'marketing' in msg_lower and any(w in msg_lower for w in ['is marketing', 'marketing good', 'marketing major', 'study marketing', 'marketing career']):
                return (
                    "**Marketing** is an excellent and creative major!\n\n"
                    "• **What you'll study:** Consumer behavior, digital marketing, branding, market research, advertising\n"
                    "• **Career options:** Marketing manager, digital marketer, brand strategist, content creator, SEO specialist\n"
                    "• **Why it's great:** Every business needs marketing — huge demand across all industries\n"
                    "• **Digital Marketing** is especially booming — social media, SEO, paid ads\n\n"
                    "If you're creative AND analytical, marketing is a perfect blend of both worlds!"
                )

            # Architecture
            if any(w in msg_lower for w in ['architecture or interior', 'architecture vs interior', 'architecture or design', 'interior design vs architecture']):
                return (
                    "**Architecture vs Interior Design:**\n\n"
                    "**Architecture:**\n"
                    "• Designing entire buildings — structure, function, and aesthetics\n"
                    "• 5-year program, requires licensure\n"
                    "• Works on large-scale projects (residential, commercial, urban)\n\n"
                    "**Interior Design:**\n"
                    "• Designing indoor spaces — furniture, lighting, colors, layout\n"
                    "• 3–4 year program\n"
                    "• More focus on aesthetics and human comfort\n\n"
                    "**Choose Architecture** for large-scale structural design.\n"
                    "**Choose Interior Design** for space aesthetics and comfort."
                )

            # Comparison questions
            if any(w in msg_lower for w in ['computer science or cybersecurity', 'cs or cybersecurity', 'cs vs cyber', 'computer science vs cybersecurity']):
                return (
                    "**Computer Science vs Cybersecurity:**\n\n"
                    "**Computer Science:**\n"
                    "• Broad foundation: programming, AI, databases, algorithms\n"
                    "• More versatile — opens doors to many tech careers\n"
                    "• Better if you're unsure which tech area you prefer\n\n"
                    "**Cybersecurity:**\n"
                    "• Specialized focus: security, hacking, defense\n"
                    "• Extremely high demand and shortage of experts\n"
                    "• Can also be pursued as a specialization after a CS degree\n\n"
                    "**Recommendation:** Start with CS for the broader foundation, then specialize in cybersecurity."
                )
            if any(w in msg_lower for w in ['medicine or pharmacy', 'pharmacy or medicine', 'medicine vs pharmacy', 'pharmacy vs medicine']):
                return (
                    "**Medicine vs Pharmacy:**\n\n"
                    "**Medicine:**\n"
                    "• 6–7 years + residency\n"
                    "• Diagnose and treat patients directly\n"
                    "• Highest medical authority and salary\n"
                    "• Very demanding and competitive\n\n"
                    "**Pharmacy:**\n"
                    "• 5–6 years\n"
                    "• Expert in medications, their effects, and interactions\n"
                    "• Work in hospitals, clinics, research, or retail\n"
                    "• Less stressful than medicine, still excellent salary\n\n"
                    "**Choose Medicine** if you want to diagnose and treat patients.\n"
                    "**Choose Pharmacy** if you're fascinated by drugs and chemistry."
                )
            if any(w in msg_lower for w in ['business vs engineering', 'engineering vs business', 'business or engineering']):
                return (
                    "**Business vs Engineering:**\n\n"
                    "**Engineering:**\n"
                    "• Technical problem-solving — building, designing, creating\n"
                    "• Strong math and science focus\n"
                    "• High salary, especially in tech-heavy industries\n\n"
                    "**Business:**\n"
                    "• Managing organizations, strategy, marketing, finance\n"
                    "• People and communication skills emphasized\n"
                    "• Very versatile across all industries\n\n"
                    "**Choose Engineering** if you love math, science, and building things.\n"
                    "**Choose Business** if you prefer leadership, strategy, and working with people."
                )

            # Interest-based recommendations
            if any(w in msg_lower for w in ['technology and creativity', 'tech and creative', 'technology and creativity', 'interests in technology and creativity']):
                return (
                    "Technology + Creativity = an amazing combination! Here are perfect majors for you:\n\n"
                    "🥇 **UI/UX Design** — designing apps and websites with both tech and creativity\n"
                    "🥈 **Digital Media & Animation** — creating digital content using software\n"
                    "🥉 **Game Design** — building interactive experiences\n"
                    "4️⃣ **Multimedia Engineering** — combining visual design with programming\n"
                    "5️⃣ **Architecture** — where engineering meets art\n\n"
                    "These fields perfectly combine technical skills with creative thinking — growing rapidly in the digital economy!"
                )
            if any(w in msg_lower for w in ['analysis and numbers', 'like analysis', 'likes analysis', 'like numbers', 'data and numbers', 'recommend a career for someone', 'likes analysis and numbers', 'who likes analysis', 'someone who likes', 'career for someone']):
                return (
                    "You're built for **analytical careers** — here are the best paths:\n\n"
                    "🔹 **Data Science** — find patterns and insights in large datasets\n"
                    "🔹 **Financial Analysis** — analyze markets and investments\n"
                    "🔹 **Actuarial Science** — calculate risk using statistics\n"
                    "🔹 **Economics** — study how markets and money work\n"
                    "🔹 **Accounting** — precise financial management\n"
                    "🔹 **AI & Machine Learning** — building systems that learn from data\n\n"
                    "All of these are high-paying, in-demand, and perfect for analytical thinkers!"
                )
            if any(w in msg_lower for w in ['based on my interests', 'suggest a major', 'based on my personality', 'recommend for me', 'what should i do', 'recommend a career path']):
                return (
                    "I'd love to give you a personalized recommendation! To do that, tell me:\n\n"
                    "1. **What subjects do you enjoy?** (math, biology, languages, arts, etc.)\n"
                    "2. **What activities do you love?** (building things, helping people, creating, analyzing)\n"
                    "3. **What kind of work environment do you prefer?** (office, field, hospital, studio)\n\n"
                    "For example: 'I love math and computers' or 'I enjoy helping people and working in teams' — and I'll suggest the perfect major for you!"
                )

            # General
            if any(w in msg_lower for w in ['compare two', 'comparison between', 'difference between', 'which is better', 'vs']) and not any(kw in msg_lower for kw in ['computer science or cy', 'medicine or pharmacy', 'business vs eng', 'nursing or medicine']):
                return "I'd be happy to compare! Just tell me which two majors or careers you're comparing and I'll break down the differences in study content, career options, and salaries."
            if any(w in msg_lower for w in ['salary', 'how much', 'earn', 'income', 'pay']):
                return (
                    "Salaries vary widely by field and experience. Here's a quick guide:\n\n"
                    "💰 **Highest paying:** Medicine, Engineering (esp. Software), Law\n"
                    "🔹 **Very good:** Computer Science, Data Science, Finance\n"
                    "🔸 **Good:** Business, Accounting, Pharmacy\n"
                    "🎨 **Variable:** Design, Media, Psychology (depends on specialization)\n\n"
                    "Which specific major would you like salary details for?"
                )
        return None

    def _compose_generic_reply(self, msg: str, language: str) -> str:
        """Compose a generic but content-aware reply based on actual message."""
        is_question = '?' in msg or '؟' in msg
        words = msg.split()
        if language == 'arabic':
            if is_question:
                return (
                    f"سؤال وجيه! للإجابة عليك بدقة، هل يمكنك إخباري أكثر عن ما تبحث عنه؟ "
                    f"أنا متخصص في مساعدتك على اختيار التخصص الجامعي وتزويدك بمعلومات عن أي مجال دراسي أو مهني."
                )
            return (
                "شكراً على رسالتك! أنا هنا لمساعدتك في كل ما يتعلق بالتخصصات الجامعية وسوق العمل. "
                "يمكنك سؤالي عن أي تخصص، الرواتب المتوقعة، فرص العمل، أو مقارنة بين تخصصين."
            )
        else:
            if is_question:
                return (
                    "Good question! To give you a precise answer, could you tell me a bit more about what you're looking for? "
                    "I specialize in helping students choose university majors and providing info about any academic or professional field."
                )
            return (
                "Thanks for your message! I'm here to help with everything related to university majors and career paths. "
                "Feel free to ask about any major, expected salaries, job opportunities, or comparisons between fields."
            )

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
            if any(w in msg for w in ['مرحبا', 'هلا', 'أهلا', 'سلام', 'كيف حال']):
                return "أهلاً بك! أنا المساعد الأكاديمي الذكي. كيف يمكنني مساعدتك اليوم في مسيرتك الجامعية أو الإجابة على استفساراتك؟"
            if any(w in msg for w in ['من أنت', 'مين انت', 'شسمك', 'اسمك']):
                return "أنا مساعدك الأكاديمي الافتراضي. هدفي هو مساعدتك في اكتشاف شغفك واختيار التخصص الجامعي الأنسب لك والإجابة عن أي استفسارات لديك."
            if any(w in msg for w in ['شكرا', 'يعطيك العافية', 'تسلم']):
                return "عفواً! أنا دائماً هنا لمساعدتك. لا تتردد في طرح أي أسئلة أخرى."
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
            # Generic conversational fallback based on input
            if len(msg.split()) > 3 and "?" in msg or "؟" in msg:
                return "هذا سؤال مثير للاهتمام! لكي أقدم لك إجابة دقيقة، هل يمكنك ربط هذا بمجال دراستك أو اهتماماتك؟ أنا هنا لتقديم الدعم الأكاديمي والمعرفي."
        else:
            if any(w in msg for w in ['hello', 'hi', 'hey', 'how are you']):
                return "Hello! I am your smart academic assistant. How can I help you today with your university journey or answer your questions?"
            if any(w in msg for w in ['who are you', 'your name']):
                return "I am your virtual academic assistant. My goal is to help you discover your passion, choose the right major, and answer any questions you have."
            if any(w in msg for w in ['thanks', 'thank you', 'appreciate']):
                return "You're welcome! I'm always here to help. Feel free to ask any other questions."
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
            if len(msg.split()) > 3 and "?" in msg:
                return "That's an interesting question! To give you a precise answer, could you relate this to your studies or interests? I'm here to provide academic and knowledge support."
        return None
