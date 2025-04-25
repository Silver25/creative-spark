from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """
    docstring / description of the function:
    A simple view to renders the cart contents page
    """
    return render(request, 'cart/cart.html')
