# create_initial_data.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from majors.models import MajorCategory, Major, Course, Book
from tests.models import QuestionCategory, Question, Choice

def create_initial_data():
    categories = [
        {'name': 'الهندسة والتكنولوجيا', 'description': 'تخصصات في المجالات الهندسية والتقنية'},
        {'name': 'العلوم الطبية', 'description': 'تخصصات في المجال الطبي والصحي'},
        {'name': 'العلوم الإنسانية', 'description': 'تخصصات في اللغات والأدب والفنون'},
        {'name': 'إدارة الأعمال', 'description': 'تخصصات في الإدارة والاقتصاد والتجارة'},
        {'name': 'العلوم الطبيعية', 'description': 'تخصصات في الفيزياء والكيمياء والرياضيات'},
    ]
    
    for cat_data in categories:
        MajorCategory.objects.get_or_create(**cat_data)
    
    question_categories = [
        {'name': 'الميول الأكاديمية', 'description': 'المواد الدراسية المفضلة'},
        {'name': 'المهارات الشخصية', 'description': 'نقاط القوة والمهارات'},
        {'name': 'الاهتمامات', 'description': 'الهوايات والاهتمامات الشخصية'},
    ]
    
    for qc_data in question_categories:
        QuestionCategory.objects.get_or_create(**qc_data)
    
    print("✅ تم إنشاء البيانات الأولية بنجاح!")

if __name__ == '__main__':
    create_initial_data()