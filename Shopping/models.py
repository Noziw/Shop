from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    image = models.FileField(upload_to = 'products/')
    cost = models.IntegerField()
    hajm = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=120)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=12)
    card = models.CharField(max_length=16)
    adress = models.TextField()

    def __str__(self):
        return self.username









