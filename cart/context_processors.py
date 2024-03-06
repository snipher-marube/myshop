from .cart import Cart

def carts(request):
    context = {'cart': Cart(request)}
    return context