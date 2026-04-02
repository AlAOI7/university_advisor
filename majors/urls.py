# majors/urls.py
from django.urls import path
from . import views

app_name = 'majors'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('courses-books/', views.courses_books, name='courses_books'),
    path('<int:major_id>/', views.major_detail, name='major_detail'),
    path('<int:major_id>/review/', views.add_review, name='add_review'),
    path('my-recommendations/', views.my_recommendations, name='my_recommendations'),
]