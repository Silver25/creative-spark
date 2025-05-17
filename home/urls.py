"""
URL configuration for the Home app.

This module defines the URL patterns for the application.
It includes the routes for the main home page.

Routes:
    - Home Page: Accessible at the root URL ('/'),
    handled by `views.index` view.

Modules:
    - django.urls: Contains tools to define URL patterns.
    - views: Contains the view functions for the app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
