from django.shortcuts import render
from .models import About


def about_all(request):

    return render(request, "about/about.html")
