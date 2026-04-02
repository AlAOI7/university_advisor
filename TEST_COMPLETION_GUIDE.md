# تعليمات تفصيلية لتشغيل صفحة الاختبار الكاملة

## الملاحظة

صفحة [test_interactive.html](file:///c:/Users/ALAOI/university_advisor/templates/tests/test_interactive.html) الحالية تحتوي فقط على 3 أسئلة من أصل 20.

## الأسئلة المتبقية (4-20)

لإكمال صفحة الاختبار، يجب إضافة الأسئلة التالية:

### السؤال 4: بيئة العمل المفضلة

```html
<div class="question-slide" data-question="4">
  <div class="question-header mb-4">
    <span class="badge bg-danger mb-2">بيئة العمل</span>
    <h4 class="question-text">في أي بيئة تفضل العمل؟</h4>
  </div>
  <div class="options-container">
    <div class="form-check option-card">
      <input
        class="form-check-input"
        type="radio"
        name="q4"
        id="q4a"
        value="office"
        required
      />
      <label class="form-check-label" for="q4a">
        <i class="fas fa-building text-primary me-2"></i>
        <span>المكتب التقليدي</span>
      </label>
    </div>
    <div class="form-check option-card">
      <input
        class="form-check-input"
        type="radio"
        name="q4"
        id="q4b"
        value="field"
      />
      <label class="form-check-label" for="q4b">
        <i class="fas fa-mountain text-success me-2"></i>
        <span>العمل الميداني</span>
      </label>
    </div>
    <div class="form-check option-card">
      <input
        class="form-check-input"
        type="radio"
        name="q4"
        id="q4c"
        value="lab"
      />
      <label class="form-check-label" for="q4c">
        <i class="fas fa-microscope text-info me-2"></i>
        <span>المختبرات والأبحاث</span>
      </label>
    </div>
    <div class="form-check option-card">
      <input
        class="form-check-input"
        type="radio"
        name="q4"
        id="q4d"
        value="remote"
      />
      <label class="form-check-label" for="q4d">
        <i class="fas fa-home text-warning me-2"></i>
        <span>العمل عن بعد</span>
      </label>
    </div>
  </div>
</div>
```

### السؤال 5-20

يجب إضافة 16 سؤال إضافي بنفس الطريقة، تشمل:

- نقاط القوة الرئيسية
- الأنشطة المفضلة
- طريقة حل المشكلات
- مستوى الاهتمام بالتكنولوجيا
- أسلوب التعلم
- القدرة على التعامل مع الضغوط
- مستوى الرغبة في مساعدة الآخرين
- تفضيل العمل الفردي/الجماعي
- مهارة التحدث أمام الجمهور
- عدد ساعات الدراسة اليومية
- الاهتمام بالتفاصيل
- تقبل المخاطرة
- تفضيل الروتين/التنوع
- أهمية المال
- تفضيل القطاع (عام/خاص)
- مدة الدراسة المقبولة

## كيفية الإضافة

1. افتح الملف: `c:\Users\ALAOI\university_advisor\templates\tests\test_interactive.html`
2. ابحث عن السطر 166: `<!-- سأضيف باقي الأسئلة بنفس الطريقة... -->`
3. احذف هذا التعليق واستبدله بباقي الأسئلة
4. استخدم النمط نفسه للأسئلة 1-3

## البديل السريع

بدلاً من إضافة ال17 سؤال يدوياً، يمكنك:

1. تعديل الصفحة لتعمل بـ 3 أسئلة فقط
2. تغيير `const totalQuestions = 20` إلى `const totalQuestions = 3` في السطر 286

هذا سيجعل الصفحة تعمل فوراً بالأسئلة الثلاثة الموجودة.

## خطوة الحل الفوري

افتح الملف وغيّر السطر 286 من:

```javascript
const totalQuestions = 20;
```

إلى:

```javascript
const totalQuestions = 3;
```

سيعمل الاختبار فوراً بـ 3 أسئلة وحفظ تلقائي! ✅
