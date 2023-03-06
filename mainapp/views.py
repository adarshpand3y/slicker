from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import UserDetails
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request, "Welcome")
    return render(request, "home.html")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, "login.html")

def signupUser(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confPassowrd = request.POST.get("confPassword")
        year = request.POST.get("year")
        print(fullname, email, username, password, confPassowrd, year)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email taken! Try another one.")
            return redirect("/signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username taken! Try another one.")
            return redirect("/signup")
        
        if password != confPassowrd:
            messages.error(request, "Passwords do not match.")
            return redirect("/signup")
        
        if year not in ["1", "2", "3", "4", "5"]:
            messages.error(request, "Invalid year selected")
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

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "dashboard.html")