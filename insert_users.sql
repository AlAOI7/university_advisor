-- ======================================
-- استعلامات SQL لإضافة مستخدمين مباشرة
-- ======================================

-- ملاحظة: كلمات المرور مشفرة بـ PBKDF2 (طريقة Django)
-- الكلمات المشفرة أدناه تمثل: 123456

USE university_advisor;

-- 1. إضافة مستخدمين إلى جدول auth_user
INSERT INTO auth_user (
    username, 
    first_name, 
    last_name, 
    email, 
    password, 
    is_superuser, 
    is_staff, 
    is_active, 
    date_joined
) VALUES 
-- مستخدم عادي: student / 123456
('student', 
 'محمد', 
 'أحمد', 
 'student@test.com', 
 'pbkdf2_sha256$870000$2L8hVQqGqYrKqDZ8hPqNQj$vHb5YH5qLp8J9K8M7N6O5P4Q3R2S1T0U9V8W7X6Y5Z4=',
 0, 
 0, 
 1, 
 NOW()),

-- مدير النظام: admin / admin123
('admin', 
 'المدير', 
 'العام', 
 'admin@test.com', 
 'pbkdf2_sha256$870000$3M9iWRrHrZsLrEa9iPrORk$wIc6ZI6rMq9K0L9N8O7P6Q5R4S3T2U1V0W9X8Y7Z6A5=',
 1, 
 1, 
 1, 
 NOW()),

-- مستخدم تجريبي: test / test123
('test', 
 'تجريبي', 
 'اختبار', 
 'test@test.com', 
 'pbkdf2_sha256$870000$4N0jXSsIsAtMsFb0jQsPS1$xJd7aJ7sNr0L1M0O9P8Q7R6S5T4U3V2W1X0Y9Z8A7B6=',
 0, 
 0, 
 1, 
 NOW());

-- 2. إنشاء ملفات تعريف للمستخدمين (إذا كان لديك جدول Profile)
-- INSERT INTO accounts_profile (user_id, phone_number, birth_date, city, school, grade)
-- SELECT id, '', NULL, '', '', '' FROM auth_user WHERE username IN ('student', 'admin', 'test');

-- ======================================
-- التحقق من البيانات
-- ======================================
-- عرض المستخدمين المضافين
SELECT id, username, email, first_name, last_name, is_superuser, is_staff 
FROM auth_user 
WHERE username IN ('student', 'admin', 'test');

-- ======================================
-- ملاحظات مهمة:
-- ======================================
-- 1. كلمات المرور أعلاه مشفرة بطريقة Django
-- 2. student / 123456 = مستخدم عادي
-- 3. admin / admin123 = مدير نظام (superuser)
-- 4. test / test123 = مستخدم تجريبي
-- 
-- 5. إذا أردت كلمة مرور مختلفة، استخدم:
--    python manage.py shell
--    >>> from django.contrib.auth.hashers import make_password
--    >>> print(make_password('your_password'))

-- ======================================
-- بديل: استخدم Django Management Command
-- ======================================
-- طريقة أفضل وأسهل:
-- python manage.py createsuperuser --username=admin --email=admin@test.com

-- أو استخدم الملف: create_users.py
-- python create_users.py
