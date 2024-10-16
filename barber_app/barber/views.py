from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from django.contrib.auth.models import User

class ServiceCommentListView(APIView):
    def get(self, request, *args, **kwargs):
        your_model_data = models.Service.objects.get(id=1).service_comments
        serializer = serializers.ServiceCommentSerializer(your_model_data, many=True)  
        return Response(serializer.data)  
    