from django.shortcuts import render,get_object_or_404 , redirect
from .models import Category , Blog , Favourite
from .forms import BlogForm
from members.models import Follow
import json
from django.http import JsonResponse

def categoryView(request,cname):
    category_list = Category.objects.all()
    category = Category.objects.get(name=cname)
    blogs = category.blog_set.all()
    context = {
        'category' : category ,
        'blogs' : blogs ,
        "category_list" : category_list, 
    }
    return render(request,'blogs/individual_category.html',context)

def homePage(request):
    category_list = Category.objects.all()
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs ,
        "category_list" : category_list,  
    }
    return render(request,'blogs/homepage.html',context)


def createBlog(request):
    author = request.user
    blogForm = BlogForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            author = author.id
            blog_form.save(author = author)
            return redirect('landing-page')
        else:
            print(blog_form.errors)
    context = {
        'blog_form' : blogForm ,
    }
    return render(request,'blogs/create_blog.html',context)


def readBlog(request,cname,slug):
    category_list = Category.objects.all()
    blog = Blog.objects.get(slug=slug)
    favourite_count = Favourite.objects.filter(blog=blog).count()

    
    follow_status = False
    if request.user.is_authenticated:
        follow_status = Follow.objects.filter(follower=request.user,following=blog.author).exists()
    
    context = {
        'blog' : blog ,
        "category_list" : category_list,
        'follow_status' : follow_status ,
        'favourite_count' : favourite_count ,
    }
    return render(request,'blogs/individual_blog.html',context)

def likeBlog(request):
    data = json.loads(request.body)
    blog_id = data['blog_id']

    print(blog_id)
    

    blog = get_object_or_404(Blog,pk=blog_id)

    try:
        if Favourite.objects.filter(author=request.user,blog=blog).exists():
            Favourite.objects.filter(author=request.user,blog=blog).delete()

        else: 
            l = Favourite.objects.create(author=request.user,blog=blog)


        return JsonResponse('Action performed',safe=False) 
    except:
        return JsonResponse('Action failed',safe=False)