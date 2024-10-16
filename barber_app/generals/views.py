from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from django.contrib.auth.models import User

class AddressListView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=1)
        #your_model_data = models.Adress.objects.filter(user=User.objects.get(id=1)) 
        your_model_data = user.addresses 
        serializer = serializers.AddressSerializer(your_model_data, many=True)  
        return Response(serializer.data)  