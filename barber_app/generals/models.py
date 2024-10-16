from django.db import models
from django.contrib.auth.models import User


class Adress(models.Model):    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="addresses")
    address_type= models.SmallIntegerField()
    building_no=models.CharField(max_length=10,blank=True,null=True)
    street = models.CharField(max_length=255,blank=True,null=True)
    region= models.CharField(max_length=255)
    postal_code= models.IntegerField()
    distirct = models.ForeignKey("District",on_delete=models.SET_NULL,null=True,blank=False,related_name="addresses")
    province = models.ForeignKey("Province",on_delete=models.SET_NULL,null=True,related_name="addresses")
    country = models.ForeignKey("Country",on_delete=models.SET_NULL,null=True,related_name="addresses")
    description=models.TextField(max_length=500,blank=True,null=True)
    coordinate=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
       return f"{self.user.username} {self.distirct} ,{self.province} , {self.country} "


class Country(models.Model):
    country_code=models.SmallIntegerField()
    country_name=models.CharField(max_length=255,unique=True)
    def __str__(self):
       return f"{self.country_name}"

   

class Province(models.Model):
    province_name=models.CharField(max_length=255,unique=True)
    country= models.ForeignKey(Country,on_delete=models.CASCADE,related_name="provinces")
    def __str__(self):
       return f"{self.province_name}"

   

class District(models.Model):
    province= models.ForeignKey(Province,on_delete=models.CASCADE,related_name="districts")
    district_name=models.CharField(max_length=255,unique=True)
    def __str__(self):
       return f"{self.district_name}"

   

class PhoneNumber(models.Model):
    country= models.ForeignKey(Country,on_delete=models.SET_NULL,blank=True,null=True,related_name="phone_numbers")
    phone_number=models.CharField(max_length=11,unique=True)
       
    def __str__(self):
       return f"{self.phone_number}"

   