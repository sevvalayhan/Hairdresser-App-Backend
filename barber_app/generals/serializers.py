from rest_framework import serializers
from . import models


class CountrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = models.Country
        fields = '__all__' 

class ProvinceSerializer(serializers.ModelSerializer):
    country= CountrySerializer()
    class Meta:
        model = models.Province
        fields = '__all__' 

class DistrictSerializer(serializers.ModelSerializer):
  
    province = ProvinceSerializer(read_only=True)
    class Meta:
        model = models.District
        fields = '__all__' 
class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneNumber 
        fields = '__all__' 

class AddressSerializer(serializers.ModelSerializer):
    district = DistrictSerializer( )
    class Meta:
        model = models.Adress
        fields = '__all__' 
       