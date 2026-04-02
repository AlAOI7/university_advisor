# analytics/tasks.py

from celery import shared_task
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta
from majors.models import Major, MajorReview
from tests.models import TestResult
from accounts.models import Profile

@shared_task
def generate_daily_reports():
    """توليد تقارير يومية"""
    yesterday = timezone.now() - timedelta(days=1)
    
    new_users = User.objects.filter(
        date_joined__gte=yesterday
    ).count()
    
    new_tests = TestResult.objects.filter(
        completed_at__gte=yesterday
    ).count()
    
    new_reviews = MajorReview.objects.filter(
        created_at__gte=yesterday
    ).count()
    
    popular_majors = Major.objects.annotate(
        view_count=Count('majorexploration')
    ).filter(
        majorexploration__viewed_at__gte=yesterday
    ).order_by('-view_count')[:5]
    
    report_data = {
        'date': timezone.now().date(),
        'new_users': new_users,
        'new_tests': new_tests,
        'new_reviews': new_reviews,
        'popular_majors': [
            {'name': m.name, 'views': m.view_count}
            for m in popular_majors
        ],
        'total_users': User.objects.count(),
        'total_tests': TestResult.objects.count(),
        'total_reviews': MajorReview.objects.count(),
    }
    
    save_report_to_database(report_data)
    
    return report_data

@shared_task
def update_user_statistics():
    """تحديث إحصائيات المستخدمين"""
    users = User.objects.all()
    
    for user in users:
        stats, created = UserStatistic.objects.get_or_create(user=user)
        stats.update_test_count()
        stats.update_average_match()
        stats.save()
    
    return f"Updated statistics for {users.count()} users"