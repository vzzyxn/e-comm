from django.urls import path 
from core.views import index,products,cart,checkout
app_name = "route" 

urlpatterns = [
    path("",index),
    path("products/",products),
    path("cart/",cart),
    path("checkout/",checkout)
]