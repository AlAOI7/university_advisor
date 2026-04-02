# tests/admin.py
from django.contrib import admin
from .models import (QuestionCategory, Question, Choice,
                     TestCategory, TestResult, UserAnswer, TestQuestion)


# ── Question Category ────────────────────────────────────────────────────────

@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


# ── Choice Inline ────────────────────────────────────────────────────────────

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    fields = ['text', 'value', 'personality_traits']


# ── Question ─────────────────────────────────────────────────────────────────

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'category', 'order']
    list_filter = ['category']
    search_fields = ['text']
    ordering = ['order']
    inlines = [ChoiceInline]


# ── Choice ───────────────────────────────────────────────────────────────────

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'value', 'personality_traits']
    list_filter = ['question__category']
    search_fields = ['text']


# ── Test Category ─────────────────────────────────────────────────────────────

@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


# ── Test Question ─────────────────────────────────────────────────────────────

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'category', 'weight_a', 'weight_b', 'weight_c', 'weight_d']
    list_filter = ['category']
    search_fields = ['text']


# ── User Answer ───────────────────────────────────────────────────────────────

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question_text', 'selected_choice', 'answer', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'question_text']
    readonly_fields = ['created_at']


# ── Test Result ───────────────────────────────────────────────────────────────

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'test_category', 'score', 'recommended_majors', 'created_at']
    list_filter = ['test_category', 'created_at']
    search_fields = ['user__username', 'recommended_majors', 'result_summary']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'