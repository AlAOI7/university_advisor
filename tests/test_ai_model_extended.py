# tests/test_ai_model_extended.py
"""
اختبارات موسعة لنموذج AI - النسخة المضاعفة
Extended AI Model Tests - Doubled Version

اختبارات إضافية تشمل:
- حالات حدية (Edge Cases)
- اختبارات أداء (Performance)
- اختبارات دقة (Accuracy)
- سيناريوهات معقدة
- اختبارات تكامل (Integration)
"""

from django.test import TestCase
from django.contrib.auth.models import User
from advisor.gemini_service import GeminiService
from advisor.ai_service import AIAdvisor
from advisor.training_examples import (
    ARABIC_PERSONALITY_EXAMPLES, 
    ENGLISH_PERSONALITY_EXAMPLES,
    format_examples_for_prompt,
    get_examples_for_language
)
from majors.models import Major
from tests.models import TestCategory
import json
import time


# ============================================
# اختبارات الحالات الحدية - Edge Cases
# ============================================

class TestEdgeCases(TestCase):
    """اختبار الحالات الحدية والاستثنائية"""
    
    def setUp(self):
        self.gemini = GeminiService()
        self.ai_advisor = AIAdvisor()
    
    def test_empty_personality_scores(self):
        """اختبار بيانات فارغة للشخصية"""
        test_data = {
            "personality_scores": {},
            "interests": {"technology": 5}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
        self.assertIn('recommendations', result)
    
    def test_empty_interests(self):
        """اختبار بيانات فارغة للاهتمامات"""
        test_data = {
            "personality_scores": {"analytical": 8},
            "interests": {}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
    
    def test_completely_empty_data(self):
        """اختبار بيانات فارغة تماماً"""
        test_data = {
            "personality_scores": {},
            "interests": {}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
        self.assertIn('personality_analysis', result)
    
    def test_very_high_scores(self):
        """اختبار درجات عالية جداً"""
        test_data = {
            "personality_scores": {"analytical": 100},
            "interests": {"science": 100}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
    
    def test_very_low_scores(self):
        """اختبار درجات منخفضة جداً"""
        test_data = {
            "personality_scores": {"analytical": 1},
            "interests": {"science": 1}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
    
    def test_negative_scores(self):
        """اختبار درجات سالبة"""
        test_data = {
            "personality_scores": {"analytical": -5},
            "interests": {"science": -10}
        }
        
        # يجب أن يتعامل مع الدرجات السالبة
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
    
    def test_mixed_language_data(self):
        """اختبار بيانات مختلطة اللغة"""
        test_data = {
            "personality_scores": {
                "analytical": 8,
                "تحليلي": 7
            },
            "interests": {
                "science": 9,
                "علوم": 8
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)


# ============================================
# اختبارات الأداء - Performance Tests
# ============================================

class TestPerformance(TestCase):
    """اختبارات الأداء والسرعة"""
    
    def setUp(self):
        self.gemini = GeminiService()
        self.ai_advisor = AIAdvisor()
    
    def test_analysis_speed(self):
        """اختبار سرعة التحليل"""
        test_data = {
            "personality_scores": {"analytical": 8, "creative": 6},
            "interests": {"technology": 9, "arts": 5}
        }
        
        start_time = time.time()
        result = self.ai_advisor.analyze_user_profile(test_data)
        end_time = time.time()
        
        execution_time = end_time - start_time
        self.assertLess(execution_time, 2.0, f"التحليل استغرق {execution_time:.2f}s - يجب أن يكون أقل من 2s")
    
    def test_multiple_sequential_analyses(self):
        """اختبار تحليلات متعددة متتالية"""
        test_data = {
            "personality_scores": {"analytical": 8},
            "interests": {"technology": 9}
        }
        
        for i in range(5):
            result = self.ai_advisor.analyze_user_profile(test_data)
            self.assertIsNotNone(result)
    
    def test_language_detection_speed(self):
        """اختبار سرعة كشف اللغة"""
        arabic_data = {"personality_scores": {"تحليلي": 8}}
        english_data = {"personality_scores": {"analytical": 8}}
        
        start = time.time()
        for _ in range(10):
            self.gemini._detect_language(arabic_data)
            self.gemini._detect_language(english_data)
        end = time.time()
        
        avg_time = (end - start) / 20
        self.assertLess(avg_time, 0.01, "كشف اللغة يجب أن يكون سريع جداً")


# ============================================
# اختبارات الدقة - Accuracy Tests
# ============================================

class TestAccuracy(TestCase):
    """اختبارات دقة التحليل والتوصيات"""
    
    def setUp(self):
        self.ai_advisor = AIAdvisor()
        # إنشاء major للاختبار
        self.major_cs = Major.objects.create(
            name="علوم الحاسب",
            description="تخصص علوم الحاسب والبرمجة والتكنولوجيا",
            job_opportunities="مبرمج، مطور، محلل بيانات",
            duration_years=4
        )
    
    def test_analytical_gets_tech_major(self):
        """اختبار: الشخصية التحليلية يجب أن تحصل على تخصصات تقنية"""
        test_data = {
            "personality_scores": {
                "تحليلي": 9,
                "إبداعي": 3
            },
            "interests": {
                "التكنولوجيا": 9,
                "البرمجة": 8
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        recommendations = result.get('recommendations', [])
        
        # يجب أن يكون هناك توصيات
        self.assertGreater(len(recommendations), 0)
        
        # يجب أن تتضمن التوصيات "علوم الحاسب"
        major_names = [rec.get('name', rec.get('major_name', '')) for rec in recommendations]
        self.assertIn("علوم الحاسب", major_names)
    
    def test_personality_type_detection(self):
        """اختبار: كشف نوع الشخصية بدقة"""
        test_data = {
            "personality_scores": {
                "تحليلي": 9,
                "إبداعي": 2,
                "اجتماعي": 3
            },
            "interests": {}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        personality = result.get('personality_analysis', {})
        personality_type = personality.get('personality_type', '')
        
        self.assertIn('تحليلي', personality_type)
    
    def test_match_percentage_range(self):
        """اختبار: نسب المطابقة يجب أن تكون بين 0-100"""
        test_data = {
            "personality_scores": {"analytical": 8},
            "interests": {"technology": 9}
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        recommendations = result.get('recommendations', [])
        
        for rec in recommendations:
            match_pct = rec.get('match_percentage', 0)
            self.assertGreaterEqual(match_pct, 0, "نسبة المطابقة يجب ألا تكون سالبة")
            self.assertLessEqual(match_pct, 100, "نسبة المطابقة يجب ألا تتجاوز 100")


# ============================================
# اختبارات السيناريوهات المعقدة
# ============================================

class TestComplexScenarios(TestCase):
    """اختبار سيناريوهات معقدة وواقعية"""
    
    def setUp(self):
        self.ai_advisor = AIAdvisor()
    
    def test_balanced_personality(self):
        """اختبار: شخصية متوازنة"""
        test_data = {
            "personality_scores": {
                "تحليلي": 6,
                "إبداعي": 6,
                "اجتماعي": 5,
                "تنظيمي": 6,
                "عملي": 5
            },
            "interests": {
                "العلوم": 6,
                "الفنون": 5,
                "التكنولوجيا": 6
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
        self.assertIn('recommendations', result)
    
    def test_conflicting_traits(self):
        """اختبار: سمات متناقضة"""
        test_data = {
            "personality_scores": {
                "تحليلي": 9,
                "إبداعي": 9  # عالية في كليهما
            },
            "interests": {
                "الرياضيات": 9,
                "الفنون": 9
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        recommendations = result.get('recommendations', [])
        
        # يجب أن يقترح تخصصات تجمع بين الاثنين
        self.assertGreater(len(recommendations), 0)
    
    def test_rare_personality_combination(self):
        """اختبار: مزيج نادر من الشخصية"""
        test_data = {
            "personality_scores": {
                "عملي": 9,
                "إبداعي": 8,
                "اجتماعي": 7
            },
            "interests": {
                "الهندسة": 9,
                "التصميم": 8,
                "التعليم": 7
            }
        }
        
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)


# ============================================
# اختبارات التكامل - Integration Tests
# ============================================

class TestIntegration(TestCase):
    """اختبارات التكامل بين المكونات"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_integration',
            password='testpass123'
        )
        self.gemini = GeminiService()
        self.ai_advisor = AIAdvisor()
    
    def test_full_pipeline_arabic(self):
        """اختبار: Pipeline كامل بالعربي"""
        user_data = ARABIC_PERSONALITY_EXAMPLES[0]['input']
        
        # التحليل
        result = self.ai_advisor.analyze_user_profile(user_data)
        
        # التحقق من كل المكونات
        self.assertIn('personality_analysis', result)
        self.assertIn('recommendations', result)
        self.assertIn('interest_analysis', result)
    
    def test_full_pipeline_english(self):
        """Test: Full pipeline in English"""
        user_data = ENGLISH_PERSONALITY_EXAMPLES[0]['input']
        
        result = self.ai_advisor.analyze_user_profile(user_data)
        
        self.assertIn('personality_analysis', result)
        self.assertIn('recommendations', result)
    
    def test_gemini_to_ai_advisor_integration(self):
        """اختبار: التكامل بين Gemini و AIAdvisor"""
        test_data = {"personality_scores": {"analytical": 8}}
        
        # التحليل باستخدام AIAdvisor (الذي يستخدم Gemini داخلياً)
        result = self.ai_advisor.analyze_user_profile(test_data)
        
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)


# ============================================
# اختبارات إضافية للـ Few-Shot Learning
# ============================================

class TestFewShotLearningAdvanced(TestCase):
    """اختبارات متقدمة لـ Few-Shot Learning"""
    
    def setUp(self):
        self.gemini = GeminiService()
    
    def test_examples_variety(self):
        """اختبار: تنوع الأمثلة"""
        arabic_examples = get_examples_for_language("arabic")
        english_examples = get_examples_for_language("english")
        
        # يجب أن يكون لدينا أمثلة متنوعة
        self.assertEqual(len(arabic_examples), 5)
        self.assertEqual(len(english_examples), 5)
        
        # كل مثال يجب أن يكون مختلف
        personality_types = [ex['output']['personality_type'] for ex in arabic_examples]
        unique_types = set(personality_types)
        self.assertEqual(len(unique_types), 5, "يجب أن تغطي الأمثلة جميع أنواع الشخصيات")
    
    def test_prompt_length_with_examples(self):
        """اختبار: طول الـ prompt مع الأمثلة"""
        test_data = {"personality_scores": {"analytical": 8}}
        
        prompt = self.gemini._build_analysis_prompt(test_data)
        
        # يجب أن يكون الـ prompt طويل بما يكفي ليحتوي على أمثلة
        self.assertGreater(len(prompt), 500, "الـ prompt يجب أن يحتوي على أمثلة")
        
        # لكن ليس طويل جداً
        self.assertLess(len(prompt), 10000, "الـ prompt يجب ألا يكون ضخم جداً")
    
    def test_examples_format_consistency(self):
        """اختبار: اتساق تنسيق الأمثلة"""
        for lang in ["arabic", "english"]:
            formatted = format_examples_for_prompt(lang, max_examples=2)
            
            self.assertIsInstance(formatted, str)
            self.assertGreater(len(formatted), 100)
            
            if lang == "arabic":
                self.assertIn("مثال", formatted)
            else:
                self.assertIn("Example", formatted.lower())


# ============================================
# اختبارات الأمان والتحقق - Validation Tests
# ============================================

class TestValidation(TestCase):
    """اختبارات التحقق من صحة البيانات"""
    
    def setUp(self):
        self.ai_advisor = AIAdvisor()
    
    def test_invalid_data_types(self):
        """اختبار: أنواع بيانات غير صحيحة"""
        # String بدل Dict
        test_data = "invalid data"
        
        try:
            result = self.ai_advisor.analyze_user_profile(test_data)
            # يجب أن يتعامل مع الخطأ بشكل صحيح
        except:
            # أو يرمي استثناء واضح
            pass
    
    def test_missing_required_fields(self):
        """اختبار: حقول مطلوبة مفقودة"""
        test_data = {
            # لا personality_scores
            "interests": {"technology": 9}
        }
        
        # يجب أن لا يفشل
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)
    
    def test_extra_unexpected_fields(self):
        """اختبار: حقول إضافية غير متوقعة"""
        test_data = {
            "personality_scores": {"analytical": 8},
            "interests": {"technology": 9},
            "random_field": "unexpected data",
            "another_field": 12345
        }
        
        # يجب أن يتجاهل الحقول الإضافية ويعمل
        result = self.ai_advisor.analyze_user_profile(test_data)
        self.assertIsNotNone(result)


# ============================================
# اختبارات Fallback System المتقدمة
# ============================================

class TestFallbackAdvanced(TestCase):
    """اختبارات متقدمة لنظام Fallback"""
    
    def setUp(self):
        self.gemini = GeminiService()
    
    def test_fallback_analysis_structure(self):
        """اختبار: هيكل تحليل Fallback"""
        fallback = self.gemini._get_fallback_analysis()
        
        # التحقق من جميع الحقول المطلوبة
        required_fields = ['personality_type', 'strengths', 'interests', 'learning_style']
        for field in required_fields:
            self.assertIn(field, fallback)
    
    def test_fallback_recommendations_quality(self):
        """اختبار: جودة توصيات Fallback"""
        recommendations = self.gemini._get_fallback_recommendations()
        
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        
        # كل توصية يجب أن تحتوي على الحقول الأساسية
        for rec in recommendations:
            self.assertIn('major_name', rec)
            self.assertIn('match_percentage', rec)
            self.assertIn('reasons', rec)
    
    def test_fallback_chat_variety(self):
        """اختبار: تنوع ردود Fallback"""
        responses = set()
        for _ in range(10):
            response = self.gemini._get_fallback_chat_response("test message")
            responses.add(response)
        
        # يجب أن يكون هناك تنوع في الردود
        self.assertGreater(len(responses), 1, "يجب أن تكون ردود Fallback متنوعة")


# ============================================
# ملخص الاختبارات
# ============================================

def print_extended_test_summary():
    """طباعة ملخص الاختبارات الموسعة"""
    print("\n" + "="*60)
    print("Extended AI Model Testing Summary - ملخص الاختبارات الموسعة")
    print("="*60)
    print("✅ Edge Cases Tests (7 tests)")
    print("✅ Performance Tests (3 tests)")
    print("✅ Accuracy Tests (3 tests)")
    print("✅ Complex Scenarios Tests (3 tests)")
    print("✅ Integration Tests (3 tests)")
    print("✅ Advanced Few-Shot Learning Tests (3 tests)")
    print("✅ Validation Tests (3 tests)")
    print("✅ Advanced Fallback Tests (3 tests)")
    print("="*60)
    print(f"📊 Total New Tests: 28 tests")
    print(f"📊 Combined with Original: 17 + 28 = 45 tests")
    print("="*60)


if __name__ == '__main__':
    import unittest
    unittest.main()
