from django.urls import path 
from core.views import index,category,cart,checkout
app_name = "route" 

urlpatterns = [
    path("",index),
    path("category/",category),
    path("cart/",cart),
    path("checkout/",checkout)
]