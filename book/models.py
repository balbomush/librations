from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    published_date = models.DateField(
            blank=True, null=True)
    descriptions = models.TextField()

    def __str__(self):
        return self.title

