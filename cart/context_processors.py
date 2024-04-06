from .cart import Cart 

# create context processor so that the cart will be made available to all pages 
def cart(request):
    # return default data from cart 
    return {'cart': Cart(request)}
