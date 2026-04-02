"""
Migrate users from old 'users' table to Django's 'auth_user' table.
Run with: python migrate_users.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User

def run():
    print("=" * 50)
    print("Migrating users from old table → auth_user...")
    print("=" * 50)

    # Get all old users
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, username, email, full_name FROM users")
        old_users = cursor.fetchall()

    if not old_users:
        print("No users found in old 'users' table.")
        return

    migrated = 0
    skipped = 0

    for row in old_users:
        old_id, username, email, full_name = row

        # Skip if username already exists in auth_user
        if User.objects.filter(username=username).exists():
            print(f"  ⚠ Skipped (already exists): {username}")
            skipped += 1
            continue

        # Parse full name
        name_parts = (full_name or '').strip().split(' ', 1) if full_name else []
        first_name = name_parts[0] if name_parts else ''
        last_name  = name_parts[1] if len(name_parts) > 1 else ''

        # Create the user with default password = username
        # (since old MD5 passwords can't be converted in Django 5)
        user = User.objects.create_user(
            username=username,
            email=email or '',
            password='123456',   # default password - can be changed later
            first_name=first_name,
            last_name=last_name,
        )

        # Make admin a superuser
        if username in ('admin',):
            user.is_staff = True
            user.is_superuser = True
            user.save()

        migrated += 1
        print(f"  ✓ Migrated: {username} ({email})")

    print()
    print(f"Done! Migrated: {migrated}, Skipped: {skipped}")
    print()
    print("All users now have password: 123456")
    print("They can change it after logging in.")

if __name__ == '__main__':
    run()
