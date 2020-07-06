from django import forms
from .models import Image, Comment

class NewStatusForm(forms.ModelForm):
    class Meta:
        model = Image
        fields =['image', 'image_caption']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']    