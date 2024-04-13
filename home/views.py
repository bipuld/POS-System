from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserInfo
@login_required
def index(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user) 
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    return render(request, 'user/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


def signup(request):
    return render(request, 'user/signup.html')

def user_profile(request,id):
    user = User.objects.get(pk=id)  
    user_profile = UserInfo.objects.get(user=user)
    if request.method == "POST":
        full_name = request.POST.get('fullname')
        if full_name:
            first_name, last_name = full_name.split(' ')
        user_profile.first_name = first_name
        user_profile.last_name = last_name           
        user_profile.intro = request.POST.get('about')
        user_profile.phone = request.POST.get('phone')
        user_profile.country = request.POST.get('country')
        user_profile.address = request.POST.get('address')
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

    user_data = []

    
    context = {
        "user_profile":user_profile,
    }
    
    return render(request, 'user/profile.html',context)


def contact_us(request):
    return render(request, 'contact.html')