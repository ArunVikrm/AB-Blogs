from django import forms
from django.db.models import fields
from .models import Blog
from blogs import models

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'author' , 'title' , 'thumbnail_image' , 'description' , 'category' , 'body'}