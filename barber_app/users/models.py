from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, first_name, last_name, password, **extra_fields)


# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=75)
#     last_name = models.CharField(max_length=75)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_set',  # Çakışmayı önlemek için related_name ekleyin
#         blank=True,
#         help_text=('The groups this user belongs to.'),
#         related_query_name='custom_user',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions_set',  # Çakışmayı önlemek için related_name ekleyin
#         blank=True,
#         help_text=('Specific permissions for this user.'),
#         related_query_name='custom_user_permissions',
#     )

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     objects = CustomUserManager()

#     def __str__(self):
#         return f"{self.username}"
    

class Following(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')
   barber = models.ForeignKey("barber.Barber", on_delete=models.CASCADE, related_name='followers')
   created_at = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return f"User: {self.user.first_name} {self.user.last_name} Follows :{self.barber.first_name} {self.barber.last_name}"


