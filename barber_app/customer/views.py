from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from . import models 

def get_customer(request):
    try:
        _user = User.objects.get(username="sevval")
        customer = models.Customer.objects.get(user=_user)
        user_data = {
            'id': customer.user.id,
            'firstname':customer.first_name,
            'lastname':customer.last_name,            
            'username': customer.user.username,
            'email': customer.user.email,
        }

        return JsonResponse({'user': user_data})

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)