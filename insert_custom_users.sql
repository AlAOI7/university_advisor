-- =====================================================
-- استعلامات إضافة بيانات لجدول users المخصص
-- =====================================================

USE university_advisor;

-- =====================================================
-- 1. إضافة مستخدمين إلى جدول users
-- =====================================================

-- كلمات المرور مشفرة بـ bcrypt أو يمكن استخدام MD5/SHA256
-- هنا سنستخدم MD5 كمثال بسيط (في الإنتاج استخدم bcrypt)

INSERT INTO users (
    id,
    username, 
    email, 
    password, 
    full_name, 
    date_of_birth, 
    gender, 
    phone,
    created_at,
    updated_at
) VALUES 
-- مستخدم 1: student / 123456
(1,
 'student', 
 'student@test.com', 
 MD5('123456'),  -- أو استخدم: '$2y$10$...' للـ bcrypt
 'محمد أحمد عبدالله',
 '2005-05-15',
 'male',
 '0501234567',
 NOW(),
 NOW()),

-- مستخدم 2: admin / admin123
(2,
 'admin', 
 'admin@test.com', 
 MD5('admin123'),
 'المدير العام',
 '1990-01-01',
 'male',
 '0550000000',
 NOW(),
 NOW()),

-- مستخدم 3: test / test123
(3,
 'test', 
 'test@test.com', 
 MD5('test123'),
 'مستخدم تجريبي',
 '2000-06-20',
 'female',
 '0559876543',
 NOW(),
 NOW()),

-- مستخدم 4: ahmed / 123456
(4,
 'ahmed',
 'ahmed@example.com',
 MD5('123456'),
 'أحمد محمود',
 '2004-03-10',
 'male',
 '0551112233',
 NOW(),
 NOW()),

-- مستخدم 5: sara / 123456
(5,
 'sara',
 'sara@example.com',
 MD5('123456'),
 'سارة علي',
 '2005-08-22',
 'female',
 '0554445566',
 NOW(),
 NOW());

-- =====================================================
-- 2. إضافة نتائج اختبار لبعض المستخدمين
-- =====================================================

INSERT INTO user_results (
    id,
    user_id,
    personality_type,
    strengths_summary,
    interests_summary,
    ai_analysis,
    test_score,
    completed_at
) VALUES
-- نتيجة للمستخدم student
(1,
 1,  -- user_id للـ student
 'محلل منطقي',
 'التفكير التحليلي، حل المشكلات، الرياضيات',
 'البرمجة، التكنولوجيا، العلوم',
 '{"learning_style": "بصري وعملي", "work_environment": "مكتب تقني", "recommendations": ["علوم الحاسب", "هندسة البرمجيات", "الذكاء الاصطناعي"]}',
 85,
 NOW()),

-- نتيجة للمستخدم ahmed
(2,
 4,  -- user_id للـ ahmed
 'مبدع فني',
 'الإبداع، التصميم، التفكير خارج الصندوق',
 'الفنون، التصميم، الميديا',
 '{"learning_style": "بصري وإبداعي", "work_environment": "استوديو إبداعي", "recommendations": ["التصميم الجرافيكي", "العمارة", "الإعلام"]}',
 78,
 NOW()),

-- نتيجة للمستخدم sara  
(3,
 5,  -- user_id للـ sara
 'اجتماعية متعاونة',
 'التواصل، مساعدة الآخرين، العمل الجماعي',
 'التعليم، الصحة، الخدمة الاجتماعية',
 '{"learning_style": "سمعي وتفاعلي", "work_environment": "بيئة اجتماعية", "recommendations": ["علم النفس", "التربية", "الخدمة الاجتماعية"]}',
 92,
 NOW());

-- =====================================================
-- 3. التحقق من البيانات المضافة
-- =====================================================

-- عرض جميع المستخدمين
SELECT id, username, email, full_name, gender, phone 
FROM users 
ORDER BY id;

-- عرض نتائج الاختبارات
SELECT 
    ur.id,
    u.username,
    u.full_name,
    ur.personality_type,
    ur.test_score,
    ur.completed_at
FROM user_results ur
JOIN users u ON ur.user_id = u.id
ORDER BY ur.id;

-- إحصائيات
SELECT 
    'إجمالي المستخدمين' as البيان, 
    COUNT(*) as العدد 
FROM users
UNION ALL
SELECT 
    'مستخدمين أكملوا الاختبار', 
    COUNT(DISTINCT user_id) 
FROM user_results;

-- =====================================================
-- ملاحظات مهمة
-- =====================================================

-- 1. بيانات تسجيل الدخول:
--    student / 123456
--    admin / admin123
--    test / test123
--    ahmed / 123456
--    sara / 123456

-- 2. كلمات المرور مشفرة بـ MD5 (للتبسيط)
--    في الإنتاج، استخدم bcrypt أو Argon2

-- 3. للحصول على hash bcrypt في Python:
--    import bcrypt
--    password = "123456"
--    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
--    print(hashed.decode())

-- 4. بيانات JSON في ai_analysis يمكن توسيعها:
--    - إضافة المزيد من التوصيات
--    - تفاصيل نقاط القوة
--    - مسار وظيفي مقترح

-- =====================================================
-- استعلامات إضافية مفيدة
-- =====================================================

-- حذف جميع البيانات (للبدء من جديد)
-- DELETE FROM user_results;
-- DELETE FROM users;
-- ALTER TABLE users AUTO_INCREMENT = 1;
-- ALTER TABLE user_results AUTO_INCREMENT = 1;

-- تحديث كلمة مرور لمستخدم معين
-- UPDATE users SET password = MD5('new_password') WHERE username = 'student';

-- إضافة مستخدم جديد بسرعة
-- INSERT INTO users (username, email, password, full_name, created_at, updated_at)
-- VALUES ('new_user', 'new@test.com', MD5('password123'), 'اسم المستخدم', NOW(), NOW());
