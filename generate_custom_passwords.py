import hashlib
import json

print("=" * 70)
print("مولد كلمات المرور المشفرة - لجدول users المخصص")
print("=" * 70)

users = {
    'student': '123456',
    'admin': 'admin123',
    'test': 'test123',
    'ahmed': '123456',
    'sara': '123456'
}

print("\n1️⃣  كلمات المرور بـ MD5 (بسيط - للتطوير):")
print("-" * 70)
for username, password in users.items():
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    print(f"{username:10} / {password:12} => {md5_hash}")

print("\n2️⃣  كلمات المرور بـ SHA256 (أفضل لل��نتاج):")
print("-" * 70)
for username, password in users.items():
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"{username:10} / {password:12}")
    print(f"           => {sha256_hash}")

print("\n3️⃣  مثال على JSON للـ ai_analysis:")
print("-" * 70)
ai_analysis = {
    "personality_type": "محلل منطقي",
    "learning_style": "بصري وعملي",
    "work_environment": "مكتب تقني هادئ",
    "strengths": ["التفكير المنطقي", "حل المشكلات", "الدقة"],
    "interests": ["البرمجة", "الرياضيات", "التكنولوجيا"],
    "recommendations": [
        {
            "major": "علوم الحاسب",
            "match_percentage": 95,
            "reason": "يتناسب مع مهاراتك التحليلية"
        },
        {
            "major": "هندسة البرمجيات",
            "match_percentage": 90,
            "reason": "مناسب لحل المشكلات"
        }
    ],
    "career_path": "مطور برمجيات، مهندس بيانات، محلل أنظمة",
    "considerations": "قد تحتاج لتطوير مهارات التواصل"
}

print(json.dumps(ai_analysis, ensure_ascii=False, indent=2))

print("\n" + "=" * 70)
print("✅ تم! استخدم القيم أعلاه في استعلامات SQL")
print("📝 ملاحظة: لـ bcrypt، نفذ: pip install bcrypt")
print("=" * 70)
