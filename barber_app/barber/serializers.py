from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__' 
class ServiceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceComment
        fields = '__all__' 
class ServiceLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceLike
        fields = '__all__' 
class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceImage
        fields = '__all__' 



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__' 
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLike
        fields = '__all__' 
class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostComment
        fields = '__all__' 



class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Barber
        fields = '__all__'         

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__' 