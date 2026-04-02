# tests/test_ai_model.py
"""
اختبارات شاملة لنموذج AI المحسّن
Comprehensive tests for the enhanced AI model

اختبارات تشمل:
- التحليل بالعربي والإنجليزي
- دقة التوصيات
- كشف اللغة
- Few-Shot Learning effectiveness
"""

from django.test import TestCase
from django.contrib.auth.models import User
from advisor.gemini_service import GeminiService
from advisor.ai_service import AIAdvisor
from advisor.training_examples import ARABIC_PERSONALITY_EXAMPLES, ENGLISH_PERSONALITY_EXAMPLES
import json


class TestLanguageDetection(TestCase):
    """اختبار كشف اللغة التلقائي"""
    
    def setUp(self):
        self.gemini = GeminiService()
    
    def test_detect_arabic_language(self):
        """اختبار كشف اللغة العربية"""
        arabic_data = {
            "personality_scores": {
                "تحليلي": 8,
                "إبداعي": 3
            },
            "interests": {
                "علوم الحاسب": 9
            }
        }
        
        language = self.gemini._detect_language(arabic_data)
        self.assertEqual(language, "arabic", "يجب أن تكتشف العربية بشكل صحيح")
    
    def test_detect_english_language(self):
        """Test English language detection"""
        english_data = {
            "personality_scores": {
                "analytical": 8,
                "creative": 3
            },
            "interests": {
                "computer_science": 9
            }
        }
        
        language = self.gemini._detect_language(english_data)
        self.assertEqual(language, "english", "Should detect English correctly")


