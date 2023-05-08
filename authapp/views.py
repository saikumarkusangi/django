from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('firstname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password != confirmpassword:
            messages.info(request,"Password is not matching")
            return redirect('/signup')

        try:
            if User.objects.filter(username = username).first():
                messages.warning(request,"email already taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username=username,email=email,password=password)
     
        myuser.save()
        return redirect('/login')

    return render(request,'signup.html')