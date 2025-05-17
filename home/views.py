from django.shortcuts import render
from django.contrib import messages
from .forms import NewsletterForm


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
    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your request for "
                "newsletter was send! You can soon expect news from us."
            )

    newsletter_form = NewsletterForm()

    return render(
        request,
        "home/index.html",
        {
            "newsletter_form": newsletter_form
        },
    )
