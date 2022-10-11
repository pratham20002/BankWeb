from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

def index(request):
    print("User is .............................................:", request.user)
    if request.user.is_anonymous:
        return render(request, 'index.html')

    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    if request.user.is_authenticated:
        return HttpResponse("This Is Services Page...!")
    else:
        messages.error(request, 'You Need To Login First.....!')
        return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request,'Submitted SucessFully....!  We will respond you for sure.....')

    return render(request, 'contact.html')

def Login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    if request.method == "POST":
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,'Login SucessFully....!')
            return redirect('/')
            
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    messages.success(request,'Logout SucessFully....!')
    return redirect('/')


def SignIn(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(firstname,lastname,email,username,password)
        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username= username, password= password)
        return render(request, 'login.html')

    return render(request,'signin.html')


def create_account(request):
    if request.user.is_authenticated:
        return render(request, 'create_account.html')

    else:
        messages.error(request, 'You Need To Login First To Perform This Task.....!')
        return render(request, 'index.html')


def deposite(request):
    if request.user.is_authenticated:
        return render(request, 'deposite.html')

    else:
        messages.error(request, 'You Need To Login First To Perform This Task.....!')
        return render(request, 'index.html')