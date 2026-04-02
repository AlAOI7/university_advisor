# tests/models.py
from django.db import models
from django.contrib.auth.models import User

class TestCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        db_table = 'tests_testcategory'
        verbose_name = 'Test Category'
        verbose_name_plural = 'Test Categories'
    
    def __str__(self):
        return self.name

class TestQuestion(models.Model):
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    weight_a = models.IntegerField(default=1)
    weight_b = models.IntegerField(default=2)
    weight_c = models.IntegerField(default=3)
    weight_d = models.IntegerField(default=4)
    
    class Meta:
        db_table = 'tests_testquestion'
    
    def __str__(self):
        return self.text[:50]

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
    test_category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    result_summary = models.TextField()
    recommended_majors = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tests_testresult'
    
    def __str__(self):
        return f"{self.user.username} - {self.test_category.name}"

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='detail_answers', null=True, blank=True)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='answers', null=True, blank=True)
    question_text = models.TextField(null=True, blank=True)
    selected_choice = models.CharField(max_length=500, null=True, blank=True)
    answer = models.CharField(max_length=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tests_useranswer'
    
    def __str__(self):
        return f"{self.user.username} - {self.question_text[:30] if self.question_text else self.question_id}"

# ====== This second section should be removed or merged ======

class QuestionCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.category.name}: {self.text[:50]}..."

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=300)
    value = models.IntegerField()
    personality_traits = models.CharField(max_length=300, help_text="Personality traits (comma-separated)")
    
    class Meta:
        ordering = ['-value']
    
    def __str__(self):
        return self.text
