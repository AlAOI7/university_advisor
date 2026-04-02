from django.contrib import admin
from .models import University, FAQ, ContactMessage

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'ranking']
    search_fields = ['name', 'location']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'order']
    list_filter = ['category']
    search_fields = ['question']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']