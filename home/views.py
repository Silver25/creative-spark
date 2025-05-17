from django.shortcuts import render


def index(request):
    """
    Renders the index.html template.

    This view serves as the entry point for the application, rendering
    the main landing page (index.html). It doesn't process any specific
    data or context, but can be extended in the future to include
    dynamic content.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response with the rendered index.html template.
    """
    return render(request, 'home/index.html')
