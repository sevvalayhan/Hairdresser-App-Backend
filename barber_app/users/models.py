from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, BaseUserManager  
from rest_framework_simplejwt.tokens import RefreshToken
 

class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, phone_number, password, **extra_fields)


class User(AbstractUser,):
    username= None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    ROLE_CHOICES = (
    ('customer', 'Customer'),
    ('barber', 'Barber'),
    ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')  
    @property 
    def is_barber(self):
        return self.role == 'barber'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text=('The groups this user belongs to.'),
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='custom_user_permissions',
    )
    objects = CustomUserManager()
    def tokens(self):    
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token),          
        }
    def get_user(self):
        return{
            "email":self.email,
            "phone_number":self.phone_number,             
        }
     
  

    def __str__(self):
        return f"{self.email,self.is_barber,str(self.role)}"

from django.db import models
from django.utils import timezone
from datetime import timedelta

class VerificationCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=90)

    def __str__(self):
        return f"{self.email} - {self.code}"


from django.conf import settings

class Following(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followings')
   barber = models.ForeignKey("barber.Barber", on_delete=models.CASCADE, related_name='followers')
   created_at = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return f"User: {self.user.email} {self.user.phone_number} Follows :{self.barber.first_name} {self.barber.last_name}"


