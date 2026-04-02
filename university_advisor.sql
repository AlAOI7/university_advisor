-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 31 مارس 2026 الساعة 09:05
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

-- --------------------------------------------------------

--
-- بنية الجدول `accounts_notification`
--

CREATE TABLE `accounts_notification` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `accounts_profile`
--

CREATE TABLE `accounts_profile` (
  `id` bigint(20) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `city` varchar(100) NOT NULL,
  `school` varchar(200) NOT NULL,
  `grade` varchar(50) NOT NULL,
  `personality_type` varchar(50) NOT NULL,
  `strengths` longtext NOT NULL,
  `interests` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `phone_number`, `birth_date`, `city`, `school`, `grade`, `personality_type`, `strengths`, `interests`, `created_at`, `updated_at`, `user_id`) VALUES
(1, '', NULL, '', '', '', '', '', '', '2026-03-31 06:34:43.747780', '2026-03-31 07:01:19.878712', 1),
(2, '', NULL, '', '', '', '', '', '', '2026-03-31 06:56:13.895104', '2026-03-31 06:56:13.897862', 2),
(3, '', NULL, '', '', '', '', '', '', '2026-03-31 06:56:15.783190', '2026-03-31 06:56:15.787591', 3),
(4, '', NULL, '', '', '', '', '', '', '2026-03-31 06:56:17.284343', '2026-03-31 06:56:17.288780', 4),
(5, '', NULL, '', '', '', '', '', '', '2026-03-31 06:56:18.974292', '2026-03-31 06:56:18.978023', 5);

-- --------------------------------------------------------

--
-- بنية الجدول `accounts_userprofile`
--

