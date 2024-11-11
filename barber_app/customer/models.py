from django.db import models
from django.conf import settings

class Customer(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
   first_name  = models.CharField(max_length = 255 , blank = False  , null= False)
   last_name  = models.CharField(max_length = 255 , blank = False  , null= False)
   phone_number = models.OneToOneField("generals.PhoneNumber" ,null=True, unique = True,on_delete=models.SET_NULL)
   email = models.EmailField(blank = False , null = False , unique  = True)
   profile_image = models.ImageField(upload_to='statics/profile_images/', blank=True, null=True)
   
   def __str__(self):
      return f"{self.first_name} {self.last_name}"

