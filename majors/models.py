# majors/models.py
from django.db import models

class MajorCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, default='fas fa-folder')
    
    class Meta:
        db_table = 'majors_majorcategory'
        verbose_name = 'Major Category'
        verbose_name_plural = 'Major Categories'
    
    def __str__(self):
        return self.name

class Major(models.Model):
    LEVEL_CHOICES = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('phd', 'PhD'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(MajorCategory, on_delete=models.CASCADE, related_name='majors')
    description = models.TextField()
    duration = models.CharField(max_length=50)
    requirements = models.TextField(blank=True, null=True)
    job_opportunities = models.TextField()
    average_salary = models.CharField(max_length=100)
    demand_level = models.CharField(max_length=50)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='bachelor')
    universities = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'majors_major'
    
    def __str__(self):
        return self.name

class Course(models.Model):
    TYPE_CHOICES = [
        ('free', 'Free'),
        ('paid', 'Paid'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    platform = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='free')
    language = models.CharField(max_length=50, default='Arabic')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'majors_course'
    
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    download_url = models.URLField()
    pages = models.IntegerField(default=0)
    format = models.CharField(max_length=10, default='pdf')
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'majors_book'
    
    def __str__(self):
        return self.title

class MajorReview(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'majors_majorreview'
        unique_together = ['user', 'major']
    
    def __str__(self):
        return f"{self.user.username} - {self.major.name} - {self.rating} stars"

class UserRecommendation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='recommendations')
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='user_recommendations')
    match_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'majors_userrecommendation'
        ordering = ['-match_percentage']
    
    def __str__(self):
        return f"{self.user.username} - {self.major.name} ({self.match_percentage}%)"