from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.signup,name='register'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('contact-us',views.contact_us,name='contact')

    
]
