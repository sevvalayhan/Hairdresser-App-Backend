from django.urls import path
from . import views

urlpatterns = [
    path('get-addresses', views.AddressListView.as_view(), name='get_addresses')
]