from django.db import models
from django.conf import settings

class Barber(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="barber")
    identity_number= models.CharField(max_length=11,)
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    bio=models.TextField(max_length=500)
    email= models.CharField(max_length=255)
    profile_image= models.ImageField(upload_to="statics/barber_profile_images")
    identity_card= models.FileField(upload_to="statics/barber_documents")
    status=models.SmallIntegerField()
    is_improved= models.BooleanField()

    def __str__(self):
      return f"{self.first_name} {self.last_name}"


def get_default_category():
    return Category.objects.get_or_create(
        category_name="Genel", 
        defaults={'category_image': 'statics/default_category_image.jpg'}
    )[0].id

class Category(models.Model):
    category_name = models.CharField(unique=True,max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    category_image = models.ImageField(upload_to="statics/category_images")

    def __str__(self):
        return f"Category: {self.category_name}"

from datetime import timedelta

class Service(models.Model):
    barber = models.ForeignKey("barber.Barber", on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=255,default="Genel")
    description = models.TextField(max_length=500, blank=True, null=True)
    duration = models.IntegerField(help_text="Duration of the service, in minutes.")  # Store duration in timedelta
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return f"Service: {self.title}"


class ServiceComment(models.Model):
   user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="service_comments")
   service= models.ForeignKey(Service,on_delete=models.CASCADE,related_name="service_comments")
   comment_text = models.TextField(max_length=500)
   comment_at = models.DateTimeField(auto_now=True) 

   def __str__(self):
      return f"{self.user} : {self.comment_text} "
   
class ServiceLike(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="service_likes")
   service= models.ForeignKey(Service,on_delete=models.CASCADE,related_name="service_likes")
   liked_at = models.DateTimeField(auto_now=True) 

   def __str__(self):
      return f"{self.user.username} : like {self.service.title} "
   
class ServiceImage(models.Model):
   service= models.ForeignKey(Service,on_delete=models.CASCADE,related_name="service_images")
   image = models.ImageField(upload_to="statics/service_images") 

   def __str__(self):
      return f"{self.image} "
   
class Post(models.Model):
   barber= models.ForeignKey(Barber,on_delete=models.CASCADE,related_name="posts")
   content = models.TextField(max_length=500)
   crated_at = models.DateTimeField(auto_now=True)
   category = models.ForeignKey(
        Category,
        related_name='posts',
        default=get_default_category,  
        on_delete=models.SET_DEFAULT
   )
   update_at=models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"{self.barber.first_name} {self.barber.last_name} : {self.content} "


class PostMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_media')
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='statics/post_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file} {self.media_type} "


class PostLike(models.Model):
     
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_likes')    
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"liked by:  {self.user.first_name} {self.user.last_name}"

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_comments')    
    commented_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.content} "
 