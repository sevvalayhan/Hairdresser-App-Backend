from django.contrib import admin
from . import models

admin.site.register(models.Adress)
admin.site.register(models.Country)
admin.site.register(models.District)
admin.site.register(models.Province)
admin.site.register(models.PhoneNumber)