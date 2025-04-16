from .cart import Cart

# create contex

def cart(request):
    # return the default data from our cart
    return {'cart':Cart(request)}