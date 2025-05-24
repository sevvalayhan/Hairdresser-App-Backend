from rest_framework import serializers
 
from . import models

class ServiceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceComment
        fields = '__all__' 
class ServiceLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceLike
        fields = '__all__'
         
class ServiceImageSerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()
    class Meta:
        model = models.ServiceImage
        fields = '__all__'      
    def get_full_image_url(self, model):
        request = self.context.get('request')
        if model.image:
            return request.build_absolute_uri(model.image.url)
        return request.build_absolute_uri('/assets/images/hairdresser.jpg')

from  users.serializers import UserSerializer    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class CategorySerializerToBarber(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [ 'category_name']
    
class BarberSerializerToPost(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = models.Barber
        fields = ('full_image_url','first_name','last_name','email','includes','shop_name','is_improved','profile_image' ,'user' )    
    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)
        return request.build_absolute_uri('/assets/images/boy.jpg')

class ServiceSerializer(serializers.ModelSerializer):
    service = models.Service.objects.all()
    barber = BarberSerializerToPost(service,read_only=True)
    category = CategorySerializer(read_only=True)
    service_images = ServiceImageSerializer(many=True, read_only=True)
    class Meta:
        model = models.Service
        fields = '__all__' 

class BarberSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    full_image_url = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    category =CategorySerializer(read_only = True,many= True)
    class Meta:
        model = models.Barber
        fields = '__all__'
    def get_full_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image:
            return request.build_absolute_uri(obj.profile_image.url)
        return request.build_absolute_uri('/assets/images/boy.jpg')
    
class PostMediaSerializer(serializers.ModelSerializer):
    media_url = serializers.SerializerMethodField()
    class Meta:
        model = models.PostMedia
        fields = '__all__'
    def get_media_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None
    
class PostSerializer(serializers.ModelSerializer):
    posts = models.Post.objects.all()
    post_medias = PostMediaSerializer(many=True, read_only=True)
    barber = BarberSerializerToPost(posts, read_only= True,)
    category= CategorySerializer(read_only = True)
    class Meta:
        model = models.Post
        fields = '__all__' 
    
class PostLikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only= True,)    
    class Meta: 
        model = models.PostLike
        fields = '__all__' 

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostComment
        fields = '__all__'  

 