from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages import constants as messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            print('invalid credentials..') 
            return redirect('signin')  

    else:
        return render(request,'signin.html')

    

def signup(reqeust):
    if reqeust.method=='POST':
        first_name=reqeust.POST['first_name']
        last_name=reqeust.POST['last_name']
        username=reqeust.POST['username']
        email=reqeust.POST['email']
        designation=reqeust.POST.get("designation")
        password=reqeust.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(reqeust,'username Taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(reqeust,'Email Taken')  
            return redirect('signup')

        else:    
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,designation=designation,password=password)
            user.save()
            return redirect('signin')

    else:
        return render(reqeust,'signup.html')
