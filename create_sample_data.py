# create_sample_data.py

import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from accounts.models import Profile
from django.contrib.auth.models import User
from majors.models import MajorCategory, Major, Course, Book
from tests.models import QuestionCategory, Question, Choice

def create_sample_data():
    users = [
        {'username': 'student1', 'email': 'student1@example.com', 'password': 'testpass123'},
        {'username': 'student2', 'email': 'student2@example.com', 'password': 'testpass123'},
        {'username': 'student3', 'email': 'student3@example.com', 'password': 'testpass123'},
    ]
    
    for user_data in users:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            print(f"✅ تم إنشاء المستخدم: {user.username}")
    
    categories_data = [
        {
            'name': 'الهندسة والتكنولوجيا',
            'description': 'تخصصات في المجالات الهندسية والتقنية تشمل البرمجة والذكاء الاصطناعي والاتصالات'
        },
        {
            'name': 'العلوم الطبية',
            'description': 'تخصصات في المجال الطبي والصحي تشمل الطب والتمريض والصيدلة'
        },
        {
            'name': 'العلوم الإنسانية',
            'description': 'تخصصات في اللغات والأدب والفنون والعلوم الاجتماعية'
        },
        {
            'name': 'إدارة الأعمال',
            'description': 'تخصصات في الإدارة والاقتصاد والتجارة والتمويل'
        },
        {
            'name': 'العلوم الطبيعية',
            'description': 'تخصصات في الفيزياء والكيمياء والرياضيات والأحياء'
        },
    ]
    
    for cat_data in categories_data:
        category, created = MajorCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"✅ تم إنشاء فئة: {category.name}")
    
    engineering = MajorCategory.objects.get(name='الهندسة والتكنولوجيا')
    medical = MajorCategory.objects.get(name='العلوم الطبية')
    
    majors_data = [
        {
            'name': 'هندسة الحاسب الآلي',
            'category': engineering,
            'description': '''يهتم هذا التخصص بتصميم وتطوير الأنظمة الحاسوبية والبرمجيات. يشمل دراسة الخوارزميات، بنية الحاسوب، الشبكات، وقواعد البيانات. يعد من أكثر التخصصات طلباً في سوق العمل.''',
            'required_skills': 'القدرة على التحليل المنطقي، مهارات رياضية قوية، التفكير الإبداعي، مهارات حل المشكلات',
            'study_nature': 'مزيج من النظري والتطبيقي العملي مع مشاريع عملية وتدريب ميداني',
            'personality_types': 'تحليلي, تنظيمي, عملي, مبدع',
            'job_opportunities': 'مبرمج، مهندس برمجيات، محلل نظم، مدير قواعد بيانات، أخصائي أمن معلومات',
            'average_salary': '15,000 - 30,000 ريال',
            'universities': 'جامعة الملك سعود، جامعة الملك فهد للبترول والمعادن، جامعة الملك عبدالعزيز، جامعة الأميرة نورة'
        },
        {
            'name': 'الطب البشري',
            'category': medical,
            'description': '''يهتم بتشخيص وعلاج الأمراض والإصابات. يتطلب دراسة عميقة لجسم الإنسان وأجهزته. من أطول وأصعب التخصصات الجامعية.''',
            'required_skills': 'ذاكرة قوية، قدرة على العمل تحت الضغط، مهارات تواصل، تعاطف مع المرضى',
            'study_nature': 'دراسة نظرية مكثفة تليها تدريب عملي في المستشفيات',
            'personality_types': 'اجتماعي, تحليلي, عملي, منظم',
            'job_opportunities': 'طبيب عام، أخصائي، استشاري، باحث طبي',
            'average_salary': '30,000 - 60,000 ريال',
            'universities': 'جامعة الملك سعود، جامعة الملك عبدالعزيز، جامعة الإمام عبدالرحمن بن فيصل، جامعة طيبة'
        },
    ]
    
    for major_data in majors_data:
        major, created = Major.objects.get_or_create(
            name=major_data['name'],
            defaults=major_data
        )
        if created:
            print(f"✅ تم إنشاء تخصص: {major.name}")
    
    courses_data = [
        {
            'title': 'مقدمة في البرمجة',
            'description': 'دورة أساسية تقدم مفاهيم البرمجة الأساسية للمبتدئين',
            'url': 'https://example.com/course1',
            'category': 'تكنولوجيا'
        },
        {
            'title': 'كيف تختار تخصصك الجامعي',
            'description': 'دورة تساعد الطلاب على اتخاذ القرار الصحيح في اختيار التخصص',
            'url': 'https://example.com/course2',
            'category': 'توجيه مهني'
        },
    ]
    
    for course_data in courses_data:
        course, created = Course.objects.get_or_create(
            title=course_data['title'],
            defaults=course_data
        )
        if created:
            print(f"✅ تم إنشاء دورة: {course.title}")
    
    books_data = [
        {
            'title': 'دليل التخصصات الجامعية',
            'author': 'وزارة التعليم',
            'description': 'كتاب شامل عن جميع التخصصات الجامعية في المملكة',
            'category': 'توجيه'
        },
        {
            'title': 'اختر مسارك المهني',
            'author': 'أحمد محمد',
            'description': 'كتاب يساعد في اكتشاف الميول المهنية',
            'category': 'تطوير ذاتي'
        },
    ]
    
    for book_data in books_data:
        book, created = Book.objects.get_or_create(
            title=book_data['title'],
            defaults=book_data
        )
        if created:
            print(f"✅ تم إنشاء كتاب: {book.title}")
    
    print("\n🎉 تم إنشاء جميع البيانات العينة بنجاح!")

if __name__ == '__main__':
    create_sample_data()