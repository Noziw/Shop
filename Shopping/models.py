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
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

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


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     date = models.DateField(auto_now=True)
#     os = (
#         ('ochiq', 'ochiq')
#         ('yetkazilgan', 'yetgazilgan')
#     ) 
#     status =models.CharField(max_length=20, choices=os)
#     paymet = models.CharField(max_length=25)

#     def __str__(self):
#         return str(self.date)
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    os = [
        ["ochiq", 'ochiq'],
        ['yetkazilgan', 'yetkazilgan']
    ]
    status = models.CharField(max_length=20, choices=os)
    payment = models.CharField(max_length=25) # card raqam
    quantity = models.IntegerField

    def __str__(self):
        return str(self.date)








