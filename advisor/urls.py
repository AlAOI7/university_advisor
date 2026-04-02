from django.urls import path
from . import views, chat_views

app_name = 'advisor'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ai-analysis/', views.ai_analysis_info, name='ai_analysis'),
    path('contact/', views.contact, name='contact'),
    
    path('chat/', views.chat_page, name='chat'),
    
    # API Endpoints
    path('api/chat/', chat_views.chat_with_ai, name='api_chat'),
    path('api/conversations/', chat_views.get_conversations, name='get_conversations'),
]