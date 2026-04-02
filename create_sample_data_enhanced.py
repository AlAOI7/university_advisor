# create_sample_data_enhanced.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from majors.models import MajorCategory, Major, Course, Book

def create_sample_data():
    print("🔄 جاري إنشاء البيانات...")
    
    engineering = MajorCategory.objects.get_or_create(
        name='الهندسة والتكنولوجيا',
        defaults={'description': 'تخصصات في المجالات الهندسية والتقنية', 'icon': 'fas fa-cogs'}
    )[0]
    
    medical = MajorCategory.objects.get_or_create(
        name='العلوم الطبية',
        defaults={'description': 'تخصصات في المجال الطبي والصحي', 'icon': 'fas fa-heartbeat'}
    )[0]
    
    humanities = MajorCategory.objects.get_or_create(
        name='العلوم الإنسانية',
        defaults={'description': 'تخصصات في اللغات والأدب والفنون', 'icon': 'fas fa-book'}
    )[0]
    
    business = MajorCategory.objects.get_or_create(
        name='إدارة الأعمال',
        defaults={'description': 'تخصصات في الإدارة والاقتصاد والتجارة', 'icon': 'fas fa-briefcase'}
    )[0]
    
    sciences = MajorCategory.objects.get_or_create(
        name='العلوم الطبيعية',
        defaults={'description': 'تخصصات في الفيزياء والكيمياء والرياضيات', 'icon': 'fas fa-flask'}
    )[0]
    
    cs = Major.objects.get_or_create(
        name='علوم الحاسب',
        category=engineering,
        defaults={
            'description': 'يركز هذا التخصص على علوم الحاسوب النظرية والبرمجة والذكاء الاصطناعي وتطوير الأنظمة.',
            'duration': '4 سنوات',
            'requirements': 'مهارات رياضية قوية، تفكير منطقي، القدرة على حل المشكلات',
            'job_opportunities': 'مهندس برمجيات، مطور تطبيقات، محلل بيانات، مهندس ذكاء اصطناعي، مدير مشاريع تقنية',
            'average_salary': '15,000 - 30,000 ريال',
            'demand_level': 'عالي جداً',
            'level': 'bachelor',
            'universities': 'جامعة الملك سعود، جامعة الملك عبدالعزيز، جامعة الملك فهد للبترول والمعادن'
        }
    )[0]
    
    it = Major.objects.get_or_create(
        name='تقنية المعلومات',
        category=engineering,
        defaults={
            'description': 'يركز على إدارة وتطبيق التقنيات الحاسوبية في بيئات الأعمال.',
            'duration': '4 سنوات',
            'requirements': 'معرفة بالحاسوب، القدرة على التعلم المستمر، مهارات التواصل',
            'job_opportunities': 'مدير أنظمة، أخصائي أمن سيبراني، مسؤول قواعد بيانات، محلل أنظمة',
            'average_salary': '12,000 - 25,000 ريال',
            'demand_level': 'عالي',
            'level': 'bachelor',
            'universities': 'جامعة الأمير سلطان، جامعة الملك سعود، جامعة الإمام عبدالرحمن'
        }
    )[0]
    
    medicine = Major.objects.get_or_create(
        name='الطب البشري',
        category=medical,
        defaults={
            'description': 'تخصص يعنى بدراسة جسم الإنسان وتشخيص وعلاج الأمراض.',
            'duration': '6-7 سنوات',
            'requirements': 'معدل عالٍ جداً، تفوق في العلوم، القدرة على التحمل النفسي',
            'job_opportunities': 'طبيب عام، أخصائي، استشاري، باحث طبي',
            'average_salary': '20,000 - 50,000 ريال',
            'demand_level': 'عالي جداً',
            'level': 'bachelor',
            'universities': 'جامعة الملك سعود، جامعة الملك عبدالعزيز، جامعة الملك فيصل'
        }
    )[0]
    
    management = Major.objects.get_or_create(
        name='إدارة الأعمال',
        category=business,
        defaults={
            'description': 'يركز على مهارات الإدارة والقيادة والتخطيط الاستراتيجي.',
            'duration': '4 سنوات',
            'requirements': 'مهارات القيادة، التفكير التحليلي، مهارات التواصل',
            'job_opportunities': 'مدير مشروع، مستشار إداري، محلل أعمال، مدير موارد بشرية',
            'average_salary': '10,000 - 25,000 ريال',
            'demand_level': 'عالي',
            'level': 'bachelor',
            'universities': 'جامعة الملك سعود، جامعة الملك عبدالعزيز، جامعة الأمير سلطان'
        }
    )[0]
    
    print("✅ تم إنشاء التخصصات")
    
    Course.objects.get_or_create(
        title='مقدمة في البرمجة - Python',
        major=cs,
        defaults={
            'description': 'دورة شاملة لتعلم أساسيات البرمجة باستخدام لغة Python من الصفر',
            'url': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc',
            'platform': 'YouTube - Programming with Mosh',
            'duration': '6 ساعات',
            'price': 0,
            'type': 'free',
            'language': 'إنجليزي',
            'rating': 4.8
        }
    )
    
    Course.objects.get_or_create(
        title='تطوير تطبيقات الويب Full Stack',
        major=cs,
        defaults={
            'description': 'تعلم تطوير تطبيقات الويب الكاملة باستخدام HTML, CSS, JavaScript, Node.js',
            'url': 'https://www.coursera.org/specializations/full-stack-react',
            'platform': 'Coursera',
            'duration': '4 أشهر',
            'price': 0,
            'type': 'free',
            'language': 'إنجليزي',
            'rating': 4.7
        }
    )
    
    Course.objects.get_or_create(
        title='الذكاء الاصطناعي والتعلم الآلي - بالعربي',
        major=cs,
        defaults={
            'description': 'دورة متقدمة في الذكاء الاصطناعي والتعلم الآلي باللغة العربية',
            'url': 'https://www.udemy.com/course/ai-machine-learning-arabic',
            'platform': 'Udemy',
            'duration': '20 ساعة',
            'price': 199,
            'type': 'paid',
            'language': 'العربية',
            'rating': 4.6
        }
    )
    
    Course.objects.get_or_create(
        title='أساسيات الأمن السيبراني',
        major=it,
        defaults={
            'description': 'تعرف على أساسيات  الأمن السيبراني وحماية الأنظمة',
            'url': 'https://www.edx.org/course/introduction-to-cybersecurity',
            'platform': 'edX',
            'duration': '6 أسابيع',
            'price': 0,
            'type': 'free',
            'language': 'إنجليزي',
            'rating': 4.5
        }
    )
    
    print("✅ تم إضافة الدورات")
    
    Book.objects.get_or_create(
        title='Python Crash Course',
        major=cs,
        defaults={
            'author': 'Eric Matthes',
            'description': 'دليل عملي شامل لتعلم البرمجة بلغة Python',
            'download_url': 'https://github.com/topics/python-crash-course',
            'pages': 544,
            'format': 'pdf'
        }
    )
    
    Book.objects.get_or_create(
        title='Clean Code',
        major=cs,
        defaults={
            'author': 'Robert C. Martin',
            'description': 'دليل لكتابة كود برمجي نظيف وقابل للصيانة',
            'download_url': 'https://github.com/topics/clean-code',
            'pages': 464,
            'format': 'pdf'
        }
    )
    
    Book.objects.get_or_create(
        title='Introduction to Algorithms',
        major=cs,
        defaults={
            'author': 'Thomas H. Cormen',
            'description': 'كتاب شامل في الخوارزميات وهياكل البيانات',
            'download_url': 'https://github.com/topics/introduction-to-algorithms',
            'pages': 1312,
            'format': 'pdf'
        }
    )
    
    Book.objects.get_or_create(
        title='The Lean Startup',
        major=management,
        defaults={
            'author': 'Eric Ries',
            'description': 'منهجية جديدة لإنشاء وإدارة الشركات الناشئة',
            'download_url': 'https://github.com/topics/lean-startup',
            'pages': 336,
            'format': 'pdf'
        }
    )
    
    print("✅ تم إضافة الكتب")
    
    print("\n📊 الإحصائيات:")
    print(f"   - عدد فئات التخصصات: {MajorCategory.objects.count()}")
    print(f"   - عدد التخصصات: {Major.objects.count()}")
    print(f"   - عدد الدورات: {Course.objects.count()}")
    print(f"   - عدد الكتب: {Book.objects.count()}")
    print("\n✅ تم إنشاء جميع البيانات بنجاح!")

if __name__ == '__main__':
    create_sample_data()
