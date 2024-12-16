from django.db import models


# Create your models here.
class Card(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/', null=True)

    class Meta:
        db_table = 'book_table'

class Register(models.Model):
    email=models.CharField(max_length=200)
    password = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='profile/', null=True)
    class Meta:
        db_table = 'register'