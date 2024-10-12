from django.db import models

# Create your models here.

class Book(models.Model):

    name = models.CharField(max_length=50, help_text="Name of the book")
    author = models.CharField(max_length=20, help_text="Name of the book writer")
    detail = models.TextField(help_text="Description of the book")
