import base64
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password

@login_required
def index(request):
    return render(request, 'home.html')



def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user) 
            messages.success(request, f"Welcome {user.username}")
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, f"Thank You For Using Us")
    return redirect('login')


def signup(request):
    return render(request, 'user/signup.html')

def user_profile(request,id):
    user = User.objects.get(pk=id)  
    user_profile = UserInfo.objects.get(user=user)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "profile_update":
            full_name = request.POST.get('fullname')
            if full_name:
                first_name, last_name = full_name.split(' ')
            user_profile.first_name = first_name
            user_profile.last_name = last_name           
            user_profile.intro = request.POST.get('about')
            user_profile.phone = request.POST.get('phone')
            user_profile.country = request.POST.get('country')
            user_profile.address = request.POST.get('address')
            user_profile.country = request.POST.get('country')
            profile_image = request.FILES.get('profile_img')
            if profile_image:
            
                user_profile.image = profile_image
            else:
                
                pass  # Or consider setting user_profile.image to None explicitly 
            user_profile.email = request.POST.get('email')
            print("User profile", user_profile.image)
            user_profile.save()
            if user_profile:
                print("Profile updated Successfully")

             
        if action == "password_change":
            old_password = request.POST.get('oldpassword')
            new_password= request.POST.get('newpassword')
            renew_password = request.POST.get('renewpassword')
            user = authenticate(request, username=request.user.username, password=old_password)
            if user is not None:
                if new_password==renew_password:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Your password has been changed successfully")
                else:
                    messages.error(request, "Your new password and confirm password does not match")
                    return redirect('index')
                    
            else:
                messages.error(request, "Your password is incorrect")
            
            
            
            
    
    context = {
        "user_profile":user_profile,
    }
    
    return render(request, 'user/profile.html',context)


def contact_us(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        type_business = request.POST.get('type_business')
        subject = request.POST.get('subject')
        message  = request.POST.get('message')
        contact = Contact(name = name,email = email,phone = phone,address = address,business_type = type_business,subject = subject,message = message)
        contact.save()
        if contact:
            messages.success(request, "Thank You For Contacting Us!")
            return redirect('login')
        else:
            messages.error(request,"Something Went Wrong!")
            return redirect('contact')
        
    return render(request, 'contact.html')