from django.urls import path
from .views import UserRegistrationView,LoginView,LogoutView,ProtectedView,VerifyEmailCodeView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'), 
    path('verify-code/',VerifyEmailCodeView.as_view(),name='verify_email'), 
    path('login/',LoginView.as_view(),name='login'), 
    path('logout/',LogoutView.as_view(),name='logout'), 
    path('protected/',ProtectedView.as_view(),name='protected'), 
]