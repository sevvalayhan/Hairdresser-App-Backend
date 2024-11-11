from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from . import models
from . import serializers
from . import serializers
from django.contrib.auth.models import User

# class ServiceCommentListView(APIView):
#     def get(self, request, *args, **kwargs):
#         your_model_data = models.Service.objects.get(id=1).service_comments
#         serializer = serializers.ServiceCommentSerializer(your_model_data, many=True)  
#         return Response(serializer.data) 

class ServiceListView(generics.ListAPIView):
    queryset = models.Service.objects.all()
    serializer_class =serializers.ServiceSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        serialized_data = serializers.ServiceSerializer(queryset, many=True).data
        print(serialized_data)  # JSON formatında serileştirilmiş veriyi yazdırır
        return queryset
class ServiceCommentListView(generics.ListAPIView):
    queryset = models.ServiceComment.objects.all()
    serializer_class =serializers.ServiceCommentSerializer

class ServiceLikeListView(generics.ListAPIView):
    queryset = models.ServiceLike.objects.all()
    serializer_class =serializers.ServiceLikeSerializer

class ServiceImageListView(generics.ListAPIView):
    queryset = models.ServiceImage.objects.all()
    serializer_class =serializers.ServiceImageSerializer

class BarberListView(generics.ListAPIView):
    queryset = models.Barber.objects.all()
    serializer_class =serializers.BarberSerializer

class PostListView(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class =serializers.PostSerializer

class PostCommentListView(generics.ListAPIView):
    queryset = models.PostComment.objects.all()
    serializer_class =serializers.PostCommentSerializer

class PostLikeListView(generics.ListAPIView):
    queryset = models.PostLike.objects.all()
    serializer_class =serializers.PostLikeSerializer

class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class =serializers.CategorySerializer