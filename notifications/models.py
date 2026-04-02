# notifications/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('test_result', 'نتيجة اختبار'),
        ('major_update', 'تحديث تخصص'),
        ('new_course', 'دورة جديدة'),
        ('system', 'إشعار نظام'),
        ('reminder', 'تذكير'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.title}"
    
    def mark_as_read(self):
        self.is_read = True
        self.save()

class UserStatistic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='statistics')
    total_tests_taken = models.IntegerField(default=0)
    majors_explored = models.IntegerField(default=0)
    courses_viewed = models.IntegerField(default=0)
    average_match_percentage = models.FloatField(default=0)
    last_active = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} Statistics"