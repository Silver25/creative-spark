from django.shortcuts import render

# Create your views here.

def all_products(request):
    """
    A view to display all products, including sorting and search queries
    """
    return render(request, 'products/products.html')
