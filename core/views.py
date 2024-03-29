from django.shortcuts import render
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
    return render(request, "store/index.html", {'products': products}) 

def products(request):
    return render(request, "store/products.html")
def cart(request):
    return render(request, "store/cart.html")
def checkout(request):
    return render(request, "store/checkout.html")  
def login_user(request):
    return render(request, "store/login.html") 
def logout_user(request):
    logout(request)