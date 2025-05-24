from django import forms
from .models import User, Following

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password', 'first_name', 'last_name']


class FollowingForm(forms.ModelForm):
    class Meta:
        model = Following
        fields = ['user', 'barber']
     
 