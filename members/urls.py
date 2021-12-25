from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingPage,name='landing-page'),
    path('register/',views.login_signupPage,name='register'),
    path('logout/',views.logoutPage,name='logout'),
    path('<int:pk>/',views.dashboardPage,name='dashboard'),
    path('<int:pk>/edit_profile/',views.editProfile,name='edit-profile'),
    path('follow/',views.follow,name='follow')
]