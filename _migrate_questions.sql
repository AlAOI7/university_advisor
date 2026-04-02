-- Migrate questions from old 'questions' table to Django ORM tables
SET FOREIGN_KEY_CHECKS=0;

-- Step 1: Create question categories from the old questions types
INSERT IGNORE INTO tests_questioncategory (name, description)
VALUES
  ('Academic Interests', 'Questions about academic subjects and learning style'),
  ('Skills & Strengths', 'Questions about personal skills and strengths'),
  ('Personality & Work Style', 'Questions about personality and preferred work environment'),
  ('Career & Goals', 'Questions about career aspirations and future goals');

-- Step 2: Migrate questions from old 'questions' table into tests_question
-- Map question_type to category:
-- 'subject' -> category 1, 'skill' -> 2, 'interest' -> 2, 
-- 'strength' -> 2, 'personality' -> 3

INSERT IGNORE INTO tests_question (text, `order`, category_id)
SELECT 
    question_text,
    id,
    CASE question_type
        WHEN 'subject'     THEN 1
        WHEN 'interest'    THEN 1
        WHEN 'skill'       THEN 2
        WHEN 'strength'    THEN 2
        WHEN 'personality' THEN 3
        ELSE 1
    END
FROM questions
WHERE id NOT IN (SELECT id FROM tests_question);

-- Step 3: For each question in tests_question that has no choices, 
-- create choices from the JSON options in the old questions table
-- (This requires the options column from old questions table)
-- We'll create TestCategory entries used by TestResult

INSERT IGNORE INTO tests_testcategory (name, description)
VALUES
    ('Personality Assessment', 'A comprehensive personality and career interest assessment test'),
    ('Skills Evaluation', 'Skills and strengths evaluation test'),
    ('Career Guidance', 'Career path guidance assessment');

SET FOREIGN_KEY_CHECKS=1;

SELECT 'Questions migrated:', COUNT(*) FROM tests_question;
SELECT 'Categories created:', COUNT(*) FROM tests_questioncategory;
SELECT 'Test categories:', COUNT(*) FROM tests_testcategory;
