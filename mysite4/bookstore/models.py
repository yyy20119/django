from django.db import models

# Create your models here.
class BookStore(models.Model):
    title=models.CharField(max_length=11,verbose_name='书名')

class Book(models.Model):
    title=models.CharField(max_length=20,unique=True,verbose_name='书名')
    pub=models.CharField(max_length=50,verbose_name='出版社')
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='图书定价')
    market_price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='图书零售价')

    def __str__(self):
        return '<%s>' % self.title

class Author(models.Model):
    name=models.CharField(max_length=11,verbose_name='姓名')
    age=models.IntegerField(default=1,verbose_name='年龄')
    email=models.EmailField(null=True,verbose_name='邮箱')







