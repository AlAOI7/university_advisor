# دليل استخدام نظام الذكاء الاصطناعي - Google Gemini

## نظرة عامة

تم دمج Google Gemini API في نظام المرشد الجامعي لتوفير:

- ✅ توصيات ذكية للتخصصات الجامعية
- ✅ Chatbot متقدم للإجابة على أسئلة الطلاب
- ✅ تحليل شامل لنتائج الاختبار

---

## الإعداد الأولي

### 1. الحصول على Gemini API Key

1. اذهب إلى [Google AI Studio](https://makersuite.google.com/app/apikey)
2. سجل الدخول بحساب Google
3. انقر على "Create API Key"
4. انسخ المفتاح

### 2. تكوين المشروع

1. انسخ ملف `.env.example` إلى `.env`:

   ```bash
   copy .env.example .env
   ```

2. افتح `.env` وأضف مفتاح API:

   ```env
   GEMINI_API_KEY=AIzaSy...your_key_here
   ```

3. ثبت المكتبات المطلوبة:
   ```bash
   pip install -r requirements.txt
   ```

---

## الاستخدام

### نظام التوصيات الذكي

```python
from advisor.ai_service import AIAdvisor

# إنشاء مثيل
advisor = AIAdvisor()

# بيانات المستخدم
user_data = {
    'personality_scores': {
        'تحليلي': 8,
        'إبداعي': 6,
        'اجتماعي': 5
    },
    'interests': {
        'التكنولوجيا': 9,
        'العلوم': 7
    }
}

# الحصول على التحليل والتوصيات
analysis = advisor.analyze_user_profile(user_data)

print(analysis['personality_analysis'])
print(analysis['recommendations'])
print(f"AI Powered: {analysis['ai_powered']}")
```

### Chatbot

```python
from advisor.chat_views import AIChatService

# إنشاء مثيل
chat = AIChatService()

# إرسال رسالة
response = chat.get_response("ما هو أفضل تخصص للبرمجة؟")

print(response['response'])
print(f"AI Powered: {response['ai_powered']}")
```

---

## الميزات

### 1. Fallback Automatic

- ✅ النظام يعمل **بدون API key** (نظام محاكي بسيط)
- ✅ عند إضافة API key، يتحول تلقائياً لاستخدام Gemini
- ✅ لا حاجة لتغيير الكود

### 2. التكاملية

- ✅ يتكامل مع قاعدة البيانات الموجودة
- ✅ يستخدم معلومات التخصصات لتحسين الردود
- ✅ يحفظ سجل المحادثات

### 3. السياق الذكي

- ✅ يستخدم تاريخ المحادثة
- ✅ يأخذ في الاعتبار ملف المستخدم
- ✅ يقترح تخصصات بناءً على السياق

---

## API Endpoints

### 1. الدردشة

**POST** `/advisor/api/chat/`

```json
{
  "message": "ما هو أفضل تخصص لي؟",
  "conversation_id": 123 // optional
}
```

**Response:**

```json
{
  "success": true,
  "conversation_id": 123,
  "response": "بناءً على مهاراتك...",
  "suggested_majors": ["علوم الحاسب", "هندسة البرمجيات"],
  "follow_up_questions": ["هل تفضل..."],
  "ai_powered": true
}
```

### 2. المحادثات

**GET** `/advisor/api/conversations/`

**Response:**

```json
{
  "success": true,
  "conversations": [
    {
      "id": 1,
      "title": "استشارة عن التخصص",
      "updated_at": "2026-02-05 10:30",
      "message_count": 15
    }
  ]
}
```

---

## التخصيص

### تعديل Prompts

افتح `advisor/gemini_service.py`وعدّل الدوال:

```python
def _build_analysis_prompt(self, user_answers):
    # عدّل هنا لتغيير طريقة التحليل
    prompt = f"""
    أنت مستشار أكاديمي...
    {your_custom_instructions}
    """
    return prompt
```

### إضافة وظائف جديدة

```python
class GeminiService:
    def your_new_function(self, data):
        prompt = f"Your custom prompt..."
        response = self.generate_content(prompt)
        return response
```

---

## الاختبار

### اختبار بدون API

```bash
# تأكد من عدم وجود API key
# أو استخدم key خاطئ
python manage.py runserver
```

النظام سيعمل بالنظام المحاكي.

### اختبار مع API

```bash
# أضف API key صحيح في .env
python manage.py runserver
```

النظام سيستخدم Gemini تلقائياً.

---

## استكشاف الأخطاء

### المشكلة: "GEMINI_API_KEY غير مكون"

**الحل:**

1. تأكد من وجود `.env` في مجلد المشروع
2. تحقق من وجود `GEMINI_API_KEY` في الملف
3. أعد تشغيل السيرفر

### المشكلة: "خطأ في تكوين Gemini"

**الحل:**

1. تحقق من صحة API key
2. تأكد من تثبيت `google-generativeai`
3. تحقق من سجلات الأخطاء:
   ```bash
   python manage.py runserver
   ```

### المشكلة: الردود بطيئة

**الحل:**

1. استخدم caching للنتائج المتكررة
2. قلل طول prompts
3. اختر نموذج أسرع (gemini-pro-flash)

---

## التكلفة

### Gemini API Pricing

- **Free Tier:** 60 طلب/دقيقة
- **Paid Tier:** طلبات غير محدودة

**نصيحة:** استخدم Free Tier للتطوير والInternal testing.

---

## الأمان

### ✅ ما قمنا به:

1. مفتاح API مخزن في `.env` (غير مشارك مع git)
2. `.gitignore` يحمي الملفات الحساسة
3. Logging للأخطاء فقط، لا تسجيل للبيانات الحساسة

### ⚠️ توصيات إضافية:

1. لا تشارك `.env` أبداً
2. استخدم API keys مختلفة للتطوير والإنتاج
3. راقب استخدام API بانتظام

---

## الخطوات التالية

### مقترحات لتحسين النظام:

1. **Caching:**
   - حفظ نتائج متكررة لتقليل تكاليف API
2. **Fine-tuning:**
   - تحسين Prompts للحصول على نتائج أفضل
3. **Analytics:**
   - تتبع دقة التوصيات
   - قياس رضا المستخدمين

4. **Multilingual:**
   - دعم اللغة الإنجليزية
   - الترجمة التلقائية

---

## الدعم

### الموارد:

- [Google Gemini Docs](https://ai.google.dev/docs)
- [Django Documentation](https://docs.djangoproject.com/)
- [Project Documentation](../USER_GUIDE.md)

### المساعدة:

للمزيد من المساعدة، راجع الملفات:

- `implementation_plan.md` - الخطة الكاملة
- `task.md` - قائمة المهام
- `walkthrough.md` - شرح التحديثات

---

**آخر تحديث:** 5 فبراير 2026
**الإصدار:** 1.0
