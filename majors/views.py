# majors/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Major, MajorCategory, Course, Book, MajorReview, UserRecommendation

def catalog(request):
    """عرض جميع التخصصات مع دعم الفلترة والبحث"""
    from django.db.models import Q

    majors = Major.objects.all().select_related('category')
    categories = MajorCategory.objects.all()

    search_query = request.GET.get('search', '').strip()
    category_id = request.GET.get('category', '').strip()
    selected_category = None

    if search_query:
        majors = majors.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(job_opportunities__icontains=search_query)
        )

    if category_id:
        try:
            selected_category = MajorCategory.objects.get(id=int(category_id))
            majors = majors.filter(category=selected_category)
        except (MajorCategory.DoesNotExist, ValueError):
            pass

    context = {
        'majors': majors,
        'categories': categories,
        'search_query': search_query,
        'selected_category': selected_category,
        'title': 'دليل التخصصات',
    }
    return render(request, 'majors/catalog.html', context)

def courses_books(request):
    """عرض الدورات والكتب مع دعم الفلترة والبحث"""
    from django.db.models import Q

    # ── Courses filtering ──────────────────────────────────────
    courses = Course.objects.all().select_related('major')

    course_search   = request.GET.get('course_search', '').strip()
    platform_filter = request.GET.get('platform', '').strip()
    type_filter     = request.GET.get('type', '').strip()
    language_filter = request.GET.get('language', '').strip()

    if course_search:
        courses = courses.filter(
            Q(title__icontains=course_search) |
            Q(description__icontains=course_search)
        )
    if platform_filter:
        courses = courses.filter(platform__icontains=platform_filter)
    if type_filter:
        courses = courses.filter(type=type_filter)
    if language_filter:
        courses = courses.filter(language__icontains=language_filter)

    # ── Books filtering ────────────────────────────────────────
    books = Book.objects.all().select_related('major')

    book_search = request.GET.get('book_search', '').strip()

    if book_search:
        books = books.filter(
            Q(title__icontains=book_search) |
            Q(author__icontains=book_search) |
            Q(description__icontains=book_search)
        )

    context = {
        'courses': courses,
        'books': books,
        'course_search': course_search,
        'platform_filter': platform_filter,
        'type_filter': type_filter,
        'language_filter': language_filter,
        'book_search': book_search,
        'active_tab': 'books' if book_search and not (course_search or platform_filter or type_filter or language_filter) else 'courses',
        'title': 'الدورات والكتب',
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
        rating = request.POST.get('rating', '').strip()
        review_text = request.POST.get('review_text', '').strip()

        # Validate rating: must be a non-empty integer between 1 and 5
        try:
            rating_int = int(rating)
            if not (1 <= rating_int <= 5):
                raise ValueError("Rating out of range")
        except (ValueError, TypeError):
            from django.contrib import messages
            messages.error(request, "الرجاء اختيار تقييم صحيح من 1 إلى 5.")
            return redirect('majors:major_detail', major_id=major_id)

        MajorReview.objects.update_or_create(
            user=request.user,
            major=major,
            defaults={'rating': rating_int, 'review_text': review_text}
        )

        from django.contrib import messages
        messages.success(request, "تم حفظ تقييمك بنجاح.")
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