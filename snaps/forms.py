from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Image,Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'user']
        fields = ['image', 'image_name', 'caption']

