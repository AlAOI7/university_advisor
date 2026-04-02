# majors/admin.py
from django.contrib import admin
from .models import MajorCategory, Major, Course, Book, MajorReview, UserRecommendation

@admin.register(MajorCategory)
class MajorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'duration', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'type', 'price', 'rating', 'created_at']
    list_filter = ['type', 'platform', 'created_at']
    search_fields = ['title', 'description', 'platform']
    readonly_fields = ['created_at']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'format', 'pages', 'created_at']
    list_filter = ['format', 'created_at']
    search_fields = ['title', 'author', 'description']
    readonly_fields = ['created_at']
    
@admin.register(MajorReview)
class MajorReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'major', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'major__name', 'review_text']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(UserRecommendation)
class UserRecommendationAdmin(admin.ModelAdmin):
    list_display = ['user', 'major', 'match_percentage', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'major__name', 'reason']
    readonly_fields = ['created_at']