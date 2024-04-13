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
    user_data = []

    
    context = {
        "user_profile":user_profile,
    }
    
    return render(request, 'user/profile.html',context)


def contact_us(request):
    return render(request, 'contact.html')