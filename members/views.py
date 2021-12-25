from django.shortcuts import get_object_or_404, render,redirect
from .forms import RegistrationForm , CustomerAuthenticationForm ,CustomerUpdateForm
from django.contrib.auth import authenticate, forms,login,logout
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
import random
from .models import Kural , Customer , Follow
import json
from django.http import JsonResponse
from blogs.models import Category , Blog , Favourite



def landingPage(request):
    category_list = Category.objects.all()
    user = request.user
    x = random.randint(1,1331)
    kural = Kural.objects.get(id=x)
    context = {
        "category_list" : category_list,
        "kural" : kural
    }
    return render(request,'standard/landing_page.html',context)

@unauthenticated_user
def login_signupPage(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('submit') == 'signup':
            signup_form = RegistrationForm(request.POST)
            login_form = CustomerAuthenticationForm()
            if signup_form.is_valid():
                signup_form.save()
                email = signup_form.cleaned_data.get('email')
                password = signup_form.cleaned_data.get('password1')
                user = authenticate(request,email=email,password=password)
                print(user)
                if user is not None:
                    login(request,user)
                    return redirect('landing-page')

        elif request.POST.get('submit') == 'login':
            login_form = CustomerAuthenticationForm(request.POST)
            signup_form = RegistrationForm()
            if login_form.is_valid():
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = authenticate(request,email=email,password=password)
                print(user)
                if user is not None:
                    login(request,user)
                    return redirect('landing-page')

    else:
        signup_form = RegistrationForm()
        login_form = CustomerAuthenticationForm()

    context = {
        'login_form' : login_form,
        'signup_form' : signup_form,
        "category_list" : category_list,
    }

    return render(request,'member_info/login_register.html',context)

@login_required(login_url='register')
def logoutPage(request):
    logout(request)
    return redirect('landing-page')


def dashboardPage(request,pk):
    user = Customer.objects.get(id = pk)

    follow_status = False
    if request.user.is_authenticated:
        follow_status = Follow.objects.filter(follower=request.user,following=user).exists()
    following_count = Follow.objects.filter(follower = user).count()
    followers_count = Follow.objects.filter(following = user).count()
    blog_count = Blog.objects.filter(author=user).count()
    favourite_count = Favourite.objects.filter(author=user).count()

    context = {
        'user' : user , 
        'follow_status' : follow_status , 
        'following_count' : following_count ,
        'followers_count' : followers_count ,
        'blog_count' : blog_count ,
        'favourite_count' : favourite_count ,
    }
    return render(request,'member_info/dashboard.html',context)

def editProfile(request,pk):
    user = Customer.objects.get(id = pk)
    form = CustomerUpdateForm(instance=user)
    if request.method == "POST":
        form = CustomerUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            # user.profile_image.delete()
            form.save()
            
            return redirect('/')
    context = {
        'form' : form ,
    }

  
       
    return render(request,'member_info/edit_profile.html',context) 

@login_required(login_url='register')
def follow(request):
    data = json.loads(request.body)
    profile_id = data['profile_id']
    action = data['action']

    print(profile_id)
    print(action)

    following = get_object_or_404(Customer,pk=profile_id)

    try:
        f,created = Follow.objects.get_or_create(follower=request.user,following=following)

        if action == 'unfollow':
            f.delete()

        return JsonResponse('Action performed',safe=False) 
    except:
        return JsonResponse('Action failed',safe=False)

    
