from django.contrib import admin
from . import models 

class AppointmentDetailAdmin(admin.ModelAdmin):
    exclude = ('end_time',)  
admin.site.register(models.AppointmentDetail,AppointmentDetailAdmin)
admin.site.register(models.Appointment)