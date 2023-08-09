from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login


def home(request):
    return render(request,"index.html")

def signin(request):
    if request.method == 'POST':
        usnm = request.POST['ussername']
        pass1 = request.POST['pass1']
        
        # this will either return a none response or not none reponse
        user = authenticate(ussername = usnm, password = pass1)
        
        if user is not None:
            login(request,user) 
            fname = user.first_name
            return render(request,"authentication/signin.html",{'fname' : fname})
        else:
            messages.error(request,"Bad credentials")
            
    
    return render(request,"authentication/signin.html")

def signup(request):
    if request.method == "POST":
        usnm = request.POST['ussername']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myUser = User.objects.create_user(usnm,email,pass1)
        myUser.first_name= fname
        myUser.last_name = lname
        myUser.save()
        
        
        messages.success(request,"Your account has been successfully created")
    
        return redirect("signin/")
  
    return render(request,"authentication/signup.html")

def signout(request):
    return render(request,"authentication/signout.html")
