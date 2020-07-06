from django import forms
from django.forms import ModelForm, Textarea, IntegerField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Profile,Review

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Required. Please use a valid email address')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','comment','like']

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following']

        
class NewPostForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude=['likes', 'slug','profile', 'posted_at']

class ReviewForm(forms.ModelForm):
    class Meta:

        model = Review
        fields = ('comment',)

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')