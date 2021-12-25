from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.shortcuts import render


class CustomerManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValidationError('Users must provide an E-mail address')
        if not username:
            raise ValidationError('Users must provide a Username')

        user = self.model(
                    email=self.normalize_email(email),
                    username = username,)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser,PermissionsMixin):
    email           = models.EmailField(max_length=50,unique=True)
    username        = models.CharField(max_length=30,unique=True)
    date_joined     = models.DateField(auto_now_add=True)
    last_login      = models.DateField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    profile_image   = models.ImageField(default= 'usercolored.png' , null=True,blank=True)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

    def profileimageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

        
class Kural(models.Model):
    Line1 = models.TextField()
    Line2 = models.TextField()	
    kural_Translation = models.TextField()	
    Explanation = models.TextField()	
    Explanation_translation = models.TextField()	
    adikaram_name = models.TextField()	
    adikaram_translation = models.TextField()

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name='follower')
    following = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,related_name='following')

