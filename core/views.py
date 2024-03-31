from django.shortcuts import render, redirect
from django.http import HttpResponse  

# to return Product from models.py 
from .models import Product 
# import user authentication,login,logout from django 
from django.contrib.auth import authenticate,login,logout 
# for displaying alert messages etc..
from django.contrib import messages

# home page
def index(request): 
    # query to return Product object from models.py  
    products = Product.objects.all()  
    return render(request, "index.html", {'products': products}) 

def products(request):
    return render(request, "products.html")
def cart(request):
    return render(request, "cart.html")
def checkout(request):
    return render(request, "checkout.html")  

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