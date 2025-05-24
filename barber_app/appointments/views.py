from django.shortcuts import render
from .models import Appointment
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AppointmentSerilaizer
from rest_framework import status 

class AppointmentView(APIView):
    def post(self, request, *args, **kwargs): 
        appointments =  Appointment.objects.all()  
        serializer =AppointmentSerilaizer(appointments, many=True,context={'request': request})        
        return Response(serializer.data, status=status.HTTP_200_OK)   
    def get(self,request, *args, **kwargs):
        appointments = Appointment.objects.all()
        serializer =  Appointment(appointments,many=True,context={'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)