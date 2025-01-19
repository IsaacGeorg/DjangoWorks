from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    language=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    image=models.ImageField(upload_to='bookimages',null=True)

    def __str__(self):
        return self.title

# settings.py
# makemigrations - to create query file
# migrate - to execute query file
# ORM - Object Relational Mapper
