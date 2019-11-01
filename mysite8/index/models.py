from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=11,verbose_name='书名')

    def __str__(self):
        return self.title