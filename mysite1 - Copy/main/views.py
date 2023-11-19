from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, request
from main import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'main/home (2).html')

def projects(request):
    return render(request, 'main/projects.html')

def aboutme(request):
	return render(request, 'main/home dark.html')

def sign_up(request):
    msg = " "
    emailvalidity = False
    usernamevalidity = False
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        
        if (re.fullmatch(regex, email)):
            emailvalidity = True
        if len(username) < 3:
            msg = "Username should be atleast 4 characters"
        if emailvalidity == False:
            msg = "Please enter a valid email"
        if len(password1) <= 3: 
            msg = "Password should be atleast 4 characters"
        if password1 != password2:
            msg = "Passwords do not match"
        else:
            if User.objects.filter(username=username).exists() == True:
                msg="this username is aldready taken"
            else:    
                user = User.objects.create_user(username, email, password1)
                return redirect('http://127.0.0.1:8000/signin')
    return render(request, 'main/register.html', {'msg':msg})

def dashboard(request):
    username4 = None
    if request.user.is_authenticated:
        username4 = request.user.username
    else:
    	username4 = "please login"
        
    
    return render(request, 'main/dashboard.html', {'username':username4})
   # user1 = None
   # if request.user.is_authenticated():
    #    user1 = request.user.username


def sign_in(request):
    msg2 = " "
    if request.method == 'POST':
        username2 = request.POST.get('username')
        password3 = request.POST.get('pass1')
        user = authenticate(username=username2, password=password3)
        print("user- ", user)
        if user is not None:
        	
        	login(request, user)
        	return redirect('http://127.0.0.1:8000/dashboard')
        else:
        	msg2="username or password is invalid"
        	
    return render(request, 'main/login.html', {'msg2':msg2})
  

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')
