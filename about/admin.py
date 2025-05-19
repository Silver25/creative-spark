from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'label_1',
        'paragraph_1',
        'label_2',
        'paragraph_2',
    )


admin.site.register(About, AboutAdmin)
