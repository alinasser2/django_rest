from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# serialize the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

