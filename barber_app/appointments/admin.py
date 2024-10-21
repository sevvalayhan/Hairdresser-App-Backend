from django.contrib import admin
from . import models 


admin.site.register(models.Appointment)
admin.site.register(models.AppointmentTime)

# Register your models here.