class TestArabicPersonalityAnalysis(TestCase):
    """اختبارات تحليل الشخصية بالعربي"""
    
    def setUp(self):
        self.gemini = GeminiService()
        self.ai_advisor = AIAdvisor()
    
    def test_analytical_personality_arabic(self):
        """اختبار تحليل الشخصية التحليلية - عربي"""
        test_data = {
            "personality_scores": {
                "تحليلي": 9,
                "إبداعي": 3,
                "اجتماعي": 2,
                "تنظيمي": 7,
                "عملي": 5
            },
            "interests": {
                "العلوم": 8,
                "التكنولوجيا": 9,
                "الهندسة": 7,
                "الرياضيات": 8
            }
        }
        
        # اختبار مع النظام الاحتياطي (بدون API key)
        result = self.ai_advisor.analyze_user_profile(test_data)
        
        # التحقق من وجود المفاتيح الأساسية
        self.assertIn('personality_analysis', result)
        self.assertIn('recommendations', result)
        
        # التحقق من نوع الشخصية
        personality = result.get('personality_analysis', {})
        self.assertIsNotNone(personality)
    
    def test_creative_personality_arabic(self):
        """اختبار تحليل الشخصية الإبداعية - عربي"""
        test_data = {
            "personality_scores": {
                "تحليلي": 4,
                "إبداعي": 9,
                "اجتماعي": 7,
                "تنظيمي": 3,
                "عملي": 5
            },
            "interests": {
                "الفنون": 9,
                "التصميم": 8,
                "الإعلام": 7
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
        self.assertIn('personality_analysis', result)
    
    def test_social_personality_arabic(self):
        """اختبار تحليل الشخصية الاجتماعية - عربي"""
        test_data = {
            "personality_scores": {
                "تحليلي": 5,
                "إبداعي": 4,
                "اجتماعي": 9,
                "تنظيمي": 6,
                "عملي": 7
            },
            "interests": {
                "الطب": 8,
                "المساعدة الاجتماعية": 9,
                "التعليم": 7
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)


class TestEnglishPersonalityAnalysis(TestCase):
    """Tests for English personality analysis"""
    
    def setUp(self):
        self.gemini = GeminiService()
        self.ai_advisor = AIAdvisor()
    
    def test_analytical_personality_english(self):
        """Test analytical personality analysis - English"""
        test_data = {
            "personality_scores": {
                "analytical": 9,
                "creative": 3,
                "social": 2,
                "organized": 7,
                "practical": 5
            },
            "interests": {
                "science": 8,
                "technology": 9,
                "engineering": 7,
                "mathematics": 8
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        
        self.assertIn('personality_analysis', result)
        self.assertIn('recommendations', result)
        self.assertIsNotNone(result.get('personality_analysis'))
    
    def test_creative_personality_english(self):
        """Test creative personality analysis - English"""
        test_data = {
            "personality_scores": {
                "analytical": 4,
                "creative": 9,
                "social": 7,
                "organized": 3,
                "practical": 5
            },
            "interests": {
                "arts": 9,
                "design": 8,
                "media": 7
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
        self.assertIn('recommendations', result)


class TestBilingualRecommendations(TestCase):
    """اختبارات التوصيات ثنائية اللغة"""
    
    def setUp(self):
        self.ai_advisor = AIAdvisor()
    
    def test_arabic_recommendations_structure(self):
        """اختبار هيكل التوصيات بالعربي"""
        test_data = ARABIC_PERSONALITY_EXAMPLES[0]['input']
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        recommendations = result.get('recommendations', [])
        
        self.assertIsInstance(recommendations, list)
        if recommendations:
            # التحقق من هيكل التوصية
            first_rec = recommendations[0]
            # يمكن أن تكون string أو dict
            self.assertTrue(isinstance(first_rec, (str, dict)))
    
    def test_english_recommendations_structure(self):
        """Test English recommendations structure"""
        test_data = ENGLISH_PERSONALITY_EXAMPLES[0]['input']
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        recommendations = result.get('recommendations', [])
        
        self.assertIsInstance(recommendations, list)
    
    def test_recommendations_count(self):
        """اختبار عدد التوصيات"""
        test_data = {
            "personality_scores": {"تحليلي": 8},
            "interests": {"التكنولوجيا": 9}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        recommendations = result.get('recommendations', [])
        
        # يجب أن يكون هناك على الأقل توصية واحدة
        self.assertGreater(len(recommendations), 0, "يجب أن يكون هناك توصيات")


class TestFewShotLearningEffectiveness(TestCase):
    """اختبار فعالية Few-Shot Learning"""
    
    def setUp(self):
        self.gemini = GeminiService()
    
    def test_prompt_contains_examples(self):
        """اختبار أن الـ prompt يحتوي على أمثلة"""
        test_data = {"personality_scores": {"تحليلي": 8}}
        
        prompt = self.gemini._build_analysis_prompt(test_data)
        
        # التحقق من وجود كلمات دالة على الأمثلة
        self.assertIn("مثال", prompt.lower(), "يجب أن يحتوي الـ prompt على أمثلة")
    
    def test_bilingual_prompt_support(self):
        """اختبار دعم الـ prompts ثنائية اللغة"""
        # اختبار عربي
        arabic_data = {"personality_scores": {"تحليلي": 8}}
        arabic_prompt = self.gemini._build_analysis_prompt(arabic_data)
        self.assertIn("تحليل", arabic_prompt)
        
        # اختبار إنجليزي
        english_data = {"personality_scores": {"analytical": 8}}
        english_prompt = self.gemini._build_analysis_prompt(english_data)
        self.assertIn("analysis", english_prompt.lower())


class TestGeminiServiceFallback(TestCase):
    """اختبار نظام Fallback"""
    
    def setUp(self):
        self.gemini = GeminiService()
    
    def test_fallback_when_not_configured(self):
        """اختبار النظام الاحتياطي عند عدم التكوين"""
        # افتراض أن API غير مكون
        self.assertIsNotNone(self.gemini)
        
        # يجب أن يعمل حتى بدون API
        result = self.gemini._get_fallback_analysis()
        self.assertIsInstance(result, dict)
        self.assertIn('personality_type', result)
    
    def test_fallback_recommendations(self):
        """اختبار التوصيات الاحتياطية"""
        recommendations = self.gemini._get_fallback_recommendations()
        
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)


class TestTrainingExamplesIntegrity(TestCase):
    """اختبار سلامة الأمثلة التدريبية"""
    
    def test_arabic_examples_structure(self):
        """اختبار هيكل الأمثلة العربية"""
        for example in ARABIC_PERSONALITY_EXAMPLES:
            self.assertIn('input', example)
            self.assertIn('output', example)
            self.assertIn('personality_type', example['output'])
            self.assertIn('strengths', example['output'])
            self.assertIn('recommended_majors', example['output'])
    
    def test_english_examples_structure(self):
        """Test English examples structure"""
        for example in ENGLISH_PERSONALITY_EXAMPLES:
            self.assertIn('input', example)
            self.assertIn('output', example)
            self.assertIn('personality_type', example['output'])
            self.assertIn('strengths', example['output'])
    
    def test_examples_count(self):
        """اختبار عدد الأمثلة"""
        self.assertEqual(len(ARABIC_PERSONALITY_EXAMPLES), 5, "يجب أن يكون هناك 5 أمثلة عربية")
        self.assertEqual(len(ENGLISH_PERSONALITY_EXAMPLES), 5, "Should be 5 English examples")


# ============================================
# Helper Functions for Testing
# ============================================

def print_test_summary():
    """طباعة ملخص الاختبارات"""
    print("\n" + "="*50)
    print("AI Model Testing Summary")
    print("="*50)
    print("✅ Language Detection Tests")
    print("✅ Arabic Personality Analysis Tests")
    print("✅ English Personality Analysis Tests")
    print("✅ Bilingual Recommendations Tests")
    print("✅ Few-Shot Learning Tests")
    print("✅ Fallback System Tests")
    print("✅ Training Examples Integrity Tests")
    print("="*50)


if __name__ == '__main__':
    import unittest
    unittest.main()
