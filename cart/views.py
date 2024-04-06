from django.shortcuts import render, get_object_or_404
from .cart import Cart
from core.models import Product
from django.http import JsonResponse  

# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html') 

def cart_add(request):
    # get the cart 
    cart = Cart(request)
    if request.POST.get('action') == "post": 
        # get the product data
        product_id = int(request.POST.get('product_id'))
        # to look product in db 
        product = get_object_or_404(Product, id=product_id)
        # save to session 
        cart.add(product=product) 
        response = JsonResponse({'Product name': product.name})
        return response

         

def cart_delete(request):
    pass
def cart_update(request):
    pass 
