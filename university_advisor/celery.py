# university_advisor/celery.py

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_advisor.settings')

app = Celery('university_advisor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-weekly-summaries': {
        'task': 'notifications.tasks.send_weekly_summaries',
        'schedule': crontab(day_of_week='monday', hour=9, minute=0),
    },
    'update-trending-majors': {
        'task': 'majors.tasks.update_trending_majors',
        'schedule': crontab(hour=0, minute=0),
    },
    'cleanup-old-data': {
        'task': 'core.tasks.cleanup_old_data',
        'schedule': crontab(day_of_month='1', hour=3, minute=0),
    },
    'generate-analytics-reports': {
        'task': 'analytics.tasks.generate_daily_reports',
        'schedule': crontab(hour=23, minute=30),
    },
}