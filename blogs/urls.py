from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='homepage'),
    path('createblog/',views.createBlog,name='create-blog'),
    path('<str:cname>/',views.categoryView,name='ind-category'),
    path('<str:cname>/<str:slug>/',views.readBlog,name='read-blog'),
    path('like/',views.likeBlog,name='like'),
]