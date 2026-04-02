from django.test import TestCase

# Create your tests here.
# tests/tests.py

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Question, Choice, TestResult, TestCategory
from majors.models import Major
from advisor.ai_service import AIAdvisor

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.test_category = TestCategory.objects.create(
            name='اختبار الميول',
            description='اختبار تجريبي'
        )
    
    def test_test_result_creation(self):
        result = TestResult.objects.create(
            user=self.user,
            test_category=self.test_category,
            score=85,
            result_summary='نوع الشخصية: تحليلي\nنقاط القوة: تحليل, تنظيم\nالاهتمامات: تكنولوجيا, علوم',
            recommended_majors='هندسة الحاسب, علوم الحاسب'
        )
        
        self.assertEqual(result.user.username, 'testuser')
        self.assertEqual(result.score, 85)
        self.assertTrue('هندسة الحاسب' in result.recommended_majors)

class TestAIService(TestCase):
    def setUp(self):
        self.ai_advisor = AIAdvisor()
        self.user_data = {
            'personality_scores': {
                'تحليلي': 8,
                'إبداعي': 5,
                'اجتماعي': 3,
                'تنظيمي': 7,
                'عملي': 6
            },
            'interests': {
                'العلوم': 9,
                'التكنولوجيا': 8,
                'الهندسة': 7,
                'الرياضيات': 6,
                'الطب': 4
            }
        }
    
    def test_analyze_user_profile(self):
        result = self.ai_advisor.analyze_user_profile(self.user_data)
        
        self.assertIn('personality_analysis', result)
        self.assertIn('interest_analysis', result)
        self.assertIn('recommendations', result)
        self.assertIn('suggested_skills', result)
        
        self.assertGreater(len(result['recommendations']), 0)
    
    def test_determine_personality_type(self):
        traits = [('تحليلي', 8), ('تنظيمي', 7)]
        personality_type = self.ai_advisor.determine_personality_type(traits)
        
        self.assertIsInstance(personality_type, str)
        self.assertGreater(len(personality_type), 0)

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advisor/home.html')
    
    def test_test_page_authenticated(self):
        response = self.client.get('/tests/')
        self.assertEqual(response.status_code, 200)
    
    def test_test_page_unauthenticated(self):
        self.client.logout()
        response = self.client.get('/tests/')
        self.assertEqual(response.status_code, 302)

class TestAPIEndpoints(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='apiuser',
            password='testpass123',
            email='api@test.com'
        )
        self.client.login(username='apiuser', password='testpass123')
    
    def test_majors_api(self):
        response = self.client.get('/api/majors/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_chat_api(self):
        data = {'message': 'ما هي أفضل التخصصات للبرمجة؟'}
        response = self.client.post(
            '/api/chat/',
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertTrue(json_response['success'])