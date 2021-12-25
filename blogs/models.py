from django.db import models
from django.conf import settings
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=255,null=False,blank=False)
    slug = models.SlugField(max_length=300,null=True,blank=True)
    thumbnail_image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=255,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    body = RichTextField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def favourite_count(self):
        count = self.favourite_set.all().count()
        return count

class Favourite(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=False)
    blog =  models.ForeignKey(Blog,on_delete=models.CASCADE,null=False)

    







