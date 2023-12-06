from rest_framework import serializers
from .models import *

class UserSRl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone']
