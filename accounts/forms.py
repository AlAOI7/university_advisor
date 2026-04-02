# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email Address',
        help_text='Required - use a valid email address'
    )
    first_name = forms.CharField(
        max_length=100, 
        required=False,  # optional
        label='First Name'
    )
    last_name = forms.CharField(
        max_length=100, 
        required=False,  # optional
        label='Last Name'
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
        }
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'birth_date', 'city', 'school', 'grade']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }