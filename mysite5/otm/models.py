from django.db import models

# Create your models here.

class Publisher(models.Model):
    name=models.CharField(max_length=11)

class Book(models.Model):
    title=models.CharField(max_length=11)
    publisher=models.ForeignKey(Publisher)

