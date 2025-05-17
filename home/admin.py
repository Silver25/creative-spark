from django.contrib import admin
from .models import NewsletterRequest


@admin.register(NewsletterRequest)
class NewsletterRequestAdmin(admin.ModelAdmin):

    list_display = ('email', 'read',)
