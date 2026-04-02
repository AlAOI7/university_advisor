# tests/urls.py
from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('personality/', views.personality_test_view, name='personality_test'),
    path('submit/', views.submit_test_view, name='submit_test'),
    path('results/<int:result_id>/', views.test_results_view, name='test_results'),
    
    path('', views.test_view, name='test_home'),
]