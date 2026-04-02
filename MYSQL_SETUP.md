# خطوات إعداد MySQL لمشروع University Advisor

## المتطلبات

1. تشغيل XAMPP وتفعيل MySQL
2. تثبيت mysqlclient: `pip install mysqlclient`

## الخطوات

### 1. إنشاء قاعدة البيانات

افتح phpMyAdmin عبر: `http://localhost/phpmyadmin/`

أو استخدم سطر أوامر MySQL:

```bash
mysql -u root -p
```

ثم نفذ الأوامر التالية:

```sql
CREATE DATABASE IF NOT EXISTS university_advisor
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

أو استخدم الملف الجاهز:

```bash
mysql -u root < create_database.sql
```

### 2. تثبيت mysqlclient

```bash
pip install mysqlclient
```

**ملاحظة**: إذا واجهت مشاكل في التثبيت على Windows، يمكنك:

- تحميل wheel من: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
- أو استخدم: `pip install pymysql` ثم أضف في `__init__.py`:
  ```python
  import pymysql
  pymysql.install_as_MySQLdb()
  ```

### 3. تشغيل الترحيلات

```bash
python manage.py migrate
```

### 4. إنشاء البيانات الأولية

```bash
python manage.py createsuperuser
python create_initial_data.py
```

### 5. تشغيل المشروع

```bash
python manage.py runserver
```

## التحقق من الاتصال

```bash
python manage.py dbshell
```

إذا نجح الاتصال، ستدخل إلى سطر أوامر MySQL.

## في حالة المشاكل

إذا واجهت مشاكل، يمكنك العودة مؤقتاً لـ SQLite بتعديل `settings.py`:

- علّق على إعدادات MySQL
- ألغِ التعليق عن إعدادات SQLite
