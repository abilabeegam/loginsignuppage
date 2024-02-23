from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def handlesignup(request):

    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")

        if password != confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.info(request,"User Already Exist !!")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Already Taken")
                return redirect('/signup')
        except:
            pass

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"SignUp Successfull !")
        return redirect('/login')
    return render(request,'signup.html')

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Susess")
            return redirect('/')
        else:
            messages.error(request,"INVALID CREDINTIALS")
            return redirect('/login')
    return render(request,'login.html')
def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Successfull")
    return redirect('/')