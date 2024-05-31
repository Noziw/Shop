from rest_framework import serializers
from .models import *

class UserSRl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone']

class LoginSRL(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username', 'password']


class AccountSRL(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSRL(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSRL(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AdminSRL(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

    class OrderSRL(serializers.ModelSerializer):
        class Meta:
         model = Order
        fields = "__all__"