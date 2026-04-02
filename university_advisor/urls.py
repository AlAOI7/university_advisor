from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from advisor import views as advisor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', advisor_views.home, name='home'),
    path('about/', advisor_views.about, name='about'),
    path('accounts/', include('accounts.urls')),
    path('majors/', include('majors.urls')),
    path('tests/', include('tests.urls')),
    
    # Global auth URLs (so {% url 'login' %} works without namespace)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]