from django.shortcuts import render


# 404 handler function will load an HTML file called 404.html
# whenever a user tries to access a URL that does not exist
def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
