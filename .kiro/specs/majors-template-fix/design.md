# وثيقة التصميم

## نظرة عامة

يعالج هذا التصميم مشاكل مساحات أسماء URL وتنظيم القوالب في تطبيق Django. يعاني النظام حالياً من تسجيل غير متسق لمساحات أسماء URL ومشاكل في هيكل دليل القوالب تمنع الوظائف من العمل بشكل صحيح. يتضمن الحل إصلاح تكوين URL وتنظيم القوالب بشكل صحيح وضمان الاستخدام المتسق لمساحات الأسماء في جميع أنحاء التطبيق.

## البنية المعمارية

يتبع التطبيق بنية Django المعيارية MVC مع تطبيقات متعددة (advisor، majors، accounts، tests). يتضمن الإصلاح:

1. **طبقة URL**: التسجيل الصحيح لمساحات الأسماء في التكوين الرئيسي لـ URL
2. **طبقة القوالب**: تنظيم دليل القوالب الصحيح وفقاً لاتفاقيات Django
3. **طبقة العرض**: مراجع مسار القوالب المتسقة في العروض

## Components and Interfaces

### URL Configuration Component
- **Main URLConf** (`university_advisor/urls.py`): Central URL routing with proper namespace inclusion
- **App URLConfs**: Individual app URL patterns with namespace definitions
- **Template URL References**: Consistent namespace usage in templates

### Template Organization Component
- **App-Specific Templates**: Templates organized in `templates/app_name/` directories
- **Shared Templates**: Common templates in the root templates directory
- **Template Inheritance**: Proper base template extension

### View-Template Interface
- **Template Path Resolution**: Views reference templates using correct paths
- **Context Data**: Proper data passing from views to templates
- **URL Reversal**: Consistent URL name usage in views and templates

## Data Models

### URL Pattern Structure
```python
# Main URL Configuration
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advisor.urls', namespace='advisor')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('majors/', include('majors.urls', namespace='majors')),
    path('tests/', include('tests.urls', namespace='tests')),
]

# App URL Configuration
app_name = 'app_name'
urlpatterns = [
    path('pattern/', views.view_name, name='url_name'),
]
```

### Template Directory Structure
```
templates/
├── base.html
├── home.html
├── about.html
├── advisor/
│   ├── chat.html
│   └── contact.html
├── majors/
│   ├── catalog.html
│   ├── major_detail.html
│   └── courses_books.html
├── accounts/
│   ├── login.html
│   └── register.html
└── tests/
    └── test.html
```