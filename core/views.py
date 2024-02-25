from django.shortcuts import render
from django.http import HttpResponse 

def index(request): 
    return render(request, "store/index.html") 
def products(request):
    return render(request, "store/products.html")
def cart(request):
    return render(request, "store/cart.html")
def checkout(request):
    return render(request, "store/checkout.html")
