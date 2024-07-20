from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# from .forms import SignUpForm

def home(request):
    return render(request,"index.html")



def signin(request):
    # Define the signin view function, which takes the HTTP request object as an argument
    if request.method == 'POST':
        # Check if the request method is POST, indicating that the form has been submitted
        form = AuthenticationForm(request, data=request.POST)
        print(request.POST)
        # Create an instance of the AuthenticationForm with the data from the request
        if form.is_valid():
            
            # Check if the form data is valid (i.e., the data meets the form's requirements)
            username = form.cleaned_data.get('username')
            # Extract the cleaned username data from the form
            password = form.cleaned_data.get('password')
            # Extract the cleaned password data from the form
            user = authenticate(username=username, password=password)
           
            # Authenticate the user by checking the username and password against the database
            if user is not None:
                # Check if the authentication was successful (i.e., a matching user was found)
                login(request, user)
                # Log the user in by creating a session
                # messages.info(request, f'Welcome back, {username}!')
           
                # Add an informational message to the messages framework to welcome the user
                return redirect('/home/')
                # Redirect the user to the 'home' URL (change 'home' to the name of your home view)
            else:
                # If authentication failed (i.e., no matching user was found)
                messages.error(request, 'Invalid username or password.')
                
             
                # Add an error message to the messages framework indicating invalid credentials
        else:
         
            # If the form data is not valid
            messages.error(request, 'Invalid username or password.')
            # Add an error message to the messages framework indicating invalid credentials
    else:
        # If the request method is not POST (i.e., the form is being accessed for the first time)
        form = AuthenticationForm()
       
        # Create an empty instance of the AuthenticationForm to be rendered in the template
    return render(request,"authentication/signin.html")

    # return render(request, 'signin.html', {'form': form})
    # Render the 'signin.html' template with the form instance passed as context


def signup(request):
    if request.method == "POST":
        usnm = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            # print(messages)
            return redirect('signup')

        # Check if username is already taken
        if User.objects.filter(username=usnm).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        # Check if email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
            return redirect('signup')

        # Create the user
        myUser = User.objects.create_user(username=usnm, email=email, password=pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect("home")

    return render(request, "authentication/signup.html")

def signout(request):
    return redirect('/')

def logoutPage(request):
    return redirect('/')




