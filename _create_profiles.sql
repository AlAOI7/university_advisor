-- Create missing profiles for all users
SET FOREIGN_KEY_CHECKS=0;

INSERT IGNORE INTO accounts_profile 
    (phone_number, birth_date, city, school, grade, personality_type, strengths, interests, created_at, updated_at, user_id)
SELECT 
    '', NULL, '', '', '', '', '', '', NOW(), NOW(), u.id
FROM auth_user u
WHERE u.id NOT IN (SELECT user_id FROM accounts_profile WHERE user_id IS NOT NULL);

INSERT IGNORE INTO accounts_userprofile 
    (phone, address, birth_date, high_school_gpa, interests, created_at, updated_at, user_id)
SELECT 
    NULL, NULL, NULL, NULL, NULL, NOW(), NOW(), u.id
FROM auth_user u
WHERE u.id NOT IN (SELECT user_id FROM accounts_userprofile WHERE user_id IS NOT NULL);

SET FOREIGN_KEY_CHECKS=1;

SELECT 'Done - Profiles count:', COUNT(*) FROM accounts_profile;
SELECT 'Done - UserProfiles count:', COUNT(*) FROM accounts_userprofile;
