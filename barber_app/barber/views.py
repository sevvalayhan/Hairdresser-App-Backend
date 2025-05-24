from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from . import models
from . import serializers
from . import serializers
from rest_framework import status 

class ServiceListView(APIView):
    def post(self, request, *args, **kwargs):
        search_query = request.data.get('search', None)
        if search_query:
            services = models.Service.objects.filter(includes__icontains=search_query) 
        else:
            services = None
        serializer =serializers.ServiceSerializer(services, many=True,context={'request': request})        
        return Response(serializer.data, status=status.HTTP_200_OK)   
       
    def get(self, request, *args, **kwargs):
        services = models.Service.objects.all()
        serializer = serializers.ServiceSerializer(services, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class BarberListView(APIView):
    def post(self, request, *args, **kwargs):
        search_query = request.data.get('search', None)
        if search_query:
            barbers = models.Barber.objects.filter(includes__icontains=search_query) 
        else:
            barbers = None
        serializer =serializers.BarberSerializer(barbers, many=True,context={'request': request})        
        return Response(serializer.data, status=status.HTTP_200_OK)   
    def get(self,request, *args, **kwargs):
        barbers = models.Barber.objects.all()
        serializer = serializers.BarberSerializer(barbers,many=True,context={'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    

       
class ServiceCommentListView(generics.ListAPIView):
    queryset = models.ServiceComment.objects.all()
    serializer_class =serializers.ServiceCommentSerializer

class ServiceLikeListView(generics.ListAPIView):
    queryset = models.ServiceLike.objects.all()
    serializer_class =serializers.ServiceLikeSerializer

class ServiceImageListView(generics.ListAPIView):
    queryset = models.ServiceImage.objects.all()
    serializer_class =serializers.ServiceImageSerializer

class PostListView(APIView):      
    def post(self, request, *args, **kwargs): 
        posts = models.Post.objects.all()  
        serializer =serializers.PostSerializer(posts, many=True,context={'request': request})        
        return Response(serializer.data, status=status.HTTP_200_OK)   
    def get(self,request, *args, **kwargs):
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializer(posts,many=True,context={'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class PostMediaListView(APIView):      
    def post(self, request, *args, **kwargs): 
        postMedias = models.PostMedia.objects.all()  
        serializer =serializers.PostMediaSerializer(postMedias, many=True,context={'request': request})        
        return Response(serializer.data, status=status.HTTP_200_OK)   
    def get(self,request, *args, **kwargs):
        postMedias = models.PostMedia.objects.all()
        serializer = serializers.PostMediaSerializer(postMedias,many=True,context={'request': request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    

class PostCommentListView(generics.ListAPIView):
    queryset = models.PostComment.objects.all()
    serializer_class =serializers.PostCommentSerializer

class PostLikeListView(generics.ListAPIView):
    queryset = models.PostLike.objects.all()
    serializer_class =serializers.PostLikeSerializer

class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class =serializers.CategorySerializer