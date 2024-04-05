from django.urls import path 
from . import views

urlpatterns= [
    path("",views.index, name='index'),  
    path("checkout/",views.checkout, name='checkout'), 
    path("login/",views.login_user, name='login'),
    path("logout/",views.logout_user, name='logout'), 
    path("register/",views.register_user, name='register'),   
    # <int:pk> will create (product number) along with the url
    path("product/<int:pk>",views.product, name='product'), 

 
]