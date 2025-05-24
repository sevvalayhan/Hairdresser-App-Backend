from django.db import models
from django.conf import settings

class Category(models.Model):
    category_name = models.CharField(unique=True,max_length=15)    
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    category_image = models.ImageField(upload_to="category_images")
    def __str__(self):
        return f"Category: {self.category_name}"
    
    
class Barber(models.Model): 
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="barber")
    category = models.ManyToManyField(
        Category,
          related_name='barbers', 
    )
    identity_number= models.CharField(max_length=11,)
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    bio=models.TextField(max_length=500)
    email= models.CharField(max_length=255)
    profile_image= models.ImageField(upload_to="barber_profile_images")
    identity_card= models.FileField(upload_to="barber_documents")
    status=models.SmallIntegerField()
    is_improved= models.BooleanField()
    shop_name = models.CharField(max_length=255,blank=False,null=False) 
    includes= models.TextField(max_length=1000,blank=True,)

    def save(self, *args, **kwargs):
            parts = []
            if self.first_name:
                parts.append(self.first_name)
            if self.last_name  :
                parts.append(self.last_name)
            if self.shop_name :
                parts.append(self.shop_name)
            
            if (
                self.user.addresses.exists() and
                self.user.addresses.first().district
                ):
                district = self.user.addresses.first().district
                if district.district_name:
                        parts.append(district.district_name)
                if district.province:
                    if district.province.province_name:
                            parts.append(district.province.province_name)
                    if district.province.country and district.province.country.country_name:
                            parts.append(district.province.country.country_name)

            self.includes = ', '.join(parts)        
            super().save(*args, **kwargs)

    @property
    def full_image_url(self):
         request = settings.SITE_URL  
         if self.profile_image:
            return f"{request}{self.profile_image.url}"
         return f"{request}/assets/images/boy.jpg"
    
    
    def __str__(self):
      return f" {self.first_name} {self.last_name}"

class Service(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name="services")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services" )
    title = models.CharField(max_length=25,default="Genel")
    description = models.TextField(max_length=500, blank=True, null=True)
    includes= models.TextField(max_length=1000,blank=True,)
    duration = models.IntegerField(help_text="Duration of the service, in minutes.") 
    price = models.FloatField()

    def save(self, *args, **kwargs):
        parts = []
        if self.title:
            parts.append(self.title)
        if self.category and self.category.category_name:
            parts.append(self.category.category_name) 
        if self.barber:
            if self.barber.first_name:
                parts.append(self.barber.first_name)
            if self.barber.last_name:
                parts.append(self.barber.last_name)
            if self.description:
                parts.append(self.description)
            if (
                self.barber.user.addresses.exists() and
                self.barber.user.addresses.first().district
            ):
                district = self.barber.user.addresses.first().district
                if district.district_name:
                    parts.append(district.district_name)
                if district.province:
                    if district.province.province_name:
                        parts.append(district.province.province_name)
                    if district.province.country and district.province.country.country_name:
                        parts.append(district.province.country.country_name)

        self.includes = ', '.join(parts)        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Service: {self.title} "


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
   image = models.ImageField(upload_to="service_images") 

   
class Post(models.Model):
   barber= models.ForeignKey(Barber,on_delete=models.CASCADE,related_name="posts")
   content = models.TextField(max_length=500)
   created_at = models.DateTimeField(auto_now=True)
   category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE ,   related_name='posts',
   )
   updated_at=models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f"{self.barber.first_name} {self.barber.last_name} : {self.content} "


class PostMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_medias')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='post_media') 
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
