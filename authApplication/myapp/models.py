from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from random import randint
class User(AbstractUser):

    phone=models.CharField(max_length=15)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=15,null=True,blank=True)


    def generate_otp(self):
        otp_number=str(randint(1000,9000))+str(self.id)
        self.otp=otp_number
        self.save()