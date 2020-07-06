from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'user']
        fields = ['image', 'image_name', 'caption']