CREATE TABLE `accounts_userprofile` (
  `id` bigint(20) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `address` longtext DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `high_school_gpa` decimal(4,2) DEFAULT NULL,
  `interests` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `accounts_userprofile`
--

INSERT INTO `accounts_userprofile` (`id`, `phone`, `address`, `birth_date`, `high_school_gpa`, `interests`, `created_at`, `updated_at`, `user_id`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, '2026-03-31 06:34:43.753251', '2026-03-31 07:01:19.883194', 1),
(2, NULL, NULL, NULL, NULL, NULL, '2026-03-31 06:56:13.909565', '2026-03-31 06:56:13.914420', 2),
(3, NULL, NULL, NULL, NULL, NULL, '2026-03-31 06:56:15.791900', '2026-03-31 06:56:15.795679', 3),
(4, NULL, NULL, NULL, NULL, NULL, '2026-03-31 06:56:17.293760', '2026-03-31 06:56:17.297452', 4),
(5, NULL, NULL, NULL, NULL, NULL, '2026-03-31 06:56:18.982974', '2026-03-31 06:56:18.986349', 5);

-- --------------------------------------------------------

--
-- بنية الجدول `advisor_aiconversation`
--

CREATE TABLE `advisor_aiconversation` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `advisor_aimessage`
--

CREATE TABLE `advisor_aimessage` (
  `id` bigint(20) NOT NULL,
  `role` varchar(10) NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `conversation_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `advisor_contactmessage`
--

CREATE TABLE `advisor_contactmessage` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `status` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `advisor_faq`
--

CREATE TABLE `advisor_faq` (
  `id` bigint(20) NOT NULL,
  `question` varchar(500) NOT NULL,
  `answer` longtext NOT NULL,
  `category` varchar(100) NOT NULL,
  `order` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `advisor_university`
--

CREATE TABLE `advisor_university` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `website` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `ranking` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- بنية الجدول `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add notification', 7, 'add_notification'),
(26, 'Can change notification', 7, 'change_notification'),
(27, 'Can delete notification', 7, 'delete_notification'),
(28, 'Can view notification', 7, 'view_notification'),
(29, 'Can add profile', 8, 'add_profile'),
(30, 'Can change profile', 8, 'change_profile'),
(31, 'Can delete profile', 8, 'delete_profile'),
(32, 'Can view profile', 8, 'view_profile'),
(33, 'Can add user profile', 9, 'add_userprofile'),
(34, 'Can change user profile', 9, 'change_userprofile'),
(35, 'Can delete user profile', 9, 'delete_userprofile'),
(36, 'Can view user profile', 9, 'view_userprofile'),
(37, 'Can add contact message', 10, 'add_contactmessage'),
(38, 'Can change contact message', 10, 'change_contactmessage'),
(39, 'Can delete contact message', 10, 'delete_contactmessage'),
(40, 'Can view contact message', 10, 'view_contactmessage'),
(41, 'Can add faq', 11, 'add_faq'),
(42, 'Can change faq', 11, 'change_faq'),
(43, 'Can delete faq', 11, 'delete_faq'),
(44, 'Can view faq', 11, 'view_faq'),
(45, 'Can add university', 12, 'add_university'),
(46, 'Can change university', 12, 'change_university'),
(47, 'Can delete university', 12, 'delete_university'),
(48, 'Can view university', 12, 'view_university'),
(49, 'Can add ai conversation', 13, 'add_aiconversation'),
(50, 'Can change ai conversation', 13, 'change_aiconversation'),
(51, 'Can delete ai conversation', 13, 'delete_aiconversation'),
(52, 'Can view ai conversation', 13, 'view_aiconversation'),
(53, 'Can add ai message', 14, 'add_aimessage'),
(54, 'Can change ai message', 14, 'change_aimessage'),
(55, 'Can delete ai message', 14, 'delete_aimessage'),
(56, 'Can view ai message', 14, 'view_aimessage'),
(57, 'Can add major', 15, 'add_major'),
(58, 'Can change major', 15, 'change_major'),
(59, 'Can delete major', 15, 'delete_major'),
(60, 'Can view major', 15, 'view_major'),
(61, 'Can add Major Category', 16, 'add_majorcategory'),
(62, 'Can change Major Category', 16, 'change_majorcategory'),
(63, 'Can delete Major Category', 16, 'delete_majorcategory'),
(64, 'Can view Major Category', 16, 'view_majorcategory'),
(65, 'Can add course', 17, 'add_course'),
(66, 'Can change course', 17, 'change_course'),
(67, 'Can delete course', 17, 'delete_course'),
(68, 'Can view course', 17, 'view_course'),
(69, 'Can add book', 18, 'add_book'),
(70, 'Can change book', 18, 'change_book'),
(71, 'Can delete book', 18, 'delete_book'),
(72, 'Can view book', 18, 'view_book'),
(73, 'Can add user recommendation', 19, 'add_userrecommendation'),
(74, 'Can change user recommendation', 19, 'change_userrecommendation'),
(75, 'Can delete user recommendation', 19, 'delete_userrecommendation'),
(76, 'Can view user recommendation', 19, 'view_userrecommendation'),
(77, 'Can add major review', 20, 'add_majorreview'),
(78, 'Can change major review', 20, 'change_majorreview'),
(79, 'Can delete major review', 20, 'delete_majorreview'),
(80, 'Can view major review', 20, 'view_majorreview'),
(81, 'Can add question', 21, 'add_question'),
(82, 'Can change question', 21, 'change_question'),
(83, 'Can delete question', 21, 'delete_question'),
(84, 'Can view question', 21, 'view_question'),
(85, 'Can add question category', 22, 'add_questioncategory'),
(86, 'Can change question category', 22, 'change_questioncategory'),
(87, 'Can delete question category', 22, 'delete_questioncategory'),
(88, 'Can view question category', 22, 'view_questioncategory'),
(89, 'Can add Test Category', 23, 'add_testcategory'),
(90, 'Can change Test Category', 23, 'change_testcategory'),
(91, 'Can delete Test Category', 23, 'delete_testcategory'),
(92, 'Can view Test Category', 23, 'view_testcategory'),
(93, 'Can add choice', 24, 'add_choice'),
(94, 'Can change choice', 24, 'change_choice'),
(95, 'Can delete choice', 24, 'delete_choice'),
(96, 'Can view choice', 24, 'view_choice'),
(97, 'Can add test question', 25, 'add_testquestion'),
(98, 'Can change test question', 25, 'change_testquestion'),
(99, 'Can delete test question', 25, 'delete_testquestion'),
(100, 'Can view test question', 25, 'view_testquestion'),
(101, 'Can add test result', 26, 'add_testresult'),
(102, 'Can change test result', 26, 'change_testresult'),
(103, 'Can delete test result', 26, 'delete_testresult'),
(104, 'Can view test result', 26, 'view_testresult'),
(105, 'Can add user answer', 27, 'add_useranswer'),
(106, 'Can change user answer', 27, 'change_useranswer'),
(107, 'Can delete user answer', 27, 'delete_useranswer'),
(108, 'Can view user answer', 27, 'view_useranswer');

-- --------------------------------------------------------

--
-- بنية الجدول `auth_user`
--
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$QTeDxFopwGT7NLdpoNAg5P$HCNVvXcDffT8wOfVyuV7BkjXKRLnZZw8MBvQGt6SJUw=', '2026-03-31 07:42:13.421115', 1, 'admin', '', '', 'dotnetala@gmail.com', 1, 1, '2026-03-31 06:34:41.999631'),
(2, 'pbkdf2_sha256$1000000$AMxEq7sdDTGsTBSwS1nOYQ$ngO5dMI9JZDkl5olfjwv658fdt0PENTC1kFMECvWDtw=', NULL, 0, 'student', 'محمد', 'أحمد عبدالله', 'student@test.com', 0, 1, '2026-03-31 06:56:12.285726'),
(3, 'pbkdf2_sha256$1000000$D8ZCFLZDqkH4Gb3mNYTuJz$KQbxmLjPn/UzNMoBP1UHZLnoUE+bByASrnkq4VVIIOU=', NULL, 0, 'test', 'مستخدم', 'تجريبي', 'test@test.com', 0, 1, '2026-03-31 06:56:13.930924'),
(4, 'pbkdf2_sha256$1000000$nfmsa8Wqi69ezQrffLCf0w$sE9/aj0pe/bgPPxBnjwI3nsqwCpr67vkO4mkUqiHaEk=', NULL, 0, 'ahmed', 'أحمد', 'محمود', 'ahmed@example.com', 0, 1, '2026-03-31 06:56:15.801303'),
(5, 'pbkdf2_sha256$1000000$UCksUNK8yxte167rWzuiY3$XG+6fSb1xmvgJJskut3Kw8FU6b4cQgaEQXBJsBXudY4=', NULL, 0, 'sara', 'سارة', 'علي', 'sara@example.com', 0, 1, '2026-03-31 06:56:17.303501'),
(9, 'pbkdf2_sha256$1000000$4cNyBF9O7voiYarCY8DM3J$b6/7g2lFOAIR9r7TpCRayl8MhHpE4a628/oJMhmEE+M=', '2026-03-31 07:16:17.136854', 1, 'superadmin', 'Super', 'Admin', 'dotnetala@gmail.com', 1, 1, '2026-03-31 10:11:17.000000');

-- --------------------------------------------------------

--
-- بنية الجدول `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

--
-- إرجاع أو استيراد بيانات الجدول `books`
--
INSERT INTO `books` (`id`, `title`, `author`, `description`, `category`, `pdf_url`, `amazon_url`, `year_published`, `created_at`) VALUES
(1, 'Python Crash Course', 'Eric Matthes', 'Comprehensive practical guide to learning Python', 'Computer Science', 'https://github.com/topics/python', NULL, 2019, '2026-01-31 10:52:52'),
(2, 'Clean Code', 'Robert C. Martin', 'Writing clean and maintainable code', 'Computer Science', 'https://github.com/topics/clean-code', NULL, 2008, '2026-01-31 10:52:52'),
(3, 'Introduction to Algorithms', 'Thomas H. Cormen', 'Comprehensive book on algorithms and data structures', 'Computer Science', 'https://mitpress.mit.edu', NULL, 2009, '2026-01-31 10:52:52'),
(4, 'The Lean Startup', 'Eric Ries', 'Modern startup methodology for launching projects', 'Business', 'https://theleanstartup.com', NULL, 2011, '2026-01-31 10:52:52'),
(5, 'Thinking, Fast and Slow', 'Daniel Kahneman', 'Cognitive psychology and decision making', 'Psychology', 'https://www.amazon.com', NULL, 2011, '2026-01-31 10:52:52'),
(6, 'The Design of Everyday Things', 'Don Norman', 'Principles of good product design', 'Design', 'https://www.nngroup.com', NULL, 1988, '2026-01-31 10:52:52'),
(7, 'Fundamentals of Electric Circuits', 'Charles Alexander', 'Fundamentals of electric circuits', 'Engineering', 'https://www.mheducation.com', NULL, 2016, '2026-01-31 10:52:52'),
(8, 'Principles of Marketing', 'Philip Kotler', 'Modern marketing principles', 'Business', 'https://www.pearson.com', NULL, 2017, '2026-01-31 10:52:52'),
(9, 'Building Construction Handbook', 'Roy Chudley', 'Comprehensive building and construction guide', 'Architecture', 'https://www.routledge.com', NULL, 2016, '2026-01-31 10:52:52'),
(10, 'University Physics', 'Hugh D. Young', 'Comprehensive university physics', 'Science', 'https://www.pearson.com', NULL, 2019, '2026-01-31 10:52:52'),
(11, 'Python Crash Course', 'Eric Matthes', 'Comprehensive practical guide to learning Python', 'Computer Science', 'https://github.com/topics/python', NULL, 2019, '2026-01-31 10:55:12'),
(12, 'Clean Code', 'Robert C. Martin', 'Writing clean and maintainable code', 'Computer Science', 'https://github.com/topics/clean-code', NULL, 2008, '2026-01-31 10:55:12'),
(13, 'Introduction to Algorithms', 'Thomas H. Cormen', 'Comprehensive book on algorithms and data structures', 'Computer Science', 'https://mitpress.mit.edu', NULL, 2009, '2026-01-31 10:55:12'),
(14, 'The Lean Startup', 'Eric Ries', 'Modern startup methodology for launching projects', 'Business', 'https://theleanstartup.com', NULL, 2011, '2026-01-31 10:55:12'),
(15, 'Thinking, Fast and Slow', 'Daniel Kahneman', 'Cognitive psychology and decision making', 'Psychology', 'https://www.amazon.com', NULL, 2011, '2026-01-31 10:55:12'),
(16, 'The Design of Everyday Things', 'Don Norman', 'Principles of good product design', 'Design', 'https://www.nngroup.com', NULL, 1988, '2026-01-31 10:55:12'),
(17, 'Fundamentals of Electric Circuits', 'Charles Alexander', 'Fundamentals of electric circuits', 'Engineering', 'https://www.mheducation.com', NULL, 2016, '2026-01-31 10:55:12'),
(18, 'Principles of Marketing', 'Philip Kotler', 'Modern marketing principles', 'Business', 'https://www.pearson.com', NULL, 2017, '2026-01-31 10:55:12'),
(19, 'Building Construction Handbook', 'Roy Chudley', 'Comprehensive building and construction guide', 'Architecture', 'https://www.routledge.com', NULL, 2016, '2026-01-31 10:55:12'),
(20, 'University Physics', 'Hugh D. Young', 'Comprehensive university physics', 'Science', 'https://www.pearson.com', NULL, 2019, '2026-01-31 10:55:12'),
(21, 'Python Crash Course', 'Eric Matthes', 'Comprehensive practical guide to learning Python programming', 'Computer Science', 'https://github.com/topics/python', NULL, 2019, '2026-02-01 07:05:29'),
(22, 'Clean Code', 'Robert C. Martin', 'Writing clean and maintainable code', 'Computer Science', 'https://github.com/topics/clean-code', NULL, 2008, '2026-02-01 07:05:29'),
(23, 'Introduction to Algorithms', 'Thomas H. Cormen', 'Comprehensive book on algorithms and data structures', 'Computer Science', 'https://mitpress.mit.edu', NULL, 2009, '2026-02-01 07:05:29'),
(24, 'The Lean Startup', 'Eric Ries', 'Modern startup methodology for launching projects', 'Business', 'https://theleanstartup.com', NULL, 2011, '2026-02-01 07:05:29'),
(25, 'Thinking, Fast and Slow', 'Daniel Kahneman', 'Cognitive psychology and decision making', 'Psychology', 'https://www.amazon.com', NULL, 2011, '2026-02-01 07:05:29'),
(26, 'The Design of Everyday Things', 'Don Norman', 'Principles of good product design', 'Design', 'https://www.nngroup.com', NULL, 1988, '2026-02-01 07:05:29'),
(27, 'Fundamentals of Electric Circuits', 'Charles Alexander', 'Fundamentals of electric circuits', 'Engineering', 'https://www.mheducation.com', NULL, 2016, '2026-02-01 07:05:29'),
(28, 'Principles of Marketing', 'Philip Kotler', 'Modern marketing principles', 'Business', 'https://www.pearson.com', NULL, 2017, '2026-02-01 07:05:29'),
(29, 'Building Construction Handbook', 'Roy Chudley', 'Comprehensive building and construction guide', 'Architecture', 'https://www.routledge.com', NULL, 2016, '2026-02-01 07:05:29'),
(30, 'University Physics', 'Hugh D. Young', 'Comprehensive and advanced university physics', 'Science', 'https://www.pearson.com', NULL, 2019, '2026-02-01 07:05:29'),
(31, 'Artificial Intelligence: A Modern Approach', 'Stuart Russell', 'Comprehensive reference on artificial intelligence', 'Computer Science', 'https://aima.cs.berkeley.edu', NULL, 2020, '2026-02-01 07:05:29'),
(32, 'Accounting Principles', 'Jerry Weygandt', 'Principles of financial accounting', 'Business', 'https://www.wiley.com', NULL, 2018, '2026-02-01 07:05:29'),
(33, 'Gray\'s Anatomy', 'Henry Gray', 'The most famous medical reference in anatomy', 'Medicine', 'https://www.elsevier.com', NULL, 2021, '2026-02-01 07:05:29'),
(34, 'Introduction to Psychology', 'James Kalat', 'Comprehensive introduction to psychology', 'Psychology', 'https://www.cengage.com', NULL, 2017, '2026-02-01 07:05:29'),
(35, 'The Art of Electronics', 'Paul Horowitz', 'Practical art of electronics', 'Engineering', 'https://artofelectronics.net', NULL, 2015, '2026-02-01 07:05:29');
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

--
-- إرجاع أو استيراد بيانات الجدول `courses`
--
INSERT INTO `courses` (`id`, `title`, `description`, `provider`, `url`, `duration`, `difficulty`, `category`, `created_at`) VALUES
(1, 'Introduction to Programming - Python', 'Comprehensive course to learn programming basics', 'Coursera', 'https://www.coursera.org/learn/python', '4 weeks', 'beginner', 'Computer Science', '2026-01-31 10:52:52'),
(2, 'Web Application Development', 'Learn HTML, CSS, JavaScript', 'Udemy', 'https://www.udemy.com/web-development', '8 weeks', 'intermediate', 'Computer Science', '2026-01-31 10:52:52'),
(3, 'Artificial Intelligence and Machine Learning', 'Comprehensive introduction to AI and ML', 'edX', 'https://www.edx.org/course/ai-ml', '12 weeks', 'advanced', 'Computer Science', '2026-01-31 10:52:52'),
(4, 'Professional Project Management', 'Project management fundamentals', 'LinkedIn Learning', 'https://www.linkedin.com/learning', '6 weeks', 'intermediate', 'Business', '2026-01-31 10:52:52'),
(5, 'Graphic Design for Beginners', 'Learn Adobe Photoshop & Illustrator', 'Udemy', 'https://www.udemy.com/graphic-design', '5 weeks', 'beginner', 'Design', '2026-01-31 10:52:52'),
(6, 'Psychology Basics', 'Introduction to psychology', 'Coursera', 'https://www.coursera.org/learn/psychology', '8 weeks', 'beginner', 'Psychology', '2026-01-31 10:52:52'),
(7, 'Basic Electrical Engineering', 'Principles of electricity and electronics', 'MIT OpenCourseWare', 'https://ocw.mit.edu', '10 weeks', 'intermediate', 'Engineering', '2026-01-31 10:52:52'),
(8, 'Digital Marketing', 'Modern marketing strategies', 'Google Digital Garage', 'https://learndigital.withgoogle.com', '4 weeks', 'beginner', 'Business', '2026-01-31 10:52:52'),
(9, 'Building Design with AutoCAD', 'Learn architectural drawing', 'Udemy', 'https://www.udemy.com/autocad-course', '7 weeks', 'intermediate', 'Architecture', '2026-01-31 10:52:52'),
(10, 'University Physics', 'Advanced physics', 'Khan Academy', 'https://www.khanacademy.org/physics', '16 weeks', 'advanced', 'Science', '2026-01-31 10:52:52'),
(11, 'Introduction to Programming - Python', 'Comprehensive course to learn programming basics using Python from scratch', 'Coursera', 'https://www.coursera.org/learn/python', '4 weeks', 'beginner', 'Computer Science', '2026-01-31 10:55:12'),
(12, 'Web Application Development', 'Learn HTML, CSS, JavaScript', 'Udemy', 'https://www.udemy.com/web-development', '8 weeks', 'intermediate', 'Computer Science', '2026-01-31 10:55:12'),
(13, 'Artificial Intelligence and Machine Learning', 'Comprehensive introduction to AI and ML', 'edX', 'https://www.edx.org/course/ai-ml', '12 weeks', 'advanced', 'Computer Science', '2026-01-31 10:55:12'),
(14, 'Professional Project Management', 'Project management fundamentals', 'LinkedIn Learning', 'https://www.linkedin.com/learning', '6 weeks', 'intermediate', 'Business', '2026-01-31 10:55:12'),
(15, 'Graphic Design for Beginners', 'Learn Adobe Photoshop & Illustrator', 'Udemy', 'https://www.udemy.com/graphic-design', '5 weeks', 'beginner', 'Design', '2026-01-31 10:55:12'),
(16, 'Psychology Basics', 'Introduction to psychology', 'Coursera', 'https://www.coursera.org/learn/psychology', '8 weeks', 'beginner', 'Psychology', '2026-01-31 10:55:12'),
(17, 'Basic Electrical Engineering', 'Principles of electricity and electronics', 'MIT OpenCourseWare', 'https://ocw.mit.edu', '10 weeks', 'intermediate', 'Engineering', '2026-01-31 10:55:12'),
(18, 'Digital Marketing', 'Modern marketing strategies', 'Google Digital Garage', 'https://learndigital.withgoogle.com', '4 weeks', 'beginner', 'Business', '2026-01-31 10:55:12'),
(19, 'Building Design with AutoCAD', 'Learn architectural drawing', 'Udemy', 'https://www.udemy.com/autocad-course', '7 weeks', 'intermediate', 'Architecture', '2026-01-31 10:55:12'),
(20, 'University Physics', 'Advanced physics', 'Khan Academy', 'https://www.khanacademy.org/physics', '16 weeks', 'advanced', 'Science', '2026-01-31 10:55:12'),
(21, 'Introduction to Programming - Python', 'Comprehensive course to learn programming basics using Python from scratch', 'Coursera', 'https://www.coursera.org/learn/python', '4 weeks', 'beginner', 'Computer Science', '2026-02-01 07:05:29'),
(22, 'Full Stack Web Application Development', 'Learn full stack web development using HTML, CSS, JavaScript, Node.js', 'Udemy', 'https://www.udemy.com/web-development', '8 weeks', 'intermediate', 'Computer Science', '2026-02-01 07:05:29'),
(23, 'Artificial Intelligence and Machine Learning', 'Comprehensive introduction to AI and ML using Python', 'edX', 'https://www.edx.org/course/ai-ml', '12 weeks', 'advanced', 'Computer Science', '2026-02-01 07:05:29'),
(24, 'Professional Project Management', 'Project management fundamentals and Agile & Scrum methodology', 'LinkedIn Learning', 'https://www.linkedin.com/learning', '6 weeks', 'intermediate', 'Business', '2026-02-01 07:05:29'),
(25, 'Graphic Design for Beginners', 'Learn Adobe Photoshop and Illustrator from scratch', 'Udemy', 'https://www.udemy.com/graphic-design', '5 weeks', 'beginner', 'Design', '2026-02-01 07:05:29'),
(26, 'Psychology Basics', 'Comprehensive introduction to psychology and human behavior', 'Coursera', 'https://www.coursera.org/learn/psychology', '8 weeks', 'beginner', 'Psychology', '2026-02-01 07:05:29'),
(27, 'Basic Electrical Engineering', 'Principles of electricity and electronics for beginners', 'MIT OpenCourseWare', 'https://ocw.mit.edu', '10 weeks', 'intermediate', 'Engineering', '2026-02-01 07:05:29'),
(28, 'Modern Digital Marketing', 'Digital marketing and social media strategies', 'Google Digital Garage', 'https://learndigital.withgoogle.com', '4 weeks', 'beginner', 'Business', '2026-02-01 07:05:29'),
(29, 'Building Design with AutoCAD', 'Learn engineering architectural drawing using AutoCAD', 'Udemy', 'https://www.udemy.com/autocad-course', '7 weeks', 'intermediate', 'Architecture', '2026-02-01 07:05:29'),
(30, 'Advanced University Physics', 'Advanced physics for university students', 'Khan Academy', 'https://www.khanacademy.org/physics', '16 weeks', 'advanced', 'Science', '2026-02-01 07:05:29'),
(31, 'Mobile App Development', 'Learn iOS and Android app development', 'Udacity', 'https://www.udacity.com/mobile', '10 weeks', 'intermediate', 'Computer Science', '2026-02-01 07:05:29'),
(32, 'Financial Accounting', 'Basics of accounting and financial statements', 'Coursera', 'https://www.coursera.org/accounting', '6 weeks', 'beginner', 'Business', '2026-02-01 07:05:29'),
(33, 'Cybersecurity', 'Protecting systems and networks from attacks', 'Cybrary', 'https://www.cybrary.it', '8 weeks', 'intermediate', 'IT', '2026-02-01 07:05:29'),
(34, 'Statistical Analysis', 'Learn statistics and data analysis', 'DataCamp', 'https://www.datacamp.com', '5 weeks', 'intermediate', 'Science', '2026-02-01 07:05:29'),
(35, 'UI/UX Design', 'Principles of user experience design', 'Interaction Design Foundation', 'https://www.interaction-design.org', '6 weeks', 'intermediate', 'Design', '2026-02-01 07:05:29');
-- --------------------------------------------------------

--
-- بنية الجدول `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'notification'),
(8, 'accounts', 'profile'),
(9, 'accounts', 'userprofile'),
(1, 'admin', 'logentry'),
(13, 'advisor', 'aiconversation'),
(14, 'advisor', 'aimessage'),
(10, 'advisor', 'contactmessage'),
(11, 'advisor', 'faq'),
(12, 'advisor', 'university'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(18, 'majors', 'book'),
(17, 'majors', 'course'),
(15, 'majors', 'major'),
(16, 'majors', 'majorcategory'),
(20, 'majors', 'majorreview'),
(19, 'majors', 'userrecommendation'),
(6, 'sessions', 'session'),
(24, 'tests', 'choice'),
(21, 'tests', 'question'),
(22, 'tests', 'questioncategory'),
(23, 'tests', 'testcategory'),
(25, 'tests', 'testquestion'),
(26, 'tests', 'testresult'),
(27, 'tests', 'useranswer');

-- --------------------------------------------------------

--
-- بنية الجدول `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-03-31 06:33:04.386134'),
(2, 'auth', '0001_initial', '2026-03-31 06:33:05.103445'),
(3, 'accounts', '0001_initial', '2026-03-31 06:33:05.423174'),
(4, 'admin', '0001_initial', '2026-03-31 06:33:05.610500'),
(5, 'admin', '0002_logentry_remove_auto_add', '2026-03-31 06:33:05.635701'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2026-03-31 06:33:05.661809'),
(7, 'advisor', '0001_initial', '2026-03-31 06:33:05.974160'),
(8, 'contenttypes', '0002_remove_content_type_name', '2026-03-31 06:33:06.072982'),
(9, 'auth', '0002_alter_permission_name_max_length', '2026-03-31 06:33:06.209361'),
(10, 'auth', '0003_alter_user_email_max_length', '2026-03-31 06:33:06.243710'),
(11, 'auth', '0004_alter_user_username_opts', '2026-03-31 06:33:06.268910'),
(12, 'auth', '0005_alter_user_last_login_null', '2026-03-31 06:33:06.343520'),
(13, 'auth', '0006_require_contenttypes_0002', '2026-03-31 06:33:06.349163'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2026-03-31 06:33:06.372647'),
(15, 'auth', '0008_alter_user_username_max_length', '2026-03-31 06:33:06.410681'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2026-03-31 06:33:06.466295'),
(17, 'auth', '0010_alter_group_name_max_length', '2026-03-31 06:33:06.505648'),
(18, 'auth', '0011_update_proxy_permissions', '2026-03-31 06:33:06.535342'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2026-03-31 06:33:06.567899'),
(20, 'majors', '0001_initial', '2026-03-31 06:33:07.377760'),
(21, 'sessions', '0001_initial', '2026-03-31 06:33:07.431417'),
(22, 'tests', '0001_initial', '2026-03-31 06:33:08.205000'),
(23, 'tests', '0002_alter_choice_options_alter_question_options_and_more', '2026-03-31 06:33:10.193976'),
(24, 'advisor', '0002_alter_aimessage_role_alter_contactmessage_status', '2026-03-31 06:37:25.708535'),
(25, 'majors', '0002_alter_course_language_alter_course_type_and_more', '2026-03-31 06:37:25.753921'),
(26, 'tests', '0003_alter_choice_personality_traits', '2026-03-31 06:37:25.762922');

-- --------------------------------------------------------

--
-- بنية الجدول `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `majors`
--
-- --------------------------------------------------------
-- Host: localhost
-- Generation Time: Mar 31, 2026
-- Table structure for table `majors`
-- --------------------------------------------------------

CREATE TABLE IF NOT EXISTS `majors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ar` varchar(100) NOT NULL,
  `name_en` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `required_skills` text DEFAULT NULL,
  `career_opportunities` text DEFAULT NULL,
  `difficulty_level` enum('low','medium','high') DEFAULT NULL,
  `demand_level` enum('low','medium','high') DEFAULT NULL,
  `salary_range` varchar(50) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `majors` (all text converted to English)
--

INSERT INTO `majors` (`id`, `name_ar`, `name_en`, `description`, `required_skills`, `career_opportunities`, `difficulty_level`, `demand_level`, `salary_range`, `image_url`, `created_at`) VALUES
(1, 'هندسة الحاسوب', 'Computer Engineering', 'Combines electrical engineering and computer science', 'Logical analysis, programming, mathematics', 'Software engineer, systems engineer, application developer', 'high', 'high', '15000-35000 SAR', NULL, '2026-01-31 10:52:52'),
(2, 'الطب البشري', 'Medicine', 'Study of the human body, diagnosis and treatment of diseases', 'Patience, precision, empathy, strong memory', 'General physician, specialist, consultant, medical researcher', 'high', 'high', '20000-50000 SAR', NULL, '2026-01-31 10:52:52'),
(3, 'العلوم السياسية', 'Political Science', 'Study of political systems and international relations', 'Analysis, communication, research, writing', 'Political analyst, diplomat, researcher, journalist', 'medium', 'medium', '8000-18000 SAR', NULL, '2026-01-31 10:52:52'),
(4, 'إدارة الأعمال', 'Business Administration', 'Study of management principles and strategic planning', 'Leadership, organization, communication, financial analysis', 'Project manager, administrative consultant, business analyst', 'medium', 'high', '10000-25000 SAR', NULL, '2026-01-31 10:52:52'),
(5, 'علوم الحاسب', 'Computer Science', 'Study of computer theory, programming, and artificial intelligence', 'Programming, mathematics, problem solving, logical thinking', 'Programmer, data analyst, AI engineer, web developer', 'high', 'high', '12000-30000 SAR', NULL, '2026-01-31 10:52:52'),
(6, 'الهندسة الكهربائية', 'Electrical Engineering', 'Study of electricity, electronics, and energy', 'Mathematics, physics, analysis, design', 'Electrical engineer, power engineer, electronics engineer', 'high', 'high', '14000-32000 SAR', NULL, '2026-01-31 10:52:52'),
(7, 'التصميم الجرافيكي', 'Graphic Design', 'Art of visual communication and creative design', 'Creativity, artistic taste, technical software skills, communication', 'Graphic designer, UI/UX designer, visual identity designer', 'low', 'medium', '6000-15000 SAR', NULL, '2026-01-31 10:52:52'),
(8, 'الهندسة المعمارية', 'Architecture', 'Design and planning of buildings and spaces', 'Creativity, drawing, mathematics, engineering, planning', 'Architect, urban planner, interior designer', 'high', 'medium', '12000-28000 SAR', NULL, '2026-01-31 10:52:52'),
(9, 'علم النفس', 'Psychology', 'Study of human behavior and mental processes', 'Listening, empathy, analysis, scientific research', 'Psychologist, counselor, researcher, therapist', 'medium', 'medium', '8000-20000 SAR', NULL, '2026-01-31 10:52:52'),
(10, 'الهندسة الميكانيكية', 'Mechanical Engineering', 'Design and analysis of mechanical systems', 'Mathematics, physics, design, problem solving', 'Mechanical engineer, manufacturing engineer, maintenance engineer', 'high', 'high', '13000-30000 SAR', NULL, '2026-01-31 10:52:52'),
(11, 'هندسة الحاسوب', 'Computer Engineering', 'Combines electrical engineering and computer science', 'Logical analysis, programming, mathematics', 'Software engineer, systems engineer, application developer', 'high', 'high', '15000-35000 SAR', NULL, '2026-01-31 10:55:12'),
(12, 'الطب البشري', 'Medicine', 'Study of the human body, diagnosis and treatment of diseases', 'Patience, precision, empathy, strong memory', 'General physician, specialist, consultant, medical researcher', 'high', 'high', '20000-50000 SAR', NULL, '2026-01-31 10:55:12'),
(13, 'العلوم السياسية', 'Political Science', 'Study of political systems and international relations', 'Analysis, communication, research, writing', 'Political analyst, diplomat, researcher, journalist', 'medium', 'medium', '8000-18000 SAR', NULL, '2026-01-31 10:55:12'),
(14, 'إدارة الأعمال', 'Business Administration', 'Study of management principles and strategic planning', 'Leadership, organization, communication, financial analysis', 'Project manager, administrative consultant, business analyst', 'medium', 'high', '10000-25000 SAR', NULL, '2026-01-31 10:55:12'),
(15, 'علوم الحاسب', 'Computer Science', 'Study of computer theory, programming, and artificial intelligence', 'Programming, mathematics, problem solving, logical thinking', 'Programmer, data analyst, AI engineer, web developer', 'high', 'high', '12000-30000 SAR', NULL, '2026-01-31 10:55:12'),
(16, 'الهندسة الكهربائية', 'Electrical Engineering', 'Study of electricity, electronics, and energy', 'Mathematics, physics, analysis, design', 'Electrical engineer, power engineer, electronics engineer', 'high', 'high', '14000-32000 SAR', NULL, '2026-01-31 10:55:12'),
(17, 'التصميم الجرافيكي', 'Graphic Design', 'Art of visual communication and creative design', 'Creativity, artistic taste, technical software skills, communication', 'Graphic designer, UI/UX designer, visual identity designer', 'low', 'medium', '6000-15000 SAR', NULL, '2026-01-31 10:55:12'),
(18, 'الهندسة المعمارية', 'Architecture', 'Design and planning of buildings and spaces', 'Creativity, drawing, mathematics, engineering, planning', 'Architect, urban planner, interior designer', 'high', 'medium', '12000-28000 SAR', NULL, '2026-01-31 10:55:12'),
(19, 'علم النفس', 'Psychology', 'Study of human behavior and mental processes', 'Listening, empathy, analysis, scientific research', 'Psychologist, counselor, researcher, therapist', 'medium', 'medium', '8000-20000 SAR', NULL, '2026-01-31 10:55:12'),
(20, 'الهندسة الميكانيكية', 'Mechanical Engineering', 'Design and analysis of mechanical systems', 'Mathematics, physics, design, problem solving', 'Mechanical engineer, manufacturing engineer, maintenance engineer', 'high', 'high', '13000-30000 SAR', NULL, '2026-01-31 10:55:12'),
(21, 'علوم الحاسب', 'Computer Science', 'Study of computer theory, programming, algorithms, and artificial intelligence', 'Programming, mathematics, problem solving, logical thinking, technical creativity', 'Programmer, data analyst, AI engineer, web developer, software engineer, information security specialist', 'high', 'high', '12,000 - 30,000 SAR', NULL, '2026-02-01 07:05:29'),
(22, 'الطب البشري', 'Medicine', 'Study of the human body, diagnosis, treatment and prevention of diseases', 'Patience, precision, empathy, strong memory, analytical ability, working under pressure', 'General physician, specialist, consultant, medical researcher, surgeon, emergency physician', 'high', 'high', '20,000 - 50,000 SAR', NULL, '2026-02-01 07:05:29'),
(23, 'الهندسة الكهربائية', 'Electrical Engineering', 'Study of electricity, electronics, energy and communications', 'Mathematics, physics, analysis, design, technical problem solving', 'Electrical engineer, power engineer, electronics engineer, communications engineer, control engineer', 'high', 'high', '14,000 - 32,000 SAR', NULL, '2026-02-01 07:05:29'),
(24, 'إدارة الأعمال', 'Business Administration', 'Study of management principles, strategic planning and resource management', 'Leadership, organization, communication, financial analysis, decision making, negotiation', 'Project manager, administrative consultant, business analyst, HR manager, entrepreneur', 'medium', 'high', '10,000 - 25,000 SAR', NULL, '2026-02-01 07:05:29'),
(25, 'التصميم الجرافيكي', 'Graphic Design', 'Art of visual communication and creative design for print and digital media', 'Creativity, artistic taste, technical software skills (Photoshop, Illustrator), visual communication', 'Graphic designer, UI/UX designer, visual identity designer, advertising designer, digital artist', 'low', 'medium', '6,000 - 15,000 SAR', NULL, '2026-02-01 07:05:29'),
(26, 'الهندسة المعمارية', 'Architecture', 'Design and planning of buildings and urban spaces', 'Creativity, drawing, mathematics, engineering, spatial planning, innovation', 'Architect, urban planner, interior designer, architectural consultant, construction project manager', 'high', 'medium', '12,000 - 28,000 SAR', NULL, '2026-02-01 07:05:29'),
(27, 'علم النفس', 'Psychology', 'Study of human behavior, mental processes and psychological disorders', 'Listening, empathy, analysis, scientific research, patience, effective communication', 'Psychologist, psychological counselor, researcher, behavioral therapist, human development specialist', 'medium', 'medium', '8,000 - 20,000 SAR', NULL, '2026-02-01 07:05:29'),
(28, 'الهندسة الميكانيكية', 'Mechanical Engineering', 'Design and analysis of mechanical and thermal systems', 'Mathematics, physics, design, problem solving, technical creativity, analytical thinking', 'Mechanical engineer, manufacturing engineer, maintenance engineer, automotive engineer, engineering consultant', 'high', 'high', '13,000 - 30,000 SAR', NULL, '2026-02-01 07:05:29'),
(29, 'تقنية المعلومات', 'Information Technology', 'Management and application of computer technologies in business environments', 'Computer literacy, continuous learning ability, communication skills, technical problem solving', 'Systems manager, cybersecurity specialist, database administrator, systems analyst, network manager', 'medium', 'high', '12,000 - 25,000 SAR', NULL, '2026-02-01 07:05:29'),
(30, 'المحاسبة', 'Accounting', 'Recording, analyzing financial transactions and preparing reports', 'Accuracy, organization, mathematics, financial analysis, compliance, integrity', 'Accountant, auditor, financial analyst, tax consultant, financial manager', 'medium', 'high', '8,000 - 20,000 SAR', NULL, '2026-02-01 07:05:29');
-- --------------------------------------------------------

--
-- بنية الجدول `majors_book`
--

CREATE TABLE `majors_book` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `author` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `download_url` varchar(200) NOT NULL,
  `pages` int(11) NOT NULL,
  `format` varchar(10) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `major_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `majors_book`
--

INSERT INTO `majors_book` (`id`, `title`, `author`, `description`, `download_url`, `pages`, `format`, `created_at`, `major_id`) VALUES
(1, 'Python Crash Course', 'Eric Matthes', '???????? ???????? ???????? ?????????? Python', 'https://github.com/topics/python', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(2, 'Clean Code', 'Robert C. Martin', '?????????? ?????? ?????????? ????????', 'https://github.com/topics/clean-code', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(3, 'Introduction to Algorithms', 'Thomas H. Cormen', '???????? ???????? ???? ??????????????????????', 'https://mitpress.mit.edu', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(4, 'The Lean Startup', 'Eric Ries', '???????????? Startup ??????????????', 'https://theleanstartup.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(5, 'Thinking, Fast and Slow', 'Daniel Kahneman', '?????? ?????????? ??????????????', 'https://www.amazon.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(6, 'The Design of Everyday Things', 'Don Norman', '?????????? ??????????????', 'https://www.nngroup.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(7, 'Fundamentals of Electric Circuits', 'Charles Alexander', '?????????????? ?????????????? ????????????????????', 'https://www.mheducation.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(8, 'Principles of Marketing', 'Philip Kotler', '?????????? ??????????????', 'https://www.pearson.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(9, 'Building Construction Handbook', 'Roy Chudley', '???????? ???????????? ????????????????', 'https://www.routledge.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(10, 'University Physics', 'Hugh D. Young', '???????????? ???????????? ??????????', 'https://www.pearson.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(11, 'Python Crash Course', 'Eric Matthes', 'دليل عملي شامل لتعلم Python', 'https://github.com/topics/python', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(12, 'Clean Code', 'Robert C. Martin', 'كتابة كود برمجي نظيف', 'https://github.com/topics/clean-code', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(13, 'Introduction to Algorithms', 'Thomas H. Cormen', 'كتاب شامل عن الخوارزميات', 'https://mitpress.mit.edu', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(14, 'The Lean Startup', 'Eric Ries', 'منهجية Startup الحديثة', 'https://theleanstartup.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(15, 'Thinking, Fast and Slow', 'Daniel Kahneman', 'علم النفس المعرفي', 'https://www.amazon.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(16, 'The Design of Everyday Things', 'Don Norman', 'مبادئ التصميم', 'https://www.nngroup.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(17, 'Fundamentals of Electric Circuits', 'Charles Alexander', 'أساسيات الدوائر الكهربائية', 'https://www.mheducation.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(18, 'Principles of Marketing', 'Philip Kotler', 'مبادئ التسويق', 'https://www.pearson.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(19, 'Building Construction Handbook', 'Roy Chudley', 'دليل البناء والتشييد', 'https://www.routledge.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(20, 'University Physics', 'Hugh D. Young', 'فيزياء جامعية شاملة', 'https://www.pearson.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(21, 'Python Crash Course', 'Eric Matthes', 'دليل عملي شامل لتعلم البرمجة بلغة Python', 'https://github.com/topics/python', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(22, 'Clean Code', 'Robert C. Martin', 'كتابة كود برمجي نظيف وقابل للصيانة', 'https://github.com/topics/clean-code', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(23, 'Introduction to Algorithms', 'Thomas H. Cormen', 'كتاب شامل عن الخوارزميات وهياكل البيانات', 'https://mitpress.mit.edu', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(24, 'The Lean Startup', 'Eric Ries', 'منهجية Startup الحديثة لإطلاق المشاريع', 'https://theleanstartup.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(25, 'Thinking, Fast and Slow', 'Daniel Kahneman', 'علم النفس المعرفي وكيف نتخذ القرارات', 'https://www.amazon.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(26, 'The Design of Everyday Things', 'Don Norman', 'مبادئ التصميم الجيد للمنتجات', 'https://www.nngroup.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(27, 'Fundamentals of Electric Circuits', 'Charles Alexander', 'أساسيات الدوائر الكهربائية', 'https://www.mheducation.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(28, 'Principles of Marketing', 'Philip Kotler', 'مبادئ التسويق الحديث', 'https://www.pearson.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(29, 'Building Construction Handbook', 'Roy Chudley', 'دليل البناء والتشييد الشامل', 'https://www.routledge.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(30, 'University Physics', 'Hugh D. Young', 'فيزياء جامعية شاملة ومتقدمة', 'https://www.pearson.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(31, 'Artificial Intelligence: A Modern Approach', 'Stuart Russell', 'المرجع الشامل في الذكاء الاصطناعي', 'https://aima.cs.berkeley.edu', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(32, 'Accounting Principles', 'Jerry Weygandt', 'مبادئ المحاسبة المالية', 'https://www.wiley.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(33, 'Gray\'s Anatomy', 'Henry Gray', 'المرجع الطبي الأشهر في علم التشريح', 'https://www.elsevier.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(34, 'Introduction to Psychology', 'James Kalat', 'مقدمة شاملة في علم النفس', 'https://www.cengage.com', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL),
(35, 'The Art of Electronics', 'Paul Horowitz', 'فن الإلكترونيات العملية', 'https://artofelectronics.net', 0, 'pdf', '2026-03-31 09:42:17.000000', NULL);

-- --------------------------------------------------------

--
-- بنية الجدول `majors_course`
--

CREATE TABLE `majors_course` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `url` varchar(200) NOT NULL,
  `platform` varchar(100) NOT NULL,
  `duration` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `type` varchar(10) NOT NULL,
  `language` varchar(50) NOT NULL,
  `rating` decimal(3,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `major_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `majors_course`
--
INSERT INTO `majors_course` (`id`, `title`, `description`, `url`, `platform`, `duration`, `price`, `type`, `language`, `rating`, `created_at`, `major_id`) VALUES
(1, 'Introduction to Programming - Python', 'Comprehensive course to learn programming basics', 'https://www.coursera.org/learn/python', 'Coursera', '4 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(2, 'Web Application Development', 'Learn HTML, CSS, JavaScript', 'https://www.udemy.com/web-development', 'Udemy', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(3, 'Artificial Intelligence and Machine Learning', 'Comprehensive introduction to AI and ML', 'https://www.edx.org/course/ai-ml', 'edX', '12 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(4, 'Professional Project Management', 'Project management fundamentals', 'https://www.linkedin.com/learning', 'LinkedIn Learning', '6 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(5, 'Graphic Design for Beginners', 'Learn Adobe Photoshop & Illustrator', 'https://www.udemy.com/graphic-design', 'Udemy', '5 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(6, 'Psychology Basics', 'Introduction to psychology', 'https://www.coursera.org/learn/psychology', 'Coursera', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(7, 'Basic Electrical Engineering', 'Principles of electricity and electronics', 'https://ocw.mit.edu', 'MIT OpenCourseWare', '10 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(8, 'Digital Marketing', 'Modern marketing strategies', 'https://learndigital.withgoogle.com', 'Google Digital Garage', '4 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(9, 'Building Design with AutoCAD', 'Learn architectural drawing', 'https://www.udemy.com/autocad-course', 'Udemy', '7 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(10, 'University Physics', 'Advanced physics', 'https://www.khanacademy.org/physics', 'Khan Academy', '16 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(11, 'Introduction to Programming - Python', 'Comprehensive course to learn programming basics using Python from scratch', 'https://www.coursera.org/learn/python', 'Coursera', '4 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(12, 'Full Stack Web Application Development', 'Learn full stack web development using HTML, CSS, JavaScript, Node.js', 'https://www.udemy.com/web-development', 'Udemy', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(13, 'Artificial Intelligence and Machine Learning', 'Comprehensive introduction to AI and ML using Python', 'https://www.edx.org/course/ai-ml', 'edX', '12 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(14, 'Professional Project Management', 'Project management fundamentals and Agile & Scrum methodology', 'https://www.linkedin.com/learning', 'LinkedIn Learning', '6 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(15, 'Graphic Design for Beginners', 'Learn Adobe Photoshop and Illustrator from scratch', 'https://www.udemy.com/graphic-design', 'Udemy', '5 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(16, 'Psychology Basics', 'Comprehensive introduction to psychology and human behavior', 'https://www.coursera.org/learn/psychology', 'Coursera', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(17, 'Basic Electrical Engineering', 'Principles of electricity and electronics for beginners', 'https://ocw.mit.edu', 'MIT OpenCourseWare', '10 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(18, 'Modern Digital Marketing', 'Digital marketing and social media strategies', 'https://learndigital.withgoogle.com', 'Google Digital Garage', '4 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(19, 'Building Design with AutoCAD', 'Learn engineering architectural drawing using AutoCAD', 'https://www.udemy.com/autocad-course', 'Udemy', '7 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(20, 'Advanced University Physics', 'Advanced physics for university students', 'https://www.khanacademy.org/physics', 'Khan Academy', '16 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(21, 'Introduction to Programming - Python', 'Comprehensive course to learn programming basics using Python from scratch', 'https://www.coursera.org/learn/python', 'Coursera', '4 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(22, 'Full Stack Web Application Development', 'Learn full stack web development using HTML, CSS, JavaScript, Node.js', 'https://www.udemy.com/web-development', 'Udemy', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(23, 'Artificial Intelligence and Machine Learning', 'Comprehensive introduction to AI and ML using Python', 'https://www.edx.org/course/ai-ml', 'edX', '12 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(24, 'Professional Project Management', 'Project management fundamentals and Agile & Scrum methodology', 'https://www.linkedin.com/learning', 'LinkedIn Learning', '6 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(25, 'Graphic Design for Beginners', 'Learn Adobe Photoshop and Illustrator from scratch', 'https://www.udemy.com/graphic-design', 'Udemy', '5 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(26, 'Psychology Basics', 'Comprehensive introduction to psychology and human behavior', 'https://www.coursera.org/learn/psychology', 'Coursera', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(27, 'Basic Electrical Engineering', 'Principles of electricity and electronics for beginners', 'https://ocw.mit.edu', 'MIT OpenCourseWare', '10 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(28, 'Modern Digital Marketing', 'Digital marketing and social media strategies', 'https://learndigital.withgoogle.com', 'Google Digital Garage', '4 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(29, 'Building Design with AutoCAD', 'Learn engineering architectural drawing using AutoCAD', 'https://www.udemy.com/autocad-course', 'Udemy', '7 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(30, 'Advanced University Physics', 'Advanced physics for university students', 'https://www.khanacademy.org/physics', 'Khan Academy', '16 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(31, 'Mobile App Development', 'Learn iOS and Android app development', 'https://www.udacity.com/mobile', 'Udacity', '10 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(32, 'Financial Accounting', 'Basics of accounting and financial statements', 'https://www.coursera.org/accounting', 'Coursera', '6 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(33, 'Cybersecurity', 'Protecting systems and networks from attacks', 'https://www.cybrary.it', 'Cybrary', '8 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(34, 'Statistical Analysis', 'Learn statistics and data analysis', 'https://www.datacamp.com', 'DataCamp', '5 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL),
(35, 'UI/UX Design', 'Principles of user experience design', 'https://www.interaction-design.org', 'Interaction Design Foundation', '6 weeks', 0.00, 'free', 'English', 4.00, '2026-03-31 09:42:17.000000', NULL);
-- --------------------------------------------------------

--
-- بنية الجدول `majors_major`
--

CREATE TABLE `majors_major` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `duration` varchar(50) NOT NULL,
  `requirements` longtext DEFAULT NULL,
  `job_opportunities` longtext NOT NULL,
  `average_salary` varchar(100) NOT NULL,
  `demand_level` varchar(50) NOT NULL,
  `level` varchar(20) NOT NULL,
  `universities` longtext DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `majors_major`
--
INSERT INTO `majors_major` (`id`, `name`, `description`, `duration`, `requirements`, `job_opportunities`, `average_salary`, `demand_level`, `level`, `universities`, `image_url`, `created_at`, `category_id`) VALUES
(1, 'Computer Engineering', 'Combines electrical engineering and computer science', '4 years', 'Logical analysis, programming, mathematics', 'Software engineer, systems engineer, application developer', '15000-35000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(2, 'Medicine', 'Study of the human body, diagnosis and treatment of diseases', '4 years', 'Patience, precision, empathy, strong memory', 'General physician, specialist, consultant, medical researcher', '20000-50000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 2),
(3, 'Political Science', 'Study of political systems and international relations', '4 years', 'Analysis, communication, research, writing', 'Political analyst, diplomat, researcher, journalist', '8000-18000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 4),
(4, 'Business Administration', 'Study of management principles and strategic planning', '4 years', 'Leadership, organization, communication, financial analysis', 'Project manager, administrative consultant, business analyst', '10000-25000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 3),
(5, 'Computer Science', 'Study of computer theory, programming, and artificial intelligence', '4 years', 'Programming, mathematics, problem solving, logical thinking', 'Programmer, data analyst, AI engineer, web developer', '12000-30000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 4),
(6, 'Electrical Engineering', 'Study of electricity, electronics, and energy', '4 years', 'Mathematics, physics, analysis, design', 'Electrical engineer, power engineer, electronics engineer', '14000-32000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(7, 'Graphic Design', 'Art of visual communication and creative design', '4 years', 'Creativity, artistic taste, technical software skills, communication', 'Graphic designer, UI/UX designer, visual identity designer', '6000-15000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 5),
(8, 'Architecture', 'Design and planning of buildings and spaces', '4 years', 'Creativity, drawing, mathematics, engineering, planning', 'Architect, urban planner, interior designer', '12000-28000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 5),
(9, 'Psychology', 'Study of human behavior and mental processes', '4 years', 'Listening, empathy, analysis, scientific research', 'Psychologist, counselor, researcher, therapist', '8000-20000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 6),
(10, 'Mechanical Engineering', 'Design and analysis of mechanical systems', '4 years', 'Mathematics, physics, design, problem solving', 'Mechanical engineer, manufacturing engineer, maintenance engineer', '13000-30000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(11, 'Computer Engineering', 'Combines electrical engineering and computer science', '4 years', 'Logical analysis, programming, mathematics', 'Software engineer, systems engineer, application developer', '15000-35000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(12, 'Medicine', 'Study of the human body, diagnosis and treatment of diseases', '4 years', 'Patience, precision, empathy, strong memory', 'General physician, specialist, consultant, medical researcher', '20000-50000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 2),
(13, 'Political Science', 'Study of political systems and international relations', '4 years', 'Analysis, communication, research, writing', 'Political analyst, diplomat, researcher, journalist', '8000-18000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 4),
(14, 'Business Administration', 'Study of management principles and strategic planning', '4 years', 'Leadership, organization, communication, financial analysis', 'Project manager, administrative consultant, business analyst', '10000-25000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 3),
(15, 'Computer Science', 'Study of computer theory, programming, and artificial intelligence', '4 years', 'Programming, mathematics, problem solving, logical thinking', 'Programmer, data analyst, AI engineer, web developer', '12000-30000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 4),
(16, 'Electrical Engineering', 'Study of electricity, electronics, and energy', '4 years', 'Mathematics, physics, analysis, design', 'Electrical engineer, power engineer, electronics engineer', '14000-32000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(17, 'Graphic Design', 'Art of visual communication and creative design', '4 years', 'Creativity, artistic taste, technical software skills, communication', 'Graphic designer, UI/UX designer, visual identity designer', '6000-15000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 5),
(18, 'Architecture', 'Design and planning of buildings and spaces', '4 years', 'Creativity, drawing, mathematics, engineering, planning', 'Architect, urban planner, interior designer', '12000-28000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 5),
(19, 'Psychology', 'Study of human behavior and mental processes', '4 years', 'Listening, empathy, analysis, scientific research', 'Psychologist, counselor, researcher, therapist', '8000-20000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 6),
(20, 'Mechanical Engineering', 'Design and analysis of mechanical systems', '4 years', 'Mathematics, physics, design, problem solving', 'Mechanical engineer, manufacturing engineer, maintenance engineer', '13000-30000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(21, 'Computer Science', 'Study of computer theory, programming, algorithms, and artificial intelligence', '4 years', 'Programming, mathematics, problem solving, logical thinking, technical creativity', 'Programmer, data analyst, AI engineer, web developer, software engineer, information security specialist', '12,000 - 30,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 4),
(22, 'Medicine', 'Study of the human body, diagnosis, treatment and prevention of diseases', '4 years', 'Patience, precision, empathy, strong memory, analytical ability, working under pressure', 'General physician, specialist, consultant, medical researcher, surgeon, emergency physician', '20,000 - 50,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 2),
(23, 'Electrical Engineering', 'Study of electricity, electronics, energy and communications', '4 years', 'Mathematics, physics, analysis, design, technical problem solving', 'Electrical engineer, power engineer, electronics engineer, communications engineer, control engineer', '14,000 - 32,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(24, 'Business Administration', 'Study of management principles, strategic planning and resource management', '4 years', 'Leadership, organization, communication, financial analysis, decision making, negotiation', 'Project manager, administrative consultant, business analyst, HR manager, entrepreneur', '10,000 - 25,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 3),
(25, 'Graphic Design', 'Art of visual communication and creative design for print and digital media', '4 years', 'Creativity, artistic taste, technical software skills (Photoshop, Illustrator), visual communication', 'Graphic designer, UI/UX designer, visual identity designer, advertising designer, digital artist', '6,000 - 15,000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 5),
(26, 'Architecture', 'Design and planning of buildings and urban spaces', '4 years', 'Creativity, drawing, mathematics, engineering, spatial planning, innovation', 'Architect, urban planner, interior designer, architectural consultant, construction project manager', '12,000 - 28,000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 5),
(27, 'Psychology', 'Study of human behavior, mental processes and psychological disorders', '4 years', 'Listening, empathy, analysis, scientific research, patience, effective communication', 'Psychologist, psychological counselor, researcher, behavioral therapist, human development specialist', '8,000 - 20,000 SAR', 'medium', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 6),
(28, 'Mechanical Engineering', 'Design and analysis of mechanical and thermal systems', '4 years', 'Mathematics, physics, design, problem solving, technical creativity, analytical thinking', 'Mechanical engineer, manufacturing engineer, maintenance engineer, automotive engineer, engineering consultant', '13,000 - 30,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 1),
(29, 'Information Technology', 'Management and application of computer technologies in business environments', '4 years', 'Computer literacy, continuous learning ability, communication skills, technical problem solving', 'Systems manager, cybersecurity specialist, database administrator, systems analyst, network manager', '12,000 - 25,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 8),
(30, 'Accounting', 'Recording, analyzing financial transactions and preparing reports', '4 years', 'Accuracy, organization, mathematics, financial analysis, compliance, integrity', 'Accountant, auditor, financial analyst, tax consultant, financial manager', '8,000 - 20,000 SAR', 'high', 'bachelor', NULL, NULL, '2026-03-31 09:42:17.000000', 3);
-- --------------------------------------------------------

--
-- بنية الجدول `majors_majorcategory`
--

CREATE TABLE `majors_majorcategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `icon` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `majors_majorcategory`
--

INSERT INTO `majors_majorcategory` (`id`, `name`, `description`, `icon`) VALUES
(1, 'Engineering & Technology', 'Engineering and technical fields', 'fas fa-cogs'),
(2, 'Medicine & Health', 'Medical and health-related fields', 'fas fa-heartbeat'),
(3, 'Business & Management', 'Business and administrative fields', 'fas fa-briefcase'),
(4, 'Science & Research', 'Pure and applied sciences', 'fas fa-flask'),
(5, 'Arts & Design', 'Creative and design fields', 'fas fa-palette'),
(6, 'Social Sciences', 'Social and human sciences', 'fas fa-users'),
(7, 'Law & Politics', 'Law and political science fields', 'fas fa-balance-scale'),
(8, 'Computer Science', 'Computing and information technology', 'fas fa-laptop-code');

-- --------------------------------------------------------

--
-- بنية الجدول `majors_majorreview`
--

CREATE TABLE `majors_majorreview` (
  `id` bigint(20) NOT NULL,
  `rating` int(11) NOT NULL,
  `review_text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `major_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `majors_userrecommendation`
--

CREATE TABLE `majors_userrecommendation` (
  `id` bigint(20) NOT NULL,
  `match_percentage` decimal(5,2) NOT NULL,
  `reason` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `major_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_text` text NOT NULL,
  `question_type` enum('strength','interest','subject','skill','personality') NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `options` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`options`)),
  `weight` decimal(3,2) DEFAULT 1.00,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
--
-- إرجاع أو استيراد بيانات الجدول `questions`
--
INSERT INTO `questions` (`id`, `question_text`, `question_type`, `category`, `options`, `weight`, `created_at`) VALUES
-- Original Questions Translated
(1, 'Which academic subjects do you prefer?', 'subject', 'academic', '["Mathematics", "Physics", "Chemistry", "Biology", "Arabic Language", "English Language", "History", "Geography"]', 1.00, '2026-01-31 10:55:12'),
(2, 'What skills do you possess?', 'skill', 'personal', '["Logical Analysis", "Creativity", "Communication", "Leadership", "Teamwork", "Problem Solving", "Organization", "Listening"]', 1.00, '2026-01-31 10:55:12'),
(3, 'What do you prefer to do in your free time?', 'interest', 'hobbies', '["Reading", "Drawing", "Programming", "Sports", "Teaching", "Helping Others", "Discovery", "Designing"]', 1.00, '2026-01-31 10:55:12'),
(4, 'In which environment do you prefer to work?', 'personality', 'work_environment', '["Traditional Office", "Field Work", "Laboratories", "Remote Work", "Workshops", "Creative Environment"]', 1.00, '2026-01-31 10:55:12'),
(5, 'What are your main strengths?', 'strength', 'personal', '["Analytical Thinking", "Creativity and Innovation", "Communication Skills", "Ability to Learn Quickly", "Patience and Endurance", "Leadership"]', 1.20, '2026-01-31 10:55:12'),
(6, 'Which of these activities do you enjoy?', 'interest', 'activities', '["Solving Puzzles", "Art and Design", "Writing and Reading", "Practical Experiments", "Social Interaction", "Strategic Games"]', 1.00, '2026-01-31 10:55:12'),
(7, 'How do you prefer to solve problems?', 'skill', 'problem_solving', '["Logical Analysis and Numbers", "Creativity and Unconventional Solutions", "Research and Reading", "Practical Experimentation", "Discussion with Others"]', 1.10, '2026-01-31 10:55:12'),
(8, 'What is your level of interest in technology?', 'interest', 'technology', '["Very interested", "Active user", "Normal use", "Limited interest", "Not interested"]', 1.00, '2026-01-31 10:55:12'),
(9, 'What is your preferred learning style?', 'personality', 'learning_style', '["Theoretical and Reading", "Practical and Experimental", "Visual and Video", "Discussion and Dialogue", "Self-taught"]', 1.00, '2026-01-31 10:55:12'),
(10, 'How ready are you to handle pressure?', 'strength', 'stress_management', '["Handle high pressure", "Handle medium pressure", "Prefer quiet environment", "Prefer no pressure"]', 0.90, '2026-01-31 10:55:12'),
(11, 'How interested are you in helping others?', 'interest', 'social', '["Very important", "Important but not priority", "Average interest", "Not a priority"]', 1.00, '2026-01-31 10:55:12'),
(12, 'Do you prefer individual or group work?', 'personality', 'work_style', '["Entirely individual", "Mostly individual", "Balanced mix", "Mostly group", "Entirely group"]', 1.00, '2026-01-31 10:55:12'),
(13, 'What is your level of public speaking ability?', 'skill', 'public_speaking', '["Excellent", "Good", "Acceptable with tension", "Difficult for me"]', 0.80, '2026-01-31 10:55:12'),
(14, 'How much time can you spend studying daily?', 'personality', 'study_habits', '["Over 4 hours", "2-4 hours", "1-2 hours", "Less than 1 hour"]', 1.00, '2026-01-31 10:55:12'),
(15, 'How much do you care about fine details?', 'skill', 'attention_to_detail', '["Very detailed", "Focus on important details", "Big picture focus", "Not a priority"]', 1.00, '2026-01-31 10:55:12'),
(16, 'Which academic subjects do you prefer? (Extended)', 'subject', 'academic', '["Math", "Physics", "Chemistry", "Biology", "Arabic", "English", "History", "Geography", "Computer Science", "Art"]', 1.20, '2026-02-01 07:05:29'),
(17, 'What skills do you possess most?', 'skill', 'personal', '["Logic", "Creativity", "Communication", "Leadership", "Teamwork", "Problem Solving", "Planning", "Listening"]', 1.20, '2026-02-01 07:05:29'),
(18, 'What do you prefer in your leisure time?', 'interest', 'hobbies', '["Writing", "Design", "Tech", "Sports", "Courses", "Volunteering", "Research", "Movies"]', 1.10, '2026-02-01 07:05:29'),
(19, 'In which environment do you prefer to work?', 'personality', 'work_environment', '["Office", "Field", "Lab", "Remote", "Workshop", "Creative", "Hospital"]', 1.00, '2026-02-01 07:05:29'),
(20, 'What are your key strengths?', 'strength', 'personal', '["Analytical", "Creative", "Communicative", "Quick learner", "Patient", "Leader", "Detail-oriented"]', 1.30, '2026-02-01 07:05:29'),
(21, 'Which activities do you enjoy?', 'interest', 'activities', '["Math Puzzles", "Art", "Writing", "Experiments", "Socializing", "Strategy Games", "Volunteering"]', 1.00, '2026-02-01 07:05:29'),
(22, 'How do you prefer solving problems?', 'skill', 'problem_solving', '["Numbers", "Creative ideas", "Research", "Trial & Error", "Discussion", "Systematic planning"]', 1.20, '2026-02-01 07:05:29'),
(23, 'Interest in technology level?', 'interest', 'technology', '["Follower of new tech", "Active user", "Basic use", "Limited", "Not interested"]', 1.10, '2026-02-01 07:05:29'),
(24, 'Preferred learning style?', 'personality', 'learning_style', '["Theory", "Practice", "Visual", "Discussion", "Self-directed"]', 1.00, '2026-02-01 07:05:29'),
(25, 'Ready for pressure?', 'strength', 'stress_management', '["High pressure", "Medium pressure", "Quiet environment", "No pressure"]', 1.00, '2026-02-01 07:05:29'),
(26, 'Interest in helping others?', 'interest', 'social', '["Very important", "Important", "Average", "Not priority"]', 1.10, '2026-02-01 07:05:29'),
(27, 'Work style preference?', 'personality', 'work_style', '["Individual", "Limited collab", "Balanced", "Group with autonomy", "Entirely group"]', 1.00, '2026-02-01 07:05:29'),
(28, 'Public speaking ability?', 'skill', 'public_speaking', '["Excellent", "Good", "Acceptable", "Very difficult"]', 0.90, '2026-02-01 07:05:29'),
(29, 'Daily study hours ability?', 'personality', 'study_habits', '["Over 4 hours", "2-4 hours", "1-2 hours", "Less than 1"]', 1.00, '2026-02-01 07:05:29'),
(30, 'Attention to detail level?', 'skill', 'attention_to_detail', '["Extremely high", "High", "Big picture", "Not important"]', 1.10, '2026-02-01 07:05:29'),
(31, 'Risk tolerance level?', 'personality', 'risk_tolerance', '["Love risk", "Calculated risk", "Safety first", "Avoid risk"]', 0.90, '2026-02-01 07:05:29'),
(32, 'Routine vs Change?', 'personality', 'routine_preference', '["Love change", "Mixed", "Prefer routine", "Total routine"]', 0.80, '2026-02-01 07:05:29'),
(33, 'Interest in financial rewards?', 'interest', 'financial', '["Top priority", "Very important", "Important but not main", "Not important"]', 0.70, '2026-02-01 07:05:29'),
(34, 'Sector preference?', 'personality', 'sector_preference', '["Private", "Government", "No difference", "Freelance"]', 0.60, '2026-02-01 07:05:29'),
(35, 'Preferred study duration?', 'personality', 'study_duration', '["6-7 years", "4-5 years", "2-3 years", "Shortest possible"]', 0.80, '2026-02-01 07:05:29'),

-- 15 Additional Questions
(36, 'How do you feel about traveling for work?', 'personality', 'mobility', '["Love it", "Occasionally", "Only if necessary", "Prefer not to travel"]', 1.00, '2026-03-31 10:00:00'),
(37, 'Interest in nature and environment?', 'interest', 'outdoors', '["Very high", "Moderate", "Occasional", "No interest"]', 1.00, '2026-03-31 10:00:00'),
(38, 'How good are you at manual/hand-on work?', 'skill', 'manual', '["Excellent", "Good", "Basic", "Not my thing"]', 1.10, '2026-03-31 10:00:00'),
(39, 'Preference for leadership roles?', 'personality', 'leadership', '["Always lead", "Lead if asked", "Prefer to follow", "Avoid responsibility"]', 1.20, '2026-03-31 10:00:00'),
(40, 'Interest in law and justice?', 'interest', 'legal', '["Very high", "High", "Moderate", "None"]', 1.00, '2026-03-31 10:00:00'),
(41, 'Ability to multi-task?', 'skill', 'productivity', '["Excellent", "Good", "Prefer one task", "Easily distracted"]', 1.00, '2026-03-31 10:00:00'),
(42, 'Attitude towards fixed working hours?', 'personality', 'flexibility', '["Prefer 9-to-5", "Flexible hours", "Task-based", "Shift work"]', 0.90, '2026-03-31 10:00:00'),
(43, 'Interest in medical or health sciences?', 'interest', 'health', '["Passionate", "Interested", "Moderate", "None"]', 1.10, '2026-03-31 10:00:00'),
(44, 'How do you handle criticism?', 'strength', 'emotional', '["Learn from it", "Neutral", "Take it personally", "Get defensive"]', 1.00, '2026-03-31 10:00:00'),
(45, 'Interest in language learning?', 'interest', 'linguistics', '["Fluent in many", "Learning now", "Want to learn", "No interest"]', 0.80, '2026-03-31 10:00:00'),
(46, 'Decision-making style?', 'personality', 'decision_making', '["Data-driven", "Intuitive", "Consultative", "Slow/Careful"]', 1.10, '2026-03-31 10:00:00'),
(47, 'Interest in physical activity at work?', 'interest', 'physical', '["Very active", "Moderate", "Mostly sitting", "Sedentary"]', 0.90, '2026-03-31 10:00:00'),
(48, 'Capability to work with abstract concepts?', 'skill', 'abstract', '["Excellent", "Good", "Basic", "Prefer concrete"]', 1.00, '2026-03-31 10:00:00'),
(49, 'Interest in managing financial records?', 'interest', 'accounting', '["Love numbers", "Acceptable", "Boring", "Hate it"]', 1.00, '2026-03-31 10:00:00'),
(50, 'Level of curiosity about how things work?', 'strength', 'curiosity', '["Inquisitive", "Interested", "Normal", "Accepting"]', 1.20, '2026-03-31 10:00:00');
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
-- بنية الجدول `tests_choice`
--

CREATE TABLE `tests_choice` (
  `id` bigint(20) NOT NULL,
  `text` varchar(300) NOT NULL,
  `value` int(11) NOT NULL,
  `personality_traits` varchar(300) NOT NULL,
  `question_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `tests_question`
--

CREATE TABLE `tests_question` (
  `id` bigint(20) NOT NULL,
  `text` longtext NOT NULL,
  `order` int(11) NOT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `tests_questioncategory`
--

CREATE TABLE `tests_questioncategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `tests_testcategory`
--

CREATE TABLE `tests_testcategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `tests_testquestion`
--

CREATE TABLE `tests_testquestion` (
  `id` bigint(20) NOT NULL,
  `text` longtext NOT NULL,
  `option_a` varchar(200) NOT NULL,
  `option_b` varchar(200) NOT NULL,
  `option_c` varchar(200) NOT NULL,
  `option_d` varchar(200) NOT NULL,
  `weight_a` int(11) NOT NULL,
  `weight_b` int(11) NOT NULL,
  `weight_c` int(11) NOT NULL,
  `weight_d` int(11) NOT NULL,
  `category_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `tests_testresult`
--

CREATE TABLE `tests_testresult` (
  `id` bigint(20) NOT NULL,
  `score` int(11) NOT NULL,
  `result_summary` longtext NOT NULL,
  `recommended_majors` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `test_category_id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- بنية الجدول `tests_useranswer`
--

CREATE TABLE `tests_useranswer` (
  `id` bigint(20) NOT NULL,
  `answer` varchar(1) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `question_id` bigint(20) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `question_text` longtext DEFAULT NULL,
  `selected_choice` varchar(500) DEFAULT NULL,
  `test_result_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

--
-- إرجاع أو استيراد بيانات الجدول `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `full_name`, `date_of_birth`, `gender`, `phone`, `created_at`, `updated_at`) VALUES
(1, 'student', 'student@test.com', 'e10adc3949ba59abbe56e057f20f883e', 'محمد أحمد عبدالله', '2005-05-15', 'male', '0501234567', '2026-02-01 07:17:25', '2026-02-01 07:17:25'),
(2, 'admin', 'admin@test.com', '0192023a7bbd73250516f069df18b500', 'المدير العام', '1990-01-01', 'male', '0550000000', '2026-02-01 07:17:25', '2026-02-01 07:17:25'),
(3, 'test', 'test@test.com', 'cc03e747a6afbbcbf8be7668acfebee5', 'مستخدم تجريبي', '2000-06-20', 'female', '0559876543', '2026-02-01 07:17:25', '2026-02-01 07:17:25'),
(4, 'ahmed', 'ahmed@example.com', 'e10adc3949ba59abbe56e057f20f883e', 'أحمد محمود', '2004-03-10', 'male', '0551112233', '2026-02-01 07:17:25', '2026-02-01 07:17:25'),
(5, 'sara', 'sara@example.com', 'e10adc3949ba59abbe56e057f20f883e', 'سارة علي', '2005-08-22', 'female', '0554445566', '2026-02-01 07:17:25', '2026-02-01 07:17:25');

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
-- إرجاع أو استيراد بيانات الجدول `user_results`
--

INSERT INTO `user_results` (`id`, `user_id`, `personality_type`, `strengths_summary`, `interests_summary`, `ai_analysis`, `test_score`, `completed_at`) VALUES
(1, 1, 'محلل منطقي', 'التفكير التحليلي، حل المشكلات، الرياضيات', 'البرمجة، التكنولوجيا، العلوم', '{\"learning_style\": \"بصري وعملي\", \"work_environment\": \"مكتب تقني\", \"recommendations\": [\"علوم الحاسب\", \"هندسة البرمجيات\", \"الذكاء الاصطناعي\"]}', 85, '2026-02-01 07:17:25'),
(2, 4, 'مبدع فني', 'الإبداع، التصميم، التفكير خارج الصندوق', 'الفنون، التصميم، الميديا', '{\"learning_style\": \"بصري وإبداعي\", \"work_environment\": \"استوديو إبداعي\", \"recommendations\": [\"التصميم الجرافيكي\", \"العمارة\", \"الإعلام\"]}', 78, '2026-02-01 07:17:25'),
(3, 5, 'اجتماعية متعاونة', 'التواصل، مساعدة الآخرين، العمل الجماعي', 'التعليم، الصحة، الخدمة الاجتماعية', '{\"learning_style\": \"سمعي وتفاعلي\", \"work_environment\": \"بيئة اجتماعية\", \"recommendations\": [\"علم النفس\", \"التربية\", \"الخدمة الاجتماعية\"]}', 92, '2026-02-01 07:17:25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_notification`
--
ALTER TABLE `accounts_notification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `accounts_notification_user_id_30e6cfc5_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `accounts_userprofile`
--
ALTER TABLE `accounts_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `advisor_aiconversation`
--
ALTER TABLE `advisor_aiconversation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `advisor_aiconversation_user_id_1e488b72_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `advisor_aimessage`
--
ALTER TABLE `advisor_aimessage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `advisor_aimessage_conversation_id_1aca98c5_fk_advisor_a` (`conversation_id`);

--
-- Indexes for table `advisor_contactmessage`
--
ALTER TABLE `advisor_contactmessage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `advisor_faq`
--
ALTER TABLE `advisor_faq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `advisor_university`
--
ALTER TABLE `advisor_university`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `question_id` (`question_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `majors_book`
--
ALTER TABLE `majors_book`
  ADD PRIMARY KEY (`id`),
  ADD KEY `majors_book_major_id_7c45f28c_fk_majors_major_id` (`major_id`);

--
-- Indexes for table `majors_course`
--
ALTER TABLE `majors_course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `majors_course_major_id_d33e62bf_fk_majors_major_id` (`major_id`);

--
-- Indexes for table `majors_major`
--
ALTER TABLE `majors_major`
  ADD PRIMARY KEY (`id`),
  ADD KEY `majors_major_category_id_97c97915_fk_majors_majorcategory_id` (`category_id`);

--
-- Indexes for table `majors_majorcategory`
--
ALTER TABLE `majors_majorcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `majors_majorreview`
--
ALTER TABLE `majors_majorreview`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `majors_majorreview_user_id_major_id_e8815ad0_uniq` (`user_id`,`major_id`),
  ADD KEY `majors_majorreview_major_id_79bd284b_fk_majors_major_id` (`major_id`);

--
-- Indexes for table `majors_userrecommendation`
--
ALTER TABLE `majors_userrecommendation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `majors_userrecommendation_major_id_1a0fe3ac_fk_majors_major_id` (`major_id`),
  ADD KEY `majors_userrecommendation_user_id_266351d9_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `tests_choice`
--
ALTER TABLE `tests_choice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tests_choice_question_id_b35df5fe_fk_tests_question_id` (`question_id`);

--
-- Indexes for table `tests_question`
--
ALTER TABLE `tests_question`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tests_question_category_id_77224b3b_fk_tests_questioncategory_id` (`category_id`);

--
-- Indexes for table `tests_questioncategory`
--
ALTER TABLE `tests_questioncategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tests_testcategory`
--
ALTER TABLE `tests_testcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tests_testquestion`
--
ALTER TABLE `tests_testquestion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tests_testquestion_category_id_8bccc9d9_fk_tests_testcategory_id` (`category_id`);

--
-- Indexes for table `tests_testresult`
--
ALTER TABLE `tests_testresult`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tests_testresult_test_category_id_53e675b2_fk_tests_tes` (`test_category_id`),
  ADD KEY `tests_testresult_user_id_b9595301_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `tests_useranswer`
--
ALTER TABLE `tests_useranswer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tests_useranswer_user_id_10967465` (`user_id`),
  ADD KEY `tests_useranswer_test_result_id_e462c9fd_fk_tests_testresult_id` (`test_result_id`),
  ADD KEY `tests_useranswer_question_id_2a91e6d6_fk_tests_testquestion_id` (`question_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_notification`
--
ALTER TABLE `accounts_notification`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `accounts_userprofile`
--
ALTER TABLE `accounts_userprofile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `advisor_aiconversation`
--
ALTER TABLE `advisor_aiconversation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `advisor_aimessage`
--
ALTER TABLE `advisor_aimessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `advisor_contactmessage`
--
ALTER TABLE `advisor_contactmessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `advisor_faq`
--
ALTER TABLE `advisor_faq`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `advisor_university`
--
ALTER TABLE `advisor_university`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `majors_book`
--
ALTER TABLE `majors_book`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `majors_course`
--
ALTER TABLE `majors_course`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `majors_major`
--
ALTER TABLE `majors_major`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `majors_majorcategory`
--
ALTER TABLE `majors_majorcategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `majors_majorreview`
--
ALTER TABLE `majors_majorreview`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `majors_userrecommendation`
--
ALTER TABLE `majors_userrecommendation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_choice`
--
ALTER TABLE `tests_choice`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_question`
--
ALTER TABLE `tests_question`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_questioncategory`
--
ALTER TABLE `tests_questioncategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_testcategory`
--
ALTER TABLE `tests_testcategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_testquestion`
--
ALTER TABLE `tests_testquestion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_testresult`
--
ALTER TABLE `tests_testresult`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tests_useranswer`
--
ALTER TABLE `tests_useranswer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- قيود الجداول المُلقاة.
--

--
-- قيود الجداول `accounts_notification`
--
ALTER TABLE `accounts_notification`
  ADD CONSTRAINT `accounts_notification_user_id_30e6cfc5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `accounts_userprofile`
--
ALTER TABLE `accounts_userprofile`
  ADD CONSTRAINT `accounts_userprofile_user_id_92240672_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `advisor_aiconversation`
--
ALTER TABLE `advisor_aiconversation`
  ADD CONSTRAINT `advisor_aiconversation_user_id_1e488b72_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `advisor_aimessage`
--
ALTER TABLE `advisor_aimessage`
  ADD CONSTRAINT `advisor_aimessage_conversation_id_1aca98c5_fk_advisor_a` FOREIGN KEY (`conversation_id`) REFERENCES `advisor_aiconversation` (`id`);

--
-- قيود الجداول `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- قيود الجداول `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- قيود الجداول `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `majors_book`
--
ALTER TABLE `majors_book`
  ADD CONSTRAINT `majors_book_major_id_7c45f28c_fk_majors_major_id` FOREIGN KEY (`major_id`) REFERENCES `majors_major` (`id`);

--
-- قيود الجداول `majors_course`
--
ALTER TABLE `majors_course`
  ADD CONSTRAINT `majors_course_major_id_d33e62bf_fk_majors_major_id` FOREIGN KEY (`major_id`) REFERENCES `majors_major` (`id`);

--
-- قيود الجداول `majors_major`
--
ALTER TABLE `majors_major`
  ADD CONSTRAINT `majors_major_category_id_97c97915_fk_majors_majorcategory_id` FOREIGN KEY (`category_id`) REFERENCES `majors_majorcategory` (`id`);

--
-- قيود الجداول `majors_majorreview`
--
ALTER TABLE `majors_majorreview`
  ADD CONSTRAINT `majors_majorreview_major_id_79bd284b_fk_majors_major_id` FOREIGN KEY (`major_id`) REFERENCES `majors_major` (`id`),
  ADD CONSTRAINT `majors_majorreview_user_id_32e91ded_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `majors_userrecommendation`
--
ALTER TABLE `majors_userrecommendation`
  ADD CONSTRAINT `majors_userrecommendation_major_id_1a0fe3ac_fk_majors_major_id` FOREIGN KEY (`major_id`) REFERENCES `majors_major` (`id`),
  ADD CONSTRAINT `majors_userrecommendation_user_id_266351d9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `tests_choice`
--
ALTER TABLE `tests_choice`
  ADD CONSTRAINT `tests_choice_question_id_b35df5fe_fk_tests_question_id` FOREIGN KEY (`question_id`) REFERENCES `tests_question` (`id`);

--
-- قيود الجداول `tests_question`
--
ALTER TABLE `tests_question`
  ADD CONSTRAINT `tests_question_category_id_77224b3b_fk_tests_questioncategory_id` FOREIGN KEY (`category_id`) REFERENCES `tests_questioncategory` (`id`);

--
-- قيود الجداول `tests_testquestion`
--
ALTER TABLE `tests_testquestion`
  ADD CONSTRAINT `tests_testquestion_category_id_8bccc9d9_fk_tests_testcategory_id` FOREIGN KEY (`category_id`) REFERENCES `tests_testcategory` (`id`);

--
-- قيود الجداول `tests_testresult`
--
ALTER TABLE `tests_testresult`
  ADD CONSTRAINT `tests_testresult_test_category_id_53e675b2_fk_tests_tes` FOREIGN KEY (`test_category_id`) REFERENCES `tests_testcategory` (`id`),
  ADD CONSTRAINT `tests_testresult_user_id_b9595301_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- قيود الجداول `tests_useranswer`
--
ALTER TABLE `tests_useranswer`
  ADD CONSTRAINT `tests_useranswer_question_id_2a91e6d6_fk_tests_testquestion_id` FOREIGN KEY (`question_id`) REFERENCES `tests_testquestion` (`id`),
  ADD CONSTRAINT `tests_useranswer_test_result_id_e462c9fd_fk_tests_testresult_id` FOREIGN KEY (`test_result_id`) REFERENCES `tests_testresult` (`id`),
  ADD CONSTRAINT `tests_useranswer_user_id_10967465_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
