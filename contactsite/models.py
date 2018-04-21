from django.db import models

# Create your models here.

class contact_info(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    content = models.CharField(max_length=300)