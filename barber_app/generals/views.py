 
from rest_framework import generics
from . import models
from . import serializers

class AddressListView(generics.ListAPIView):
   queryset = models.Adress.objects.all()
   serializer_class = serializers.AddressSerializer

class CountryListView(generics.ListAPIView):
   queryset = models.Country.objects.all()
   serializer_class = serializers.CountrySerializer

class ProvinceListView(generics.ListAPIView):
   queryset = models.Province.objects.all()
   serializer_class = serializers.ProvinceSerializer
class DistrictListView(generics.ListAPIView):
   queryset = models.District.objects.all()
   serializer_class = serializers.DistrictSerializer 
class PhoneNumberListView(generics.ListAPIView):
   queryset = models.PhoneNumber.objects.all()
   serializer_class = serializers.PhoneNumberSerializer 