-- استعلامات SQL لإضافة مستخدمين تجريبيين
-- يمكن تنفيذها مباشرة في MySQL

-- ملاحظة: Django يستخدم hashing لكلمات المرور
-- لذلك يفضل استخدام Django shell أو Admin panel لإنشاء المستخدمين
-- هذا الملف للمرجعية فقط

-- ===========================================
-- طريقة 1: استخدام Django Admin Panel
-- ===========================================
-- 1. افتح: http://127.0.0.1:8000/admin/
-- 2. سجل الدخول كـ superuser
-- 3. اذهب إلى Users
-- 4. أضف مستخدم جديد

-- ===========================================
-- طريقة 2: استخدام Django Shell (الموصى بها)
-- ===========================================
-- افتح PowerShell وشغل:
-- python manage.py shell

-- ثم نفذ الكود التالي:
/*
from django.contrib.auth.models import User

# حذف المستخدمين القدامى
User.objects.filter(username__in=['student', 'admin', 'test']).delete()

# إنشاء مستخدم طالب
student = User.objects.create_user(
    username='student',
    email='student@test.com',
    password='123456',
    first_name='محمد',
    last_name='أحمد'
)
print(f'✅ تم إنشاء: {student.username}')

# إنشاء مدير
admin = User.objects.create_superuser(
    username='admin',
    email='admin@test.com',
    password='admin123',
    first_name='المدير',
    last_name='العام'
)
print(f'✅ تم إنشاء: {admin.username}')

# إنشاء مستخدم تجريبي
test = User.objects.create_user(
    username='test',
    email='test@test.com',
    password='test123'
)
print(f'✅ تم إنشاء: {test.username}')

print('\n=== بيانات التسجيل ===')
print('student / 123456')
print('admin / admin123')
print('test / test123')
*/

-- ===========================================
-- طريقة 3: SQL مباشر (للمرجعية فقط - غير موصى به)
-- ===========================================
-- ⚠️ تحذير: كلمات المرور يجب أن تكون مشفرة بـ Django
-- هذه الطريقة لن تعمل مع Django authentication

-- مثال فقط (لن يعمل):
-- INSERT INTO auth_user (username, email, password, is_superuser, is_staff, is_active, date_joined)
-- VALUES 
--   ('student', 'student@test.com', 'pbkdf2_sha256$...', 0, 0, 1, NOW()),
--   ('admin', 'admin@test.com', 'pbkdf2_sha256$...', 1, 1, 1, NOW());

-- ===========================================
-- الخلاصة: استخدم Django Shell
-- ===========================================
-- الأمر الصحيح:
-- python manage.py shell
-- ثم الصق الكود Python أعلاه
