import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from django.contrib.auth.models import User

User.objects.filter(username__in=['student', 'admin', 'test']).delete()

student = User.objects.create_user(
    username='student',
    email='student@test.com',
    password='123456',
    first_name='محمد',
    last_name='أحمد'
)
print(f'✅ مستخدم: {student.username} / 123456')

admin = User.objects.create_superuser(
    username='admin',
    email='admin@test.com',
    password='admin123',
    first_name='المدير',
    last_name='العام'
)
print(f'✅ مدير: {admin.username} / admin123')

test = User.objects.create_user(
    username='test',
    email='test@test.com',
    password='test123'
)
print(f'✅ تجريبي: {test.username} / test123')

print('\n🎉 تم إنشاء 3 مستخدمين بنجاح!')
print('=' * 40)
print('بيانات التسجيل:')
print('  student / 123456')
print('  admin / admin123')
print('  test / test123')
print('=' * 40)
