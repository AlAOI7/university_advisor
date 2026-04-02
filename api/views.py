# api/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import *
from majors.models import Major, MajorReview
from tests.models import TestResult
from accounts.models import Profile

class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        major = self.get_object()
        reviews = major.reviews.all()
        serializer = MajorReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        major = self.get_object()
        serializer = RatingSerializer(data=request.data)
        
        if serializer.is_valid():
            rating = serializer.validated_data['rating']
            comment = serializer.validated_data.get('comment', '')
            
            review, created = MajorReview.objects.update_or_create(
                user=request.user,
                major=major,
                defaults={
                    'rating': rating,
                    'comment': comment
                }
            )
            
            return Response({
                'success': True,
                'created': created,
                'review_id': review.id
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def trending(self, request):
        trending_majors = Major.objects.annotate(
            review_count=Count('reviews'),
            avg_rating=Avg('reviews__rating')
        ).filter(review_count__gt=0).order_by('-review_count')[:10]
        
        serializer = self.get_serializer(trending_majors, many=True)
        return Response(serializer.data)

class TestResultViewSet(viewsets.ModelViewSet):
    serializer_class = TestResultSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return TestResult.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['get'])
    def recommendations(self, request, pk=None):
        test_result = self.get_object()
        majors = []
        
        for major_name in test_result.recommended_majors.split(','):
            try:
                major = Major.objects.get(name=major_name.strip())
                majors.append(major)
            except Major.DoesNotExist:
                continue
        
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        user = request.user
        stats = {
            'total_tests': TestResult.objects.filter(user=user).count(),
            'majors_explored': user.majorexploration_set.count(),
            'average_match': user.recommendations.aggregate(
                avg=Avg('match_percentage')
            )['avg'] or 0,
            'personality_type': user.profile.personality_type,
            'last_test_date': TestResult.objects.filter(
                user=user
            ).order_by('-completed_at').first().completed_at if TestResult.objects.filter(user=user).exists() else None
        }
        return Response(stats)

class AIChatAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        
        if serializer.is_valid():
            message = serializer.validated_data['message']
            
            ai_service = AIChatService()
            response = ai_service.get_response(message)
            
            return Response({
                'success': True,
                'response': response['response'],
                'suggested_majors': response['suggested_majors'],
                'follow_up_questions': response['follow_up_questions']
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MajorComparisonAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = ComparisonSerializer(data=request.data)
        
        if serializer.is_valid():
            major1_id = serializer.validated_data['major1_id']
            major2_id = serializer.validated_data['major2_id']
            
            major1 = get_object_or_404(Major, id=major1_id)
            major2 = get_object_or_404(Major, id=major2_id)
            
            comparison_data = self.compare_majors(major1, major2)
            
            return Response({
                'success': True,
                'comparison': comparison_data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def compare_majors(self, major1, major2):
        comparison = {
            'study_duration': self.compare_study_duration(major1, major2),
            'difficulty_level': self.compare_difficulty(major1, major2),
            'job_opportunities': self.compare_job_opportunities(major1, major2),
            'salary_expectation': self.compare_salary(major1, major2),
            'skills_required': self.compare_skills(major1, major2)
        }
        return comparison