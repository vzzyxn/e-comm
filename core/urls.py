from django.urls import path 
from . import views
app_name = "route" 

urlpatterns= [
    path("",views.index, name='index'),
    path("products/",views.products, name='products'),
    path("cart/",views.cart, name='cart'),
    path("checkout/",views.checkout, name='checkout'), 
    path("login/",views.login_user, name='login'),
    path("logout/",views.logout_user, name='logout')
]