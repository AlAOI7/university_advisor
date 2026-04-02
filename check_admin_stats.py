import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from majors.models import Course, Book
from tests.models import Question, Choice, QuestionCategory

print("=" * 60)
print("📊 إحصائيات لوحة التحكم")
print("=" * 60)

courses_count = Course.objects.count()
print(f"\n📚 الكورسات: {courses_count}")

books_count = Book.objects.count()
print(f"📖 الكتب: {books_count}")

categories_count = QuestionCategory.objects.count()
questions_count = Question.objects.count()
choices_count = Choice.objects.count()

print(f"\n❓ فئات الأسئلة: {categories_count}")
print(f"❓ الأسئلة: {questions_count}")
print(f"✅ الخيارات: {choices_count}")

if questions_count > 0:
    print(f"\n📝 آخر 5 أسئلة:")
    for q in Question.objects.all()[:5]:
        print(f"   - {q.text[:60]}...")

print("\n" + "=" * 60)
print("🔐 معلومات الدخول:")
print("=" * 60)
print("الرابط: http://127.0.0.1:8000/admin/")
print("المستخدم: admin")
print("كلمة المرور: admin123")
print("=" * 60)
