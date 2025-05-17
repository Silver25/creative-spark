from django.db import models


class NewsletterRequest(models.Model):
    email = models.EmailField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Newsletter request from {self.email}"
