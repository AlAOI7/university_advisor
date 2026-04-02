from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=200, blank=True)
    grade = models.CharField(max_length=50, blank=True)

    # Test Results
    personality_type = models.CharField(max_length=50, blank=True)
    strengths = models.TextField(blank=True)
    interests = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Profile"


# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# UserProfile Model (Additional/Legacy)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    high_school_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    interests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts_userprofile'

    def __str__(self):
        return self.user.username


# ── Signals ────────────────────────────────────────────────────────────────

@receiver(post_save, sender=User)
def create_user_profiles(sender, instance, created, **kwargs):
    """Create Profile and UserProfile when a new user is created."""
    if created:
        Profile.objects.get_or_create(user=instance)
        UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profiles(sender, instance, **kwargs):
    """Save Profile and UserProfile - create them if they do not exist yet."""
    Profile.objects.get_or_create(user=instance)
    UserProfile.objects.get_or_create(user=instance)