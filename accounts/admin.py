# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, UserProfile, Notification


# ── Inline: show Profile inside User admin ──────────────────────────────────

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    extra = 0
    fields = ['phone_number', 'birth_date', 'city', 'school', 'grade',
              'personality_type', 'strengths', 'interests']

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile (Extended)'
    extra = 0
    fields = ['phone', 'address', 'birth_date', 'high_school_gpa', 'interests']


# ── Custom User Admin ────────────────────────────────────────────────────────

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, UserProfileInline)
    list_display = ['username', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_superuser', 'is_active', 'date_joined']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_inline_instances(self, request, obj=None):
        """Only show inlines for existing users (not on add form)."""
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# ── Profile Admin ────────────────────────────────────────────────────────────

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'school', 'grade', 'personality_type', 'created_at']
    list_filter = ['city', 'grade', 'personality_type']
    search_fields = ['user__username', 'user__email', 'city', 'school']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city_display', 'birth_date', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone']
    readonly_fields = ['created_at', 'updated_at']

    def city_display(self, obj):
        return obj.address or '-'
    city_display.short_description = 'Address'


# ── Notification Admin ───────────────────────────────────────────────────────

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['user__username', 'title', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = 'Mark selected as read'