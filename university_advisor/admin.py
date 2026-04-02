# university_advisor/admin.py
from django.contrib import admin
from django.contrib.admin import AdminSite

class UniversityAdminSite(AdminSite):
    site_header = "University Advisor Admin"
    site_title = "University Advisor Management"
    index_title = "Welcome to the Admin Dashboard"
    
    def has_permission(self, request):
        """
        Only users with is_staff permission can access the admin panel.
        """
        return request.user.is_active and request.user.is_staff

# Replace the default site
admin_site = UniversityAdminSite(name='admin')
