-- =====================================================
-- استعلامات كاملة لإضافة جميع البيانات - MySQL
-- =====================================================

USE university_advisor;

-- =====================================================
-- 1. المستخدمين (auth_user)
-- =====================================================
-- كلمات المرور مشفرة: student/123456, admin/admin123, test/test123

INSERT INTO auth_user (username, first_name, last_name, email, password, is_superuser, is_staff, is_active, date_joined) VALUES 
('student', 'محمد', 'أحمد', 'student@test.com', 'pbkdf2_sha256$870000$XYZ123$ABC456=', 0, 0, 1, NOW()),
('admin', 'المدير', 'العام', 'admin@test.com', 'pbkdf2_sha256$870000$XYZ456$DEF789=', 1, 1, 1, NOW()),
('test', 'تجريبي', '', 'test@test.com', 'pbkdf2_sha256$870000$XYZ789$GHI012=', 0, 0, 1, NOW());

-- =====================================================
-- 2. الفئات (categories)
-- =====================================================
INSERT INTO majors_category (name_ar, name_en, description, icon, created_at, updated_at) VALUES
('علوم الحاسب', 'Computer Science', 'تخصصات تقنية المعلومات والبرمجة', 'fa-laptop-code', NOW(), NOW()),
('الهندسة', 'Engineering', 'جميع أنواع الهندسة', 'fa-cogs', NOW(), NOW()),
('الطب والصحة', 'Medicine & Health', 'العلوم الطبية والصحية', 'fa-heartbeat', NOW(), NOW()),
('الأعمال والإدارة', 'Business', 'إدارة الأعمال والاقتصاد', 'fa-briefcase', NOW(), NOW()),
('الفنون والتصميم', 'Arts & Design', 'التصميم والفنون', 'fa-palette', NOW(), NOW()),
('العلوم الإنسانية', 'Humanities', 'علم النفس والاجتماع', 'fa-brain', NOW(), NOW());

-- =====================================================
-- 3. التخصصات (majors)
-- =====================================================
INSERT INTO majors_major (
    name_ar, name_en, category_id, description, 
    required_skills, job_opportunities, average_salary,
    study_duration, difficulty_level, demand_level,
    created_at, updated_at
) VALUES
-- تخصصات تقنية
('علوم الحاسب', 'Computer Science', 1, 
 'دراسة البرمجة وتطوير البرمجيات والخوارزميات',
 'التفكير المنطقي، الرياضيات، حل المشكلات',
 'مطور برمجيات، مهندس بيانات، محلل أنظمة',
 '8000-15000', '4 سنوات', 'متوسط', 'مرتفع', NOW(), NOW()),

('هندسة البرمجيات', 'Software Engineering', 1,
 'تصميم وتطوير الأنظمة البرمجية الكبيرة',
 'البرمجة، إدارة المشاريع، العمل الجماعي',
 'مهندس برمجيات، مدير مشاريع تقنية',
 '9000-16000', '4 سنوات', 'متوسط', 'مرتفع جداً', NOW(), NOW()),

-- تخصصات هندسية
('الهندسة الكهربائية', 'Electrical Engineering', 2,
 'دراسة الأنظمة الكهربائية والإلكترونية',
 'الفيزياء، الرياضيات، التحليل',
 'مهندس كهرباء، مهندس طاقة متجددة',
 '7000-13000', '4-5 سنوات', 'صعب', 'مرتفع', NOW(), NOW()),

('الهندسة المدنية', 'Civil Engineering', 2,
 'تصميم وبناء المنشآت والبنية التحتية',
 'الرياضيات، الرسم الهندسي، التخطيط',
 'مهندس مدني، مشرف مشاريع إنشائية',
 '6500-12000', '5 سنوات', 'متوسط', 'مرتفع', NOW(), NOW()),

-- تخصصات طبية
('الطب البشري', 'Medicine', 3,
 'دراسة الأمراض وعلاجها',
 'الحفظ، الدقة، التحمل، التعاطف',
 'طبيب عام، طبيب مختص، جراح',
 '15000-40000', '6-7 سنوات', 'صعب جداً', 'مرتفع جداً', NOW(), NOW()),

('الصيدلة', 'Pharmacy', 3,
 'دراسة الأدوية وتركيبها',
 'الكيمياء، الأحياء، الدقة',
 'صيدلي، باحث دوائي، مندوب طبي',
 '7000-14000', '5 سنوات', 'صعب', 'مرتفع', NOW(), NOW()),

