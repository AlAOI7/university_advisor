# majors/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Major, MajorCategory, Course, Book, MajorReview, UserRecommendation

def catalog(request):
    """عرض جميع التخصصات"""
    majors = Major.objects.all().select_related('category')
    categories = MajorCategory.objects.all()
    
    context = {
        'majors': majors,
        'categories': categories,
        'title': 'دليل التخصصات'
    }
    return render(request, 'majors/catalog.html', context)

def courses_books(request):
    """عرض الدورات والكتب"""
    courses = Course.objects.all()[:20]
    books = Book.objects.all()[:20]
    
    context = {
        'courses': courses,
        'books': books,
        'title': 'الدورات والكتب'
    }
    return render(request, 'majors/courses_books.html', context)

def major_detail(request, major_id):
    """تفاصيل تخصص معين"""
    major = get_object_or_404(Major, id=major_id)
    related_courses = Course.objects.filter(major=major)[:5]
    related_books = Book.objects.filter(major=major)[:5]
    reviews = MajorReview.objects.filter(major=major).select_related('user')[:10]
    
    context = {
        'major': major,
        'related_courses': related_courses,
        'related_books': related_books,
        'reviews': reviews,
        'title': major.name
    }
    return render(request, 'majors/major_detail.html', context)

@login_required
def add_review(request, major_id):
    """إضافة مراجعة للتخصص"""
    if request.method == 'POST':
        major = get_object_or_404(Major, id=major_id)
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        
        review, created = MajorReview.objects.update_or_create(
            user=request.user,
            major=major,
            defaults={'rating': rating, 'review_text': review_text}
        )
        
        return redirect('majors:major_detail', major_id=major_id)
    
    return redirect('majors:major_detail', major_id=major_id)

@login_required
def my_recommendations(request):
    """عرض التوصيات الشخصية للمستخدم"""
    recommendations = UserRecommendation.objects.filter(user=request.user).select_related('major')
    
    context = {
        'recommendations': recommendations,
        'title': 'توصياتي'
    }
    return render(request, 'majors/recommendations.html', context)