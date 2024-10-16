from rest_framework import serializers
from . import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adress
        fields = '__all__' 