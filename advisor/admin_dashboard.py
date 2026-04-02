# advisor/admin_dashboard.py

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta
from majors.models import Major, MajorReview
from tests.models import TestResult
from accounts.models import Profile
from django.contrib.auth.models import User

def is_admin_user(user):
    return user.is_staff

@user_passes_test(is_admin_user)
def admin_dashboard(request):
    """لوحة تحكم إدارية متقدمة"""
    
    total_users = User.objects.count()
    new_users_week = User.objects.filter(
        date_joined__gte=timezone.now() - timedelta(days=7)
    ).count()
    active_users = User.objects.filter(
        last_login__gte=timezone.now() - timedelta(days=30)
    ).count()
    
    total_tests = TestResult.objects.count()
    tests_today = TestResult.objects.filter(
        completed_at__date=timezone.now().date()
    ).count()
    
    total_majors = Major.objects.count()
    top_rated_majors = Major.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).filter(avg_rating__isnull=False).order_by('-avg_rating')[:5]
    
    personality_stats = TestResult.objects.values('personality_type').annotate(
        count=Count('id')
    ).order_by('-count')[:5]
    
    recent_activity = TestResult.objects.select_related('user').order_by('-completed_at')[:10]
    
    most_reviewed_majors = Major.objects.annotate(
        review_count=Count('reviews')
    ).filter(review_count__gt=0).order_by('-review_count')[:5]
    
    context = {
        'user_stats': {
            'total': total_users,
            'new_week': new_users_week,
            'active': active_users,
        },
        'test_stats': {
            'total': total_tests,
            'today': tests_today,
        },
        'major_stats': {
            'total': total_majors,
            'top_rated': top_rated_majors,
        },
        'personality_stats': personality_stats,
        'recent_activity': recent_activity,
        'most_reviewed': most_reviewed_majors,
        'total_reviews': MajorReview.objects.count(),
    }
    
    return render(request, 'admin/dashboard.html', context)

@user_passes_test(is_admin_user)
def user_analytics(request):
    """تحليلات المستخدمين"""
    
    city_distribution = Profile.objects.exclude(
        city__isnull=True
    ).exclude(
        city=''
    ).values('city').annotate(
        count=Count('id')
    ).order_by('-count')[:10]
    
    grade_distribution = Profile.objects.exclude(
        grade__isnull=True
    ).exclude(
        grade=''
    ).values('grade').annotate(
        count=Count('id')
    ).order_by('-count')
    
    user_test_counts = TestResult.objects.values(
        'user__username'
    ).annotate(
        test_count=Count('id')
    ).order_by('-test_count')[:10]
    
    context = {
        'city_distribution': city_distribution,
        'grade_distribution': grade_distribution,
        'user_test_counts': user_test_counts,
    }
    
    return render(request, 'admin/user_analytics.html', context)

@user_passes_test(is_admin_user)
def major_analytics(request):
    """تحليلات التخصصات"""
    
    major_review_stats = Major.objects.annotate(
        review_count=Count('reviews'),
        avg_rating=Avg('reviews__rating')
    ).filter(
        review_count__gt=0
    ).order_by('-review_count')[:10]
    
    major_recommendation_stats = []
    majors = Major.objects.all()
    for major in majors:
        recommendation_count = TestResult.objects.filter(
            recommended_majors__contains=major.name
        ).count()
        if recommendation_count > 0:
            major_recommendation_stats.append({
                'major': major,
                'recommendation_count': recommendation_count
            })
    
    major_recommendation_stats.sort(
        key=lambda x: x['recommendation_count'],
        reverse=True
    )[:10]
    
    category_distribution = Major.objects.values(
        'category__name'
    ).annotate(
        count=Count('id')
    ).order_by('-count')
    
    context = {
        'major_review_stats': major_review_stats,
        'major_recommendation_stats': major_recommendation_stats[:10],
        'category_distribution': category_distribution,
    }
    
    return render(request, 'admin/major_analytics.html', context)