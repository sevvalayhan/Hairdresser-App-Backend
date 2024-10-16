from django.urls import path
from . import views

urlpatterns = [
    path('getcustomer', views.get_customer, name='get_customer')
]