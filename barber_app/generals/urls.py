from django.urls import path
from . import views

urlpatterns = [
    path('get-addresses', views.AddressListView.as_view(), name='get_addresses'),
    path('get-country', views.CountryListView.as_view(), name='get_country'),
    path('get-province', views.ProvinceListView.as_view(), name='get_province'),
    path('get-district', views.DistrictListView.as_view(), name='get_district'),
    path('get-phonenumber', views.PhoneNumberListView.as_view(), name='get_phonenumber'),
]