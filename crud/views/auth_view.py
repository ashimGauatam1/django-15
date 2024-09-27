from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as Login
def register(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(
            username = username, 
            email = email, 
        )
        user.set_password(password)
        user.save()
        return render(request,"auth/login.html")
    return render(request,'auth/register.html')
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(email=email).first()
        if user:
            if user.check_password(password):
                Login(request,user)
                
                return redirect("home")
            else:
                return render(request,'auth/login.html')
        else:
            return render(request,'auth/login.html')
    return render(request,'auth/login.html')

