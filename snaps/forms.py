from django import forms
from .models import Image,Profile

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        fields = ['bio', 'profile_photo']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'user']
        fields = ['image', 'image_name', 'caption']