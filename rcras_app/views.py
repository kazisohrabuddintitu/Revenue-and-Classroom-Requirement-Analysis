from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# superuser: admin; password: admin
# user: Lamisa; password: lami$$0000

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if the user has entered correct credentitals
        user = authenticate(username=username, password=password)

        if user is not None:
            #A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
            #No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
    
def revenue(request):
    return render(request,'revenue.html')

def about(request):
    return render(request,'about.html')