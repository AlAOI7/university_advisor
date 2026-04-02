# api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile
from majors.models import Major, MajorReview, Course, Book
from tests.models import TestResult, Question, Choice
from notifications.models import Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'

class MajorReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    major_name = serializers.CharField(source='major.name', read_only=True)
    
    class Meta:
        model = MajorReview
        fields = ['id', 'user', 'major', 'major_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

class MajorSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    is_recommended = serializers.SerializerMethodField()
    
    class Meta:
        model = Major
        fields = '__all__'
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum(r.rating for r in reviews) / reviews.count()
        return 0
    
    def get_review_count(self, obj):
        return obj.reviews.count()
    
    def get_is_recommended(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return UserRecommendation.objects.filter(
                user=request.user,
                major=obj
            ).exists()
        return False

class TestResultSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    recommended_majors_list = serializers.SerializerMethodField()
    
    class Meta:
        model = TestResult
        fields = '__all__'
        read_only_fields = ['user', 'completed_at']
    
    def get_recommended_majors_list(self, obj):
        return [m.strip() for m in obj.recommended_majors.split(',') if m.strip()]

class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'category', 'order', 'choices']
    
    def get_choices(self, obj):
        choices = obj.choices.all()
        return ChoiceSerializer(choices, many=True).data

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'value', 'personality_traits']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)
    conversation_id = serializers.IntegerField(required=False)

class ComparisonSerializer(serializers.Serializer):
    major1_id = serializers.IntegerField()
    major2_id = serializers.IntegerField()

class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField(required=False, max_length=1000)