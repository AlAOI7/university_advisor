"""
Data migration script: transfers data from old tables to Django ORM tables.
Run with: python migrate_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from django.db import connection, transaction

def run():
    print("=" * 60)
    print("Starting data migration...")
    print("=" * 60)

    with transaction.atomic():

        # ─── 1. Categories (from old majors categories) ───────────────
        print("\n[1] Creating major categories...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM majors_majorcategory")
            existing = cursor.fetchone()[0]

        if existing == 0:
            categories_sql = """
            INSERT INTO majors_majorcategory (name, description, icon) VALUES
            ('Engineering & Technology', 'Engineering and technical fields', 'fas fa-cogs'),
            ('Medicine & Health', 'Medical and health-related fields', 'fas fa-heartbeat'),
            ('Business & Management', 'Business and administrative fields', 'fas fa-briefcase'),
            ('Science & Research', 'Pure and applied sciences', 'fas fa-flask'),
            ('Arts & Design', 'Creative and design fields', 'fas fa-palette'),
            ('Social Sciences', 'Social and human sciences', 'fas fa-users'),
            ('Law & Politics', 'Law and political science fields', 'fas fa-balance-scale'),
            ('Computer Science', 'Computing and information technology', 'fas fa-laptop-code')
            """
            with connection.cursor() as cursor:
                cursor.execute(categories_sql)
            print("  ✓ 8 categories created.")
        else:
            print(f"  ✓ Categories already exist ({existing} found).")

        # Build category name → id map
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name FROM majors_majorcategory")
            cat_rows = cursor.fetchall()
        cat_map = {name: id_ for id_, name in cat_rows}

        # ─── 2. Majors (from old `majors` table) ──────────────────────
        print("\n[2] Migrating majors...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM majors_major")
            existing = cursor.fetchone()[0]

        if existing == 0:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, name_ar, name_en, description, required_skills, career_opportunities, difficulty_level, demand_level, salary_range, image_url FROM majors")
                old_majors = cursor.fetchall()

            def get_category_id(name_en):
                name_lower = (name_en or '').lower()
                if any(w in name_lower for w in ['engineering', 'mechanical', 'electrical', 'civil']):
                    return cat_map.get('Engineering & Technology', 1)
                elif any(w in name_lower for w in ['medicine', 'medical', 'pharmacy', 'nursing', 'dental']):
                    return cat_map.get('Medicine & Health', 2)
                elif any(w in name_lower for w in ['business', 'management', 'accounting', 'marketing', 'finance']):
                    return cat_map.get('Business & Management', 3)
                elif any(w in name_lower for w in ['science', 'physics', 'chemistry', 'biology', 'math']):
                    return cat_map.get('Science & Research', 4)
                elif any(w in name_lower for w in ['design', 'art', 'graphic', 'architecture']):
                    return cat_map.get('Arts & Design', 5)
                elif any(w in name_lower for w in ['psychology', 'social', 'political', 'sociology']):
                    return cat_map.get('Social Sciences', 6)
                elif any(w in name_lower for w in ['law', 'legal']):
                    return cat_map.get('Law & Politics', 7)
                elif any(w in name_lower for w in ['computer', 'software', 'information', 'it', 'ai']):
                    return cat_map.get('Computer Science', 8)
                return 1

            inserted = 0
            with connection.cursor() as cursor:
                for row in old_majors:
                    id_, name_ar, name_en, description, skills, careers, difficulty, demand, salary, image = row
                    name = name_en or name_ar or 'Unknown'
                    cat_id = get_category_id(name_en)
                    description = description or ''
                    duration = '4 years'
                    requirements = skills or ''
                    job_opportunities = careers or ''
                    average_salary = salary or 'Competitive'
                    demand_level = demand or 'medium'
                    cursor.execute("""
                        INSERT INTO majors_major
                        (name, category_id, description, duration, requirements, job_opportunities,
                         average_salary, demand_level, level, universities, image_url, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
                    """, [name, cat_id, description, duration, requirements,
                          job_opportunities, average_salary, demand_level,
                          'bachelor', None, image])
                    inserted += 1
            print(f"  ✓ {inserted} majors migrated.")
        else:
            print(f"  ✓ Majors already exist ({existing} found).")

        # ─── 3. Courses (from old `courses` table) ────────────────────
        print("\n[3] Migrating courses...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM majors_course")
            existing = cursor.fetchone()[0]

        if existing == 0:
            with connection.cursor() as cursor:
                cursor.execute("SELECT title, description, provider, url, duration, difficulty, category FROM courses")
                old_courses = cursor.fetchall()

            inserted = 0
            with connection.cursor() as cursor:
                for row in old_courses:
                    title, description, provider, url, duration, difficulty, category = row
                    course_type = 'free'
                    language = 'Arabic'
                    rating = 4.0
                    cursor.execute("""
                        INSERT INTO majors_course
                        (title, description, url, platform, duration, price, type, language, rating, major_id, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL, NOW())
                    """, [title or 'Untitled', description or '', url or '#',
                          provider or 'Online', duration or 'Self-paced',
                          0, course_type, language, rating])
                    inserted += 1
            print(f"  ✓ {inserted} courses migrated.")
        else:
            print(f"  ✓ Courses already exist ({existing} found).")

        # ─── 4. Books (from old `books` table) ────────────────────────
        print("\n[4] Migrating books...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM majors_book")
            existing = cursor.fetchone()[0]

        if existing == 0:
            with connection.cursor() as cursor:
                cursor.execute("SELECT title, author, description, category, pdf_url, amazon_url FROM books")
                old_books = cursor.fetchall()

            inserted = 0
            with connection.cursor() as cursor:
                for row in old_books:
                    title, author, description, category, pdf_url, amazon_url = row
                    download_url = pdf_url or amazon_url or '#'
                    cursor.execute("""
                        INSERT INTO majors_book
                        (title, author, description, download_url, pages, format, major_id, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s, NULL, NOW())
                    """, [title or 'Untitled', author or 'Unknown',
                          description or '', download_url, 0, 'pdf'])
                    inserted += 1
            print(f"  ✓ {inserted} books migrated.")
        else:
            print(f"  ✓ Books already exist ({existing} found).")

        # ─── 5. Create superuser if no users exist ────────────────────
        print("\n[5] Checking users...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM auth_user")
            user_count = cursor.fetchone()[0]

        if user_count == 0:
            from django.contrib.auth.models import User
            User.objects.create_superuser(
                username='admin',
                email='admin@university.com',
                password='admin123'
            )
            # Also create a test student
            student = User.objects.create_user(
                username='student',
                email='student@university.com',
                password='student123',
                first_name='Test',
                last_name='Student'
            )
            print("  ✓ Created admin (admin/admin123) and student (student/student123)")
        else:
            print(f"  ✓ Users already exist ({user_count} found).")

    print("\n" + "=" * 60)
    print("✅ Migration completed successfully!")
    print("=" * 60)
    print("\nLogin credentials:")
    print("  Admin:   admin / admin123")
    print("  Student: student / student123")


if __name__ == '__main__':
    run()
