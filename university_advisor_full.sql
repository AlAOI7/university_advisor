-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 31 يناير 2026 الساعة 11:40
-- إصدار الخادم: 10.4.32-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `university_advisor`
--

-- إنشاء قاعدة البيانات
CREATE DATABASE IF NOT EXISTS `university_advisor` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `university_advisor`;

-- --------------------------------------------------------

--
-- بنية الجدول `answers`
--

CREATE TABLE `answers` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `answer` text NOT NULL,
  `score` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `author` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `pdf_url` varchar(255) DEFAULT NULL,
  `amazon_url` varchar(255) DEFAULT NULL,
  `year_published` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text DEFAULT NULL,
  `provider` varchar(100) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `difficulty` enum('beginner','intermediate','advanced') DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `majors`
--

CREATE TABLE `majors` (
  `id` int(11) NOT NULL,
  `name_ar` varchar(100) NOT NULL,
  `name_en` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `required_skills` text DEFAULT NULL,
  `career_opportunities` text DEFAULT NULL,
  `difficulty_level` enum('low','medium','high') DEFAULT NULL,
  `demand_level` enum('low','medium','high') DEFAULT NULL,
  `salary_range` varchar(50) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- إرجاع أو استيراد بيانات الجدول `majors`
--

INSERT INTO `majors` (`id`, `name_ar`, `name_en`, `description`, `required_skills`, `career_opportunities`, `difficulty_level`, `demand_level`, `salary_range`, `image_url`, `created_at`) VALUES
(1, 'هندسة الحاسوب', 'Computer Engineering', 'يجمع بين الهندسة الكهربائية وعلوم الحاسوب', 'التحليل المنطقي, البرمجة, الرياضيات', 'مهندس برمجيات, مهندس أنظمة, مطور تطبيقات', 'high', 'high', '15000-35000 ريال', NULL, NOW()),
(2, 'الطب البشري', 'Medicine', 'دراسة جسم الإنسان وتشخيص وعلاج الأمراض', 'الصبر, الدقة, التعاطف, الذاكرة القوية', 'طبيب عام, أخصائي, استشاري, باحث طبي', 'high', 'high', '20000-50000 ريال', NULL, NOW()),
(3, 'العلوم السياسية', 'Political Science', 'دراسة النظم السياسية والعلاقات الدولية', 'التحليل, التواصل, البحث, الكتابة', 'محلل سياسي, دبلوماسي, باحث, صحفي', 'medium', 'medium', '8000-18000 ريال', NULL, NOW()),
(4, 'إدارة الأعمال', 'Business Administration', 'دراسة مبادئ الإدارة والتخطيط الاستراتيجي', 'القيادة, التنظيم, التواصل, التحليل المالي', 'مدير مشروع, مستشار إداري, محلل أعمال', 'medium', 'high', '10000-25000 ريال', NULL, NOW()),
(5, 'علوم الحاسب', 'Computer Science', 'دراسة نظرية الحاسوب والبرمجة والذكاء الاصطناعي', 'البرمجة, الرياضيات, حل المشكلات, التفكير المنطقي', 'مبرمج, محلل بيانات, مهندس AI, مطور ويب', 'high', 'high', '12000-30000 ريال', NULL, NOW()),
(6, 'الهندسة الكهربائية', 'Electrical Engineering', 'دراسة الكهرباء والإلكترونيات والطاقة', 'الرياضيات, الفيزياء, التحليل, التصميم', 'مهندس كهرباء, مهندس طاقة, مهندس إلكترونيات', 'high', 'high', '14000-32000 ريال', NULL, NOW()),
(7, 'التصميم الجرافيكي', 'Graphic Design', 'فن التواصل البصري والتصميم الإبداعي', 'الإبداع, التذوق الفني, البرامج التقنية, التواصل', 'مصمم جرافيك, مصمم واجهات, مصمم هوية بصرية', 'low', 'medium', '6000-15000 ريال', NULL, NOW()),
(8, 'الهندسة المعمارية', 'Architecture', 'تصميم وتخطيط المباني والمساحات', 'الإبداع, الرسم, الرياضيات, الهندسة, التخطيط', 'مهندس معماري, مخطط عمراني, مصمم داخلي', 'high', 'medium', '12000-28000 ريال', NULL, NOW()),
(9, 'علم النفس', 'Psychology', 'دراسة السلوك البشري والعمليات العقلية', 'الاستماع, التعاطف, التحليل, البحث العلمي', 'أخصائي نفسي, مستشار, باحث, معالج', 'medium', 'medium', '8000-20000 ريال', NULL, NOW()),
(10, 'الهندسة الميكانيكية', 'Mechanical Engineering', 'تصميم وتحليل الأنظمة الميكانيكية', 'الرياضيات, الفيزياء, التصميم, حل المشكلات', 'مهندس ميكانيكي, مهندس تصنيع, مهندس صيانة', 'high', 'high', '13000-30000 ريال', NULL, NOW());

-- --------------------------------------------------------

--
-- بنية الجدول `major_questions`
--

CREATE TABLE `major_questions` (
  `id` int(11) NOT NULL,
  `major_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `preferred_answer` text DEFAULT NULL,
  `importance_level` enum('low','medium','high') DEFAULT 'medium'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `question_text` text NOT NULL,
  `question_type` enum('strength','interest','subject','skill','personality') NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `options` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`options`)),
  `weight` decimal(3,2) DEFAULT 1.00,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- إرجاع أو استيراد بيانات الجدول `questions`
--

INSERT INTO `questions` (`id`, `question_text`, `question_type`, `category`, `options`, `weight`, `created_at`) VALUES
(1, 'ما هي المواد الدراسية التي تفضلها؟', 'subject', 'academic', '[\"الرياضيات\", \"الفيزياء\", \"الكيمياء\", \"الأحياء\", \"اللغة العربية\", \"اللغة الإنجليزية\", \"التاريخ\", \"الجغرافيا\"]', 1.00, NOW()),
(2, 'ما هي المهارات التي تتمتع بها؟', 'skill', 'personal', '[\"التحليل المنطقي\", \"الإبداع\", \"التواصل\", \"القيادة\", \"العمل الجماعي\", \"حل المشكلات\", \"التنظيم\", \"الاستماع\"]', 1.00, NOW()),
(3, 'ماذا تفضل في وقت فراغك؟', 'interest', 'hobbies', '[\"القراءة\", \"الرسم\", \"البرمجة\", \"الرياضة\", \"التعليم\", \"مساعدة الآخرين\", \"الاكتشاف\", \"التصميم\"]', 1.00, NOW()),
(4, 'في أي بيئة تفضل العمل؟', 'personality', 'work_environment', '[\"المكتب التقليدي\", \"العمل الميداني\", \"المختبرات\", \"العمل عن بعد\", \"ورش العمل\", \"البيئة الإبداعية\"]', 1.00, NOW()),
(5, 'ما هي نقاط قوتك الرئيسية؟', 'strength', 'personal', '[\"التفكير التحليلي\", \"الإبداع والابتكار\", \"مهارات التواصل\", \"القدرة على التعلم السريع\", \"الصبر والتحمل\", \"القيادة\"]', 1.20, NOW()),
(6, 'أي من هذه الأنشطة تستمتع بها؟', 'interest', 'activities', '[\"حل الألغاز والمسائل\", \"التصميم والفن\", \"الكتابة والقراءة\", \"التجارب العملية\", \"التفاعل الاجتماعي\", \"الألعاب الاستراتيجية\"]', 1.00, NOW()),
(7, 'كيف تفضل حل المشكلات؟', 'skill', 'problem_solving', '[\"التحليل المنطقي والأرقام\", \"الإبداع والحلول غير التقليدية\", \"البحث والقراءة\", \"التجربة العملية\", \"النقاش مع الآخرين\"]', 1.10, NOW()),
(8, 'ما مستوى اهتمامك بالتكنولوجيا؟', 'interest', 'technology', '[\"مهتم جداً ومتابع للجديد\", \"مهتم ومستخدم نشط\", \"استخدام عادي\", \"اهتمام محدود\", \"غير مهتم\"]', 1.00, NOW()),
(9, 'ما هو أسلوب التعلم المفضل لديك؟', 'personality', 'learning_style', '[\"التعلم النظري والقراءة\", \"التطبيق العملي والتجريب\", \"الشرح المرئي والفيديو\", \"المناقشة والحوار\", \"التعلم الذاتي\"]', 1.00, NOW()),
(10, 'ما مدى استعدادك للتعامل مع الضغوطات؟', 'strength', 'stress_management', '[\"قادر على التعامل مع ضغوط عالية\", \"أتعامل جيداً مع الضغوط المتوسطة\", \"أفضل بيئة عمل هادئة\", \"أفضل العمل بدون ضغوط\"]', 0.90, NOW()),
(11, 'ما مدى اهتمامك بمساعدة الآخرين؟', 'interest', 'social', '[\"مهم جداً بالنسبة لي\", \"مهم ولكن ليس الأولوية\", \"اهتمام متوسط\", \"ليس من أولوياتي\"]', 1.00, NOW()),
(12, 'هل تفضل العمل الفردي أم الجماعي؟', 'personality', 'work_style', '[\"العمل الفردي تماماً\", \"أفضل الفردي مع تعاون محدود\", \"مزيج متوازن\", \"أفضل الجماعي مع استقلالية\", \"العمل الجماعي تماماً\"]', 1.00, NOW()),
(13, 'ما مستوى قدرتك على التحدث أمام الجمهور؟', 'skill', 'public_speaking', '[\"ممتاز وأستمتع به\", \"جيد وأستطيع القيام به\", \"مقبول مع بعض التوتر\", \"صعب بالنسبة لي\"]', 0.80, NOW()),
(14, 'كم تستطيع قضاء الوقت في القراءة والدراسة؟', 'personality', 'study_habits', '[\"أكثر من 4 ساعات يومياً بارتياح\", \"2-4 ساعات يومياً\", \"1-2 ساعة يومياً\", \"أقل من ساعة\"]', 1.00, NOW()),
(15, 'ما مدى اهتمامك بالتفاصيل الدقيقة؟', 'skill', 'attention_to_detail', '[\"أهتم كثيراً بأدق التفاصيل\", \"أهتم بالتفاصيل المهمة\", \"أركز على الصورة الكبرى\", \"التفاصيل ليست أولويتي\"]', 1.00, NOW());

-- البيانات للدورات
INSERT INTO `courses` (`title`, `description`, `provider`, `url`, `duration`, `difficulty`, `category`) VALUES
('مقدمة في البرمجة - Python', 'دورة شاملة لتعلم أساسيات البرمجة', 'Coursera', 'https://www.coursera.org/learn/python', '4 أسابيع', 'beginner', 'Computer Science'),
('تطوير تطبيقات الويب', 'تعلم HTML, CSS, JavaScript', 'Udemy', 'https://www.udemy.com/web-development', '8 أسابيع', 'intermediate', 'Computer Science'),
('الذكاء الاصطناعي والتعلم الآلي', 'مقدمة شاملة للـ AI و ML', 'edX', 'https://www.edx.org/course/ai-ml', '12 أسبوع', 'advanced', 'Computer Science'),
('إدارة المشاريع الاحترافية', 'أساسيات إدارة المشاريع', 'LinkedIn Learning', 'https://www.linkedin.com/learning', '6 أسابيع', 'intermediate', 'Business'),
('التصميم الجرافيكي للمبتدئين', 'تعلم Adobe Photoshop & Illustrator', 'Udemy', 'https://www.udemy.com/graphic-design', '5 أسابيع', 'beginner', 'Design'),
('أساسيات علم النفس', 'مقدمة في علم النفس', 'Coursera', 'https://www.coursera.org/learn/psychology', '8 أسابيع', 'beginner', 'Psychology'),
('الهندسة الكهربائية الأساسية', 'مبادئ الكهرباء والإلكترونيات', 'MIT OpenCourseWare', 'https://ocw.mit.edu', '10 أسابيع', 'intermediate', 'Engineering'),
('التسويق الرقمي', 'استراتيجيات التسويق الحديثة', 'Google Digital Garage', 'https://learndigital.withgoogle.com', '4 أسابيع', 'beginner', 'Business'),
('تصميم المباني بـ AutoCAD', 'تعلم الرسم المعماري', 'Udemy', 'https://www.udemy.com/autocad-course', '7 أسابيع', 'intermediate', 'Architecture'),
('الفيزياء الجامعية', 'فيزياء متقدمة', 'Khan Academy', 'https://www.khanacademy.org/physics', '16 أسبوع', 'advanced', 'Science');

-- البيانات للكتب
INSERT INTO `books` (`title`, `author`, `description`, `category`, `pdf_url`, `year_published`) VALUES
('Python Crash Course', 'Eric Matthes', 'دليل عملي شامل لتعلم Python', 'Computer Science', 'https://github.com/topics/python', 2019),
('Clean Code', 'Robert C. Martin', 'كتابة كود برمجي نظيف', 'Computer Science', 'https://github.com/topics/clean-code', 2008),
('Introduction to Algorithms', 'Thomas H. Cormen', 'كتاب شامل عن الخوارزميات', 'Computer Science', 'https://mitpress.mit.edu', 2009),
('The Lean Startup', 'Eric Ries', 'منهجية Startup الحديثة', 'Business', 'https://theleanstartup.com', 2011),
('Thinking, Fast and Slow', 'Daniel Kahneman', 'علم النفس المعرفي', 'Psychology', 'https://www.amazon.com', 2011),
('The Design of Everyday Things', 'Don Norman', 'مبادئ التصميم', 'Design', 'https://www.nngroup.com', 1988),
('Fundamentals of Electric Circuits', 'Charles Alexander', 'أساسيات الدوائر الكهربائية', 'Engineering', 'https://www.mheducation.com', 2016),
('Principles of Marketing', 'Philip Kotler', 'مبادئ التسويق', 'Business', 'https://www.pearson.com', 2017),
('Building Construction Handbook', 'Roy Chudley', 'دليل البناء والتشييد', 'Architecture', 'https://www.routledge.com', 2016),
('University Physics', 'Hugh D. Young', 'فيزياء جامعية شاملة', 'Science', 'https://www.pearson.com', 2019);

-- --------------------------------------------------------

--
-- بنية الجدول `recommendations`
--

CREATE TABLE `recommendations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `major_id` int(11) NOT NULL,
  `match_percentage` decimal(5,2) NOT NULL,
  `reasoning` text DEFAULT NULL,
  `is_accepted` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` enum('male','female','other') DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `user_results`
--

CREATE TABLE `user_results` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `personality_type` varchar(50) DEFAULT NULL,
  `strengths_summary` text DEFAULT NULL,
  `interests_summary` text DEFAULT NULL,
  `ai_analysis` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`ai_analysis`)),
  `test_score` int(11) DEFAULT NULL,
  `completed_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `question_id` (`question_id`);

ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `majors`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `major_questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `major_id` (`major_id`),
  ADD KEY `question_id` (`question_id`);

ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `recommendations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `major_id` (`major_id`);

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

ALTER TABLE `user_results`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

ALTER TABLE `answers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `majors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `major_questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `recommendations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `user_results`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- قيود الجداول
--

ALTER TABLE `answers`
  ADD CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `answers_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`) ON DELETE CASCADE;

ALTER TABLE `major_questions`
  ADD CONSTRAINT `major_questions_ibfk_1` FOREIGN KEY (`major_id`) REFERENCES `majors` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `major_questions_ibfk_2` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`) ON DELETE CASCADE;

ALTER TABLE `recommendations`
  ADD CONSTRAINT `recommendations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `recommendations_ibfk_2` FOREIGN KEY (`major_id`) REFERENCES `majors` (`id`) ON DELETE CASCADE;

ALTER TABLE `user_results`
  ADD CONSTRAINT `user_results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
