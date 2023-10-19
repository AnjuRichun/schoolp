from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here
def home(request):
    return render(request,"home.html")
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('storeapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('storeapp:login')
        else:
            messages.error(request,"password not matching")
            return redirect('storeapp:register')
    return render(request,"register.html")
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username")
            return redirect('storeapp:login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')