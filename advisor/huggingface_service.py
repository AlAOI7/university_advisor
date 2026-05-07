# advisor/huggingface_service.py
"""
خدمة Hugging Face Inference API - مجانية 100%
Free AI model service using Hugging Face
"""

import requests
import json
import logging
from typing import Dict, List, Optional
from django.conf import settings

logger = logging.getLogger(__name__)

class HuggingFaceService:
    """
    خدمة مجانية للذكاء الاصطناعي باستخدام Hugging Face
    Free AI service using Hugging Face Inference API
    
    الميزات:
    - مجاني 100% (بدون API key مطلوب للنماذج العامة)
    - لا يحتاج تثبيت مكتبات إضافية (requests فقط)
    - يدعم العربية والإنجليزية
    - سرعة جيدة
    """
    
    # نماذج مجانية متاحة
    MODELS = {
        'sentiment':  'cardiffnlp/twitter-xlm-roberta-base-sentiment',
        'text_gen': 'facebook/opt-350m',  # نموذج توليد نصوص صغير وسريع
        'multilingual': 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
    }
    
    def __init__(self):
        """تهيئة الخدمة"""
        self.api_url = "https://api-inference.huggingface.co/models/"
        self.api_key = getattr(settings, 'HUGGINGFACE_API_KEY', None)
        self.is_configured = True # متاح بدون API key!
        logger.info("HuggingFace Service initialized (Free tier)")
    
    def analyze_personality(self, user_data: Dict) -> Dict:
        """
        تحليل الشخصية باستخدام Hugging Face
        
        Args:
            user_data: بيانات المستخدم (personality_scores, interests)
        
        Returns:
            تحليل شامل للشخصية
        """
        try:
            # استخراج البيانات
            personality_scores = user_data.get('personality_scores', {})
            interests = user_data.get('interests', {})
            
            # تحديد نوع الشخصية
            personality_type = self._determine_personality_type(personality_scores)
            
            # توليد الوصف باستخدام AI
            description = self._generate_personality_description(
                personality_type,
                personality_scores,
                interests
            )
            
            return {
                'personality_type': personality_type,
                'description': description,
                'strengths': self._get_strengths(personality_type),
                'weaknesses': self._get_weaknesses(personality_type),
                'learning_style': self._get_learning_style(personality_type),
                'career_paths': self._get_career_paths(personality_type),
                'confidence_score': 0.85,
                'source': 'HuggingFace (Free)'
            }
        
        except Exception as e:
            logger.error(f"HuggingFace analysis error: {e}")
            return self._get_fallback_analysis()
    
    def _determine_personality_type(self, scores: Dict) -> str:
        """تحديد نوع الشخصية الرئيسي"""
        if not scores:
            return 'متوازن'
        
        # إيجاد أعلى درجة
        max_trait = max(scores.items(), key=lambda x: x[1])
        
        # تحديد النوع بالعربية
        trait_map = {
            'analytical': 'تحليلي',
            'creative': 'إبداعي',
            'social': 'اجتماعي',
            'organized': 'تنظيمي',
            'practical': 'عملي',
            'تحليلي': 'تحليلي',
            'إبداعي': 'إبداعي',
            'اجتماعي': 'اجتماعي',
            'تنظيمي': 'تنظيمي',
            'عملي': 'عملي'
        }
        
        return trait_map.get(max_trait[0], 'متوازن')
    
    def _generate_personality_description(self, personality_type: str, 
                                          scores: Dict, interests: Dict) -> str:
        """توليد وصف شخصي باستخدام AI"""
        
        # بناء prompt
        prompt = self._build_description_prompt(personality_type, scores, interests)
        
        try:
            # محاولة استخدام نموذج توليد النصوص
            response = self._query_huggingface(
                self.MODELS['text_gen'],
                {"inputs": prompt, "parameters": {"max_length": 200}}
            )
            
            if response and isinstance(response, list) and len(response) > 0:
                generated = response[0].get('generated_text', '')
                if generated:
                    return generated
        
        except Exception as e:
            logger.warning(f"Text generation failed, using fallback: {e}")
        
        # Fallback: قالب ثابت
        return self._get_template_description(personality_type)
    
    def _build_description_prompt(self, personality_type: str, 
                                  scores: Dict, interests: Dict) -> str:
        """بناء prompt لتوليد الوصف"""
        
        interests_str = ', '.join(list(interests.keys())[:3]) if interests else 'متنوعة'
        
        prompt = f"""Describe a student with {personality_type} personality.
Their interests are: {interests_str}.
Provide a brief, positive description in Arabic focusing on their strengths and suitable career paths.

الطالب ذو شخصية {personality_type}"""
        
        return prompt
    
    def _query_huggingface(self, model: str, payload: Dict) -> Optional[str]:
        """إرسال طلب إلى Hugging Face API"""
        
        headers = {}
        if self.api_key:
            headers['Authorization'] = f"Bearer {self.api_key}"
        
        url = f"{self.api_url}{model}"
        
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.warning(f"HuggingFace API returned {response.status_code}")
                return None
        
        except requests.exceptions.RequestException as e:
            logger.error(f"Request to HuggingFace failed: {e}")
            return None
    
    def _get_strengths(self, personality_type: str) -> List[str]:
        """نقاط القوة حسب نوع الشخصية"""
        
        strengths_map = {
            'تحليلي': [
                'التفكير المنطقي والنقدي',
                'حل المشكلات المعقدة',
                'الدقة في التفاصيل',
                'القدرة على التحليل العميق',
                'اتخاذ قرارات مبنية على البيانات'
            ],
            'إبداعي': [
                'التفكير خارج الصندوق',
                'الابتكار والخيال الواسع',
                'التعبير الفني',
                'حل المشكلات بطرق غير تقليدية',
                'الشغف بالتجديد'
            ],
            'اجتماعي': [
                'مهارات التواصل الممتازة',
                'القدرة على بناء العلاقات',
                'العمل الجماعي الفعال',
                'التعاطف مع الآخرين',
                'القيادة والتأثير'
            ],
            'تنظيمي': [
                'التخطيط الممتاز',
                'إدارة الوقت بكفاءة',
                'الدقة والانضباط',
                'القدرة على التنظيم',
                'الالتزام بالمواعيد'
            ],
            'عملي': [
                'التطبيق العملي للمعرفة',
                'المهارات اليدوية',
                'حل المشكلات الواقعية',
                'التركيز على النتائج',
                'القدرة على التنفيذ'
            ]
        }
        
        return strengths_map.get(personality_type, strengths_map['تحليلي'])
    
    def _get_weaknesses(self, personality_type: str) -> List[str]:
        """نقاط الضعف للعمل عليها"""
        
        weaknesses_map = {
            'تحليلي': ['التردد في القرارات السريعة', 'التركيز الزائد على التفاصيل'],
            'إبداعي': ['صعوبة التنظيم أحياناً', 'الانشغال بالأفكار الجديدة'],
            'اجتماعي': ['صعوبة العمل منفرداً لفترات طويلة', 'الحساسية العاطفية'],
            'تنظيمي': ['المرونة في التغيير', 'القلق من عدم الانضباط'],
            'عملي': ['الصبر على الأمور النظرية', 'التخطيط طويل المدى']
        }
        
        return weaknesses_map.get(personality_type, [])
    
    def _get_learning_style(self, personality_type: str) -> str:
        """أسلوب التعلم المفضل"""
        
        styles = {
            'تحليلي': 'التعلم من خلال البحث والتحليل والدراسة المعمقة',
            'إبداعي': 'التعلم من خلال المشاريع الإبداعية والتجريب',
            'اجتماعي': 'التعلم من خلال المناقشات والعمل الجماعي',
            'تنظيمي': 'التعلم من خلال الجداول المنظمة والخطط الواضحة',
            'عملي': 'التعلم من خلال التطبيق العملي والتدريب'
        }
        
        return styles.get(personality_type, 'التعلم المتنوع')
    
    def _get_career_paths(self, personality_type: str) -> List[str]:
        """المسارات المهنية المناسبة"""
        
        careers = {
            'تحليلي': [
                'علوم الحاسب والبرمجة',
                'الهندسة',
                'المالية والاقتصاد',
                'علوم البيانات',
                'البحث العلمي'
            ],
            'إبداعي': [
                'التصميم والفنون',
                'الإعلام والاتصال',
                'الهندسة المعمارية',
                'الكتابة والأدب',
                'التسويق الإبداعي'
            ],
            'اجتماعي': [
                'التعليم',
                'الطب والتمريض',
                'علم النفس',
                'الخدمة الاجتماعية',
                'إدارة الموارد البشرية'
            ],
            'تنظيمي': [
                'إدارة الأعمال',
                'المحاسبة',
                'إدارة المشاريع',
                'القانون',
                'اللوجستيات'
            ],
            'عملي': [
                'الهندسة التطبيقية',
                'الطب',
                'الزراعة',
                'التقنية المهنية',
                'الصناعة'
            ]
        }
        
        return careers.get(personality_type, careers['تحليلي'])
    
    def _get_template_description(self, personality_type: str) -> str:
        """وصف قالبي للشخصية"""
        
        templates = {
            'تحليلي': 'أنت شخص يتميز بالتفكير المنطقي والنقدي. تفضل تحليل المعلومات بعمق قبل اتخاذ القرارات. مهاراتك في حل المشكلات المعقدة ممتازة، وتستمتع بالعمل مع البيانات والأرقام.',
            
            'إبداعي': 'أنت شخص مبدع يتمتع بخيال واسع وقدرة على التفكير خارج الصندوق. تحب التجديد والابتكار، وتستمتع بالتعبير عن أفكارك الفريدة بطرق مبتكرة.',
            
            'اجتماعي': 'أنت شخص اجتماعي يحب التواصل مع الآخرين وبناء العلاقات. مهاراتك في التعامل مع الناس ممتازة، وتستمتع بالعمل الجماعي ومساعدة الآخرين.',
            
            'تنظيمي': 'أنت شخص منظم يتميز بالدقة والانضباط. تفضل التخطيط المسبق والعمل وفق جداول محددة. مهاراتك في إدارة الوقت والمشاريع ممتازة.',
            
            'عملي': 'أنت شخص عملي يفضل التطبيق على النظرية. تستمتع بحل المشكلات الواقعية والعمل بيديك. تركز على النتائج الملموسة والتنفيذ الفعال.'
        }
        
        return templates.get(personality_type, templates['تحليلي'])
    
    def _get_fallback_analysis(self) -> Dict:
        """تحليل احتياطي في حالة الفشل"""
        return {
            'personality_type': 'متوازن',
            'description': 'شخصية متوازنة تجمع بين عدة سمات إيجابية',
            'strengths': ['التكيف', 'المرونة', 'التنوع'],
            'weaknesses': [],
            'learning_style': 'متنوع',
            'career_paths': ['متعدد'],
            'confidence_score': 0.6,
            'source': 'Fallback'
        }
    
    def recommend_majors(self, personality_analysis: Dict, interests: List) -> List[Dict]:
        """التوصية بالتخصصات بناءً على التحليل"""

        personality_type = personality_analysis.get('personality_type', 'متوازن')
        career_paths = personality_analysis.get('career_paths', [])

        try:
            from majors.models import Major
            from django.db.models import Q  # Fix: was using models.Q without import

            recommendations = []

            for career in career_paths[:5]:
                matching_majors = Major.objects.filter(
                    Q(name__icontains=career) |
                    Q(description__icontains=career)
                )[:2]

                seen_ids = {r['major'].id for r in recommendations if hasattr(r.get('major'), 'id')}
                for major in matching_majors:
                    if major.id not in seen_ids:
                        seen_ids.add(major.id)
                        match_score = self._calculate_match_score(
                            major, personality_type, interests
                        )
                        recommendations.append({
                            'major': major,
                            'match_percentage': match_score,
                            'reasons': self._get_match_reasons(major, personality_type),
                        })

            recommendations.sort(key=lambda x: x['match_percentage'], reverse=True)
            return recommendations[:10]

        except Exception as e:
            logger.error(f"recommend_majors error: {e}")
            return []
    
    def _calculate_match_score(self, major, personality_type: str, interests: List) -> float:
        """حساب نسبة التطابق"""
        score = 60.0  # قاعدة
        
        # زيادة بناءً على الشخصية
        if personality_type in major.description:
            score += 20
        
        # زيادة بناءً على الاهتمامات
        for interest in interests[:3]:
            if interest.lower() in major.description.lower():
                score += 5
        
        return min(score, 95.0)
    
    def _get_match_reasons(self, major, personality_type: str) -> List[str]:
        """أسباب التوصية"""
        return [
            f'يناسب الشخصية {personality_type}',
            'فرص عمل واسعة',
            'مستقبل وظيفي واعد'
        ]


# اختبار سريع
if __name__ == '__main__':
    service = HuggingFaceService()
    
    test_data = {
        'personality_scores': {
            'تحليلي': 9,
            'إبداعي': 4
        },
        'interests': {
            'البرمجة': 9,
            'التكنولوجيا': 8
        }
    }
    
    result = service.analyze_personality(test_data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
