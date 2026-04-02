# تعليمات إعداد قاعدة MySQL للمرشد الجامعي

## الوضع الحالي

- ✅ النظام يعمل حالياً على SQLite
- ✅ قاعدة MySQL جاهزة ومعدة
- ✅ ملف استعلامات SQL جاهز (`insert_data.sql`)
- ⚠️ يحتاج تثبيت pymysql أو mysqlclient للاتصال بـ MySQL

## خطوات التبديل إلى MySQL

### 1. تثبيت مكتبة الاتصال بـ MySQL

قم بتفعيل الاتصال بالإنترنت ثم شغّل:

```bash
pip install pymysql
```

**أو** إذا فشل pymysql:

```bash
pip install mysqlclient
```

### 2. تنفيذ استعلامات البيانات

افتح phpMyAdmin على `http://localhost/phpmyadmin` ثم:

1. اختر قاعدة `university_advisor`
2. اضغط على تبويب SQL
3. افتح الملف `insert_data.sql` وانسخ محتواه
4. الصق الاستعلامات في phpMyAdmin
5. اضغط "Go/تنفيذ"

سيتم إضافة:

- **10 تخصصات** شاملة (حاسب، طب، هندسة، إدارة، تصميم، إلخ)
- **20 سؤال** متنوع للاختبار
- **15 دورة تدريبية** من منصات مختلفة
- **15 كتاب** في مجالات متنوعة

### 3. تفعيل MySQL في Django

افتح الملف `university_advisor/settings.py`:

```python
# احذف أو علّق إعدادات SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# فعّل إعدادات MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'university_advisor',
        'USER': 'root',
        'PASSWORD': '',  # كلمة مرور فارغة في XAMPP
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
```

### 4. تشغيل السيرفر

```bash
python manage.py runserver
```

## التحقق من نجاح التبديل

قم بزيارة:

- `http://127.0.0.1:8000/majors/` - يجب أن ترى 10 تخصصات
- `http://127.0.0.1:8000/tests/` - صفحة الاختبار مع 20 سؤال

## حل المشاكل الشائعة

### مشكلة: `No module named 'pymysql'`

**الحل**: قم بتثبيت pymysql:

```bash
pip install pymysql
```

### مشكلة: `Access denied for user 'root'@'localhost'`

**الحل**: تحقق من كلمة مرور MySQL في `settings.py`

### مشكلة: `Unknown database 'university_advisor'`

**الحل**: أنشئ القاعدة يدوياً:

```sql
CREATE DATABASE university_advisor CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### مشكلة: الجداول فارغة

**الحل**: نفذ استعلامات `insert_data.sql` في phpMyAdmin

## نصيحة للمستقبل

- احتفظ بملف `insert_data.sql` للرجوع إليه
- قم بعمل نسخة احتياطية من القاعدة بانتظام
- لنقل البيانات من SQLite إلى MySQL، استخدم:
  ```bash
  python manage.py dumpdata > data.json
  # ثم بعد التبديل لـ MySQL
  python manage.py loaddata data.json
  ```

## الملفات المهمة

- `insert_data.sql` - استعلامات إضافة البيانات الافتراضية
- `university_advisor_full.sql` - الملف الكامل لإنشاء القاعدة مع البيانات
- `settings.py` - إعدادات قاعدة البيانات

## الدعم

إذا واجهت أي مشاكل:

1. تأكد من تشغيل XAMPP وخدمة MySQL
2. تحقق من منفذ 3306 غير مستخدم من برنامج آخر
3. جرب إعادة تشغيل XAMPP
