from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     email = models.EmailField()

class product(models.Model):
    product_name = models.CharField(max_length = 75)
    product_price = models.IntegerField()
    user = models.ManyToManyField(User)