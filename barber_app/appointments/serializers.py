from rest_framework import serializers
from . import models

class AppointmentSerilaizer(serializers.ModelSerializer): 
    class Meta:
        model = models.Appointment
        fields = '__all__' 
