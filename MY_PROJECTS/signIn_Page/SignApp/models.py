from django.db import models

# Create your models here.
class NewAccount(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=320)
    Password=models.CharField(max_length=50)