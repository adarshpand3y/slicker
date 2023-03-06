from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import UserDetails

# Create your views here.
def index(request):
    return render(request, "home.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "profile.html")
        else:
            return render(request, "login.html")
    return render(request, "login.html")

def signupUser(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confPassowrd = request.POST.get("confPassword")
        year = request.POST.get("year")
        print(fullname, email, username, password, confPassowrd, year)
        if User.objects.filter(username=username).exists():
            return redirect("/signup")

        if User.objects.filter(email=email).exists():
            return redirect("/signup")
        
        if password != confPassowrd:
            return redirect("/signup")
        
        newUser = User(first_name=fullname, email=email, username=username, password=password)
        newUser.save()
        newUserDetails = UserDetails(userClass=newUser, currentYear=year)
        newUserDetails.save()
        return render(request, "login.html")
    return render(request, "signup.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")