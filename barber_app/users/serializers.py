from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.cache import cache 
from rest_framework import serializers
from .models import  User 
from django.contrib.auth import authenticate
from generals import serializers as generalsSerializers

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    addresses = generalsSerializers.AddressSerializer(many = True, required=False)
    class Meta:
        model = User
        fields = ['id', 'confirm_password', 'email', 'password', 'phone_number','addresses']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'addresses': {'required': False} 
        }        
    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"password": "Şifreler eşleşmiyor."})
        return data
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()
        return user



class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    def validate(self, data):
        email = data["email"]
        code = data["code"]
        stored_code = cache.get(f"verify:{email}")
        if stored_code is None:
            raise serializers.ValidationError("Code expired or invalid.")
        if code != stored_code:
            raise serializers.ValidationError("Invalid code.")
        user = User.objects.get(email=email)
        user.is_verified = True
        user.is_active = True
        user.save()
        cache.delete(f"verify:{email}")
        return data

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.email 
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['email'] = self.user.email
        data['phone_number'] = self.user.phone_number
        return data