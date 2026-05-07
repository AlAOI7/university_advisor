from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'title': 'Smart University Advisor',
        'features': [
            {'title': 'Personality Test', 'desc': 'Discover your career interests'},
            {'title': 'Majors ', 'desc': 'Browse all university majors'},
            {'title': 'Courses & Books', 'desc': 'Free learning resources'},
            {'title': 'Smart Advisor', 'desc': 'Chat with an AI-powered smart advisor'}
        ]
    }
    return render(request, 'advisor/home.html', context)

def about(request):
    return render(request, 'advisor/about.html', {'title': 'About Us'})

@login_required
def chat_page(request):
    """Chat page with the Smart Advisor"""
    return render(request, 'advisor/chat.html', {
        'title': 'Chat with Smart Advisor'
    })

@login_required
def ai_analysis_info(request):
    """AI Analysis information page"""
    return render(request, 'advisor/ai_info.html', {
        'title': 'AI Analysis'
    })

def contact(request):
    """Contact page"""
    return render(request, 'advisor/contact.html', {
        'title': 'Contact Us'
    })