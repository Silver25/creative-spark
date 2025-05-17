from django import forms
from .models import NewsletterRequest


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterRequest
        fields = ('email',)
