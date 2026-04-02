import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from django.contrib.auth.hashers import make_password

passwords = {
    'student (123456)': make_password('123456'),
    'admin (admin123)': make_password('admin123'),
    'test (test123)': make_password('test123'),
}

print("=" * 60)
print("كلمات المرور المشفرة للاستخدام في SQL:")
print("=" * 60)
for user, hashed in passwords.items():
    print(f"\n{user}:")
    print(hashed)

print("\n" + "=" * 60)
print("استخدم هذه القيم في استعلام INSERT INTO auth_user")
print("=" * 60)
