import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(is_superuser=True).exists():
    print("📝 إنشاء حساب مدير...")
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@university.com',
        password='admin123'
    )
    print(f"✅ تم إنشاء حساب المدير بنجاح!")
    print(f"اسم المستخدم: admin")
    print(f"كلمة المرور: admin123")
    print(f"\n🔐 الرابط: http://127.0.0.1:8000/admin/")
else:
    admin = User.objects.filter(is_superuser=True).first()
    print(f"✅ حساب المدير موجود بالفعل: {admin.username}")
    print(f"🔐 الرابط: http://127.0.0.1:8000/admin/")