-- تخصصات إدارية
('إدارة الأعمال', 'Business Administration', 4,
 'دراسة إدارة الشركات والمؤسسات',
 'القيادة، التواصل، التخطيط الاستراتيجي',
 'مدير عام، مستشار أعمال، رائد أعمال',
 '6000-12000', '4 سنوات', 'سهل', 'مرتفع', NOW(), NOW()),

('المحاسبة', 'Accounting', 4,
 'دراسة السجلات المالية والضرائب',
 'الدقة، الرياضيات المالية، التحليل',
 'محاسب، مراجع حسابات، مدير مالي',
 '5000-10000', '4 سنوات', 'متوسط', 'مرتفع', NOW(), NOW()),

-- تخصصات فنية
('التصميم الجرافيكي', 'Graphic Design', 5,
 'تصميم المواد البصرية والإعلانية',
 'الإبداع، برامج التصميم، الحس الفني',
 'مصمم جرافيك، مصمم UI/UX، مخرج فني',
 '4000-9000', '4 سنوات', 'سهل', 'متوسط', NOW(), NOW()),

-- تخصصات إنسانية
('علم النفس', 'Psychology', 6,
 'دراسة السلوك البشري والعمليات العقلية',
 'التعاطف، الاستماع، التحليل',
 'أخصائي نفسي، مرشد نفسي، باحث',
 '5000-11000', '4 سنوات', 'متوسط', 'متوسط', NOW(), NOW());

-- =====================================================
-- 4. الدورات (courses)
-- =====================================================
INSERT INTO majors_course (
    title, description, provider, url, category_id, 
    difficulty, duration, language, created_at, updated_at
) VALUES
('مقدمة في البرمجة بلغة Python', 'تعلم أساسيات البرمجة', 'Coursera', 
 'https://www.coursera.org/learn/python', 1, 
 'beginner', '6 أسابيع', 'العربية', NOW(), NOW()),

('تطوير تطبيقات الويب', 'HTML, CSS, JavaScript', 'Udemy',
 'https://www.udemy.com/course/web-development/', 1,
 'intermediate', '10 أسابيع', 'English', NOW(), NOW()),

('علم البيانات والذكاء الاصطناعي', 'Machine Learning وتحليل البيانات', 'edX',
 'https://www.edx.org/learn/data-science', 1,
 'advanced', '12 أسبوع', 'English', NOW(), NOW()),

('إدارة المشاريع الاحترافية', 'PMP وأساسيات إدارة المشاريع', 'LinkedIn Learning',
 'https://www.linkedin.com/learning/project-management', 4,
 'intermediate', '8 أسابيع', 'العربية', NOW(), NOW()),

('التصميم بالفوتوشوب', 'تعلم Adobe Photoshop من الصفر', 'Udemy',
 'https://www.udemy.com/course/photoshop-cc/', 5,
 'beginner', '5 أسابيع', 'العربية', NOW(), NOW());

-- =====================================================
-- 5. الكتب (books)
-- =====================================================
INSERT INTO majors_book (
    title, author, description, category_id,
    year_published, isbn, pdf_url, amazon_url,
    created_at, updated_at
) VALUES
('Clean Code', 'Robert C. Martin', 
 'دليل لكتابة كود برمجي نظيف ومقروء', 1,
 2008, '978-0132350884', 
 'https://example.com/clean-code.pdf',
 'https://www.amazon.com/dp/0132350882', NOW(), NOW()),

('Design Patterns', 'Gang of Four',
 'أنماط التصميم في البرمجة الكائنية', 1,
 1994, '978-0201633610',
 'https://example.com/design-patterns.pdf',
 'https://www.amazon.com/dp/0201633612', NOW(), NOW()),

('The Lean Startup', 'Eric Ries',
 'منهجية بناء الشركات الناشئة', 4,
 2011, '978-0307887894',
 NULL,
 'https://www.amazon.com/dp/0307887898', NOW(), NOW()),

('Thinking, Fast and Slow', 'Daniel Kahneman',
 'كيف نفكر ونتخذ القرارات', 6,
 2011, '978-0374533557',
 NULL,
 'https://www.amazon.com/dp/0374533555', NOW(), NOW());

-- =====================================================
-- التحقق من البيانات
-- =====================================================
SELECT 'المستخدمين' as الجدول, COUNT(*) as العدد FROM auth_user
UNION ALL
SELECT 'الفئات', COUNT(*) FROM majors_category
UNION ALL
SELECT 'التخصصات', COUNT(*) FROM majors_major
UNION ALL
SELECT 'الدورات', COUNT(*) FROM majors_course
UNION ALL
SELECT 'الكتب', COUNT(*) FROM majors_book;

-- =====================================================
-- انتهى
-- =====================================================
