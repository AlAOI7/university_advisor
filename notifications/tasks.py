# notifications/tasks.py

from celery import shared_task
from django.utils import timezone
from django.contrib.auth.models import User
from .services import NotificationService
from .models import Notification

@shared_task
def send_weekly_summaries():
    """إرسال ملخصات أسبوعية لجميع المستخدمين"""
    users = User.objects.filter(is_active=True)
    
    for user in users:
        NotificationService.create_weekly_summary(user)
    
    return f"Sent weekly summaries to {users.count()} users"

@shared_task
def send_test_reminders():
    """إرسال تذكير لإعادة الاختبار"""
    three_months_ago = timezone.now() - timezone.timedelta(days=90)
    
    users = User.objects.filter(
        testresult__completed_at__lte=three_months_ago
    ).distinct()
    
    for user in users:
        last_test = user.testresult_set.order_by('-completed_at').first()
        if last_test:
            NotificationService.send_reminder_notification(
                user=user,
                message=f"مرت 3 أشهر منذ آخر اختبار لك. هل تريد إعادة الاختبار لمعرفة التطورات؟",
                link='/tests/'
            )
    
    return f"Sent reminders to {users.count()} users"

@shared_task
def cleanup_old_notifications():
    """تنظيف الإشعارات القديمة"""
    six_months_ago = timezone.now() - timezone.timedelta(days=180)
    
    deleted_count = Notification.objects.filter(
        created_at__lte=six_months_ago,
        is_read=True
    ).delete()[0]
    
    return f"Deleted {deleted_count} old notifications"