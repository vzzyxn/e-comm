from django.shortcuts import render, redirect
from django.http import HttpResponse  

# to return Product from models.py 
from .models import Product 
# import user authentication,login,logout from django 
from django.contrib.auth import authenticate,login,logout 
# for displaying alert messages etc..
from django.contrib import messages 

# packages for registering a new user
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# home page
def index(request): 
    # query to return Product object from models.py  
    products = Product.objects.all()  
    return render(request, "index.html", {'products': products}) 

# products page 
def products(request):
    return render(request, "products.html")

# cart page
def cart(request):
    return render(request, "cart.html")

# checkout page
def checkout(request):
    return render(request, "checkout.html")  

# login page
def login_user(request): 
    if request.method == "POST":
        userid = request.POST['userid']  
        userpassword = request.POST['userpassword']
        user = authenticate(request, username = userid, password = userpassword)
        if user is not None:
            login(request, user)
            messages.success(request, (f"Hello {userid}👋! You have been logged in"))
            return redirect('/') 
        else:
            messages.success(request, ("Incorrect username or password! Please try again"))
            return redirect('/login')
    else:
        return render(request, "login.html") 
def logout_user(request):
    logout(request) 
    messages.success(request, (f"Bye! see you again.."))
    return redirect('/')

# register page
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":  
        # Here all the fields on the webpage that the user entered(POST) will be stored to the SignUpForm() function
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            userid = form.cleaned_data['username']
            userpassword = form.cleaned_data['password1']
            user = authenticate(username = userid, password = userpassword) 
            login(request, user) 
            messages.success(request, ("Sucessfully registered, Welcome!")) 
            return redirect('/')
        else:
            messages.success(request, ("Something went wrong! Register again.."))
            return redirect('/register')

    return render(request, "register.html", {'form':form})
