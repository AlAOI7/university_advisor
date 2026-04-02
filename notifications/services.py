# notifications/services.py

from django.utils import timezone
from .models import Notification
from tests.models import TestResult
from majors.models import Major

class NotificationService:
    @staticmethod
    def send_test_result_notification(user, test_result):
        """إرسال إشعار بنتيجة الاختبار"""
        notification = Notification.objects.create(
            user=user,
            notification_type='test_result',
            title='🎉 نتائج اختبارك جاهزة!',
            message=f'تم تحليل إجاباتك واقتراح {len(test_result.recommended_majors.split(","))} تخصصات مناسبة لك.',
            link=f'/tests/results/{test_result.id}/'
        )
        return notification
    
    @staticmethod
    def send_major_update_notification(users, major, update_type):
        """إرسال إشعارات بتحديث تخصص"""
        notifications = []
        for user in users:
            notification = Notification.objects.create(
                user=user,
                notification_type='major_update',
                title=f'📢 تحديث في تخصص {major.name}',
                message=f'تم {update_type} في التخصص الذي اهتممت به سابقاً.',
                link=f'/majors/{major.id}/'
            )
            notifications.append(notification)
        return notifications
    
    @staticmethod
    def send_reminder_notification(user, message, link=None):
        """إرسال إشعار تذكير"""
        notification = Notification.objects.create(
            user=user,
            notification_type='reminder',
            title='⏰ تذكير مهم',
            message=message,
            link=link
        )
        return notification
    
    @staticmethod
    def get_unread_count(user):
        """الحصول على عدد الإشعارات غير المقروءة"""
        return Notification.objects.filter(user=user, is_read=False).count()
    
    @staticmethod
    def mark_all_as_read(user):
        """تحديد جميع الإشعارات كمقروءة"""
        Notification.objects.filter(user=user, is_read=False).update(is_read=True)
    
    @staticmethod
    def create_weekly_summary(user):
        """إنشاء ملخص أسبوعي"""
        last_week = timezone.now() - timezone.timedelta(days=7)
        
        tests_taken = TestResult.objects.filter(
            user=user,
            completed_at__gte=last_week
        ).count()
        
        majors_explored = user.majorexploration_set.filter(
            viewed_at__gte=last_week
        ).count()
        
        message = f"""
        ملخص أسبوعك:
        • عدد الاختبارات: {tests_taken}
        • التخصصات المستكشفة: {majors_explored}
        • متوسط نسبة المطابقة: {user.statistics.average_match_percentage:.1f}%
        
        استمر في استكشاف التخصصات المناسبة لك! 🚀
        """
        
        notification = Notification.objects.create(
            user=user,
            notification_type='system',
            title='📊 ملخص أسبوعك',
            message=message,
            link='/profile/'
        )
        
        return notification