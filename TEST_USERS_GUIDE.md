# إنشاء مستخدمين تجريبيين - تعليمات خطوة بخطوة

## ⚠️ مهم جداً

**لا تنفذ أوامر Python في PowerShell مباشرة!**
استخدم `python manage.py shell` أولاً.

---

## الطريقة الصحيحة ✅

### الخطوة 1: افتح Django Shell

في PowerShell، اكتب:

```powershell
python manage.py shell
```

ستظهر لك `>>>` - هذا يعني أنك الآن في Python shell.

### الخطوة 2: الصق الكود التالي

```python
from django.contrib.auth.models import User

# حذف المستخدمين القدامى إن وجدوا
User.objects.filter(username__in=['student', 'admin', 'test']).delete()

# إنشاء مستخدم طالب
student = User.objects.create_user(
    username='student',
    email='student@test.com',
    password='123456',
    first_name='محمد',
    last_name='أحمد'
)
print(f'✅ مستخدم: {student.username} / 123456')

# إنشاء مدير النظام
admin = User.objects.create_superuser(
    username='admin',
    email='admin@test.com',
    password='admin123',
    first_name='المدير',
    last_name='العام'
)
print(f'✅ مدير: {admin.username} / admin123')

# إنشاء مستخدم تجريبي
test = User.objects.create_user(
    username='test',
    email='test@test.com',
    password='test123'
)
print(f'✅ تجريبي: {test.username} / test123')

print('\n🎉 تم بنجاح! استخدم أي من الحسابات أعلاه')
```

### الخطوة 3: اضغط Enter

سيتم إنشاء 3 مستخدمين فوراً!

### الخطوة 4: الخروج

اكتب:

```python
exit()
```

---

## بيانات التسجيل الجاهزة 🔑

بعد تنفيذ الكود أعلاه، يمكنك الدخول بـ:

| اسم المستخدم | كلمة المرور | الصلاحية |
| ------------ | ----------- | -------- |
| `student`    | `123456`    | طالب     |
| `admin`      | `admin123`  | مدير     |
| `test`       | `test123`   | تجريبي   |

---

## الطريقة البديلة: إنشاء Superuser يدوياً

في PowerShell:

```powershell
python manage.py createsuperuser
```

ثم أدخل:

- اسم المستخدم: `admin`
- البريد: `admin@test.com`
- كلمة المرور: `admin123` (اكتبها مرتين)

---

## تسجيل الدخول 🚪

1. افتح المتصفح
2. اذهب إلى: http://127.0.0.1:8000/accounts/login/
3. أدخل: `student` و `123456`
4. انقر "دخول"

أو:

للدخول للوحة الإدارة:
http://127.0.0.1:8000/admin/
استخدم: `admin` / `admin123`

---

## التسجيل بحساب جديد 📝

إذا أردت إنشاء حساب جديد:

1. اذهب إلى: http://127.0.0.1:8000/accounts/register/
2. أدخل:
   - **اسم المستخدم** (مطلوب) - مثل: `ahmed`
   - **البريد الإلكتروني** (مطلوب) - مثل: `ahmed@test.com`
   - **كلمة المرور** (6 أحرف على الأقل) - مثل: `123456`
   - **تأكيد كلمة المرور** - نفس الأعلى
   - الاسم الأول والأخير (اختياري)
3. وافق على الشروط
4. انقر "إنشاء حساب"

---

## حل المشاكل الشائعة 🔧

### المشكلة: "This field is required"

**الحل:** تأكد من ملء:

- اسم المستخدم ✓
- البريد الإلكتروني ✓
- كلمة المرور ✓
- تأكيد كلمة المرور ✓

### المشكلة: كلمة المرور ضعيفة

**الحل:** تم تبسيط المتطلبات! الآن فقط 6 أحرف كافية.
مثال: `123456`, `test123`, `password` كلها مقبولة.

### المشكلة: اسم المستخدم موجود

**الحل:** استخدم اسم مستخدم مختلف.

---

## ملاحظة عن MySQL 🗄️

حالياً النظام يعمل على **SQLite** (قاعدة محلية).
لاستخدام MySQL، راجع: [MYSQL_INSTRUCTIONS.md](file:///c:/Users/ALAOI/university_advisor/MYSQL_INSTRUCTIONS.md)

**لكن لا داعي الآن - كل شيء يعمل!** ✅
