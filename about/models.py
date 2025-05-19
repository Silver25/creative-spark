from django.db import models


class About(models.Model):
    label_1 = models.CharField(max_length=255)
    paragraph_1 = models.TextField()
    label_2 = models.CharField(max_length=255)
    paragraph_2 = models.TextField()

    def __str__(self):
        return self.label_1
