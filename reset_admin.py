"""
Reset admin password directly - no Django DB connection needed for hash generation.
"""
import os
import sys
import hashlib
import base64
import secrets
import subprocess

def make_pbkdf2_hash(password, iterations=260000):
    """Generate Django-compatible PBKDF2 SHA256 hash."""
    salt = secrets.token_urlsafe(16)
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
    hash_b64 = base64.b64encode(dk).decode()
    return f"pbkdf2_sha256${iterations}${salt}${hash_b64}"

# New admin credentials
NEW_USERNAME = "superadmin"
NEW_EMAIL    = "dotnetala@gmail.com"
NEW_PASSWORD = "Admin@2026"
NEW_FIRST    = "Super"
NEW_LAST     = "Admin"

hashed = make_pbkdf2_hash(NEW_PASSWORD)
print(f"Generated hash: {hashed[:40]}...")

# Build the MySQL command to insert/update admin
sql = f"""
SET FOREIGN_KEY_CHECKS=0;

-- Update existing admin password
UPDATE auth_user SET
    password='{hashed}',
    is_staff=1,
    is_superuser=1,
    is_active=1,
    email='{NEW_EMAIL}'
WHERE username='admin';

-- Check if superadmin already exists; if not insert it
INSERT IGNORE INTO auth_user
    (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES
    ('{hashed}', NULL, 1, '{NEW_USERNAME}', '{NEW_FIRST}', '{NEW_LAST}', '{NEW_EMAIL}', 1, 1, NOW());

SET FOREIGN_KEY_CHECKS=1;
SELECT id, username, email, is_superuser, is_staff FROM auth_user WHERE is_superuser=1;
"""

# Write to a temp SQL file to avoid shell escaping issues
sql_file = os.path.join(os.path.dirname(__file__), '_reset_admin_tmp.sql')
with open(sql_file, 'w', encoding='utf-8') as f:
    f.write(sql)

mysql_path = r'C:\xampp\mysql\bin\mysql.exe'
cmd = [mysql_path, '-u', 'root', '--connect-timeout=5', 'university_advisor']

try:
    result = subprocess.run(
        cmd,
        input=open(sql_file, 'rb').read(),
        capture_output=True,
        timeout=10
    )
    output = result.stdout.decode('utf-8', errors='replace')
    errors = result.stderr.decode('utf-8', errors='replace')

    if result.returncode == 0:
        print("\n✅ Admin credentials updated successfully!")
        print(f"\nAdmin users in database:")
        print(output)
        print(f"\n{'='*45}")
        print(f"  Username : admin")
        print(f"  Password : Admin@2026")
        print(f"  URL      : http://127.0.0.1:8000/admin/")
        print(f"{'='*45}")
        print(f"\n  Username : superadmin  (new)")
        print(f"  Password : Admin@2026")
        print(f"  URL      : http://127.0.0.1:8000/admin/")
        print(f"{'='*45}")
    else:
        print(f"❌ MySQL error: {errors}")
finally:
    if os.path.exists(sql_file):
        os.remove(sql_file)
