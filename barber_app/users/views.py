from rest_framework import generics
from .models import User
from .methods import send_verification_email 
from .serializers import UserSerializer, MyTokenObtainPairSerializer ,VerifyCodeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.utils import timezone  
from django.conf import settings

class UserRegistrationView(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                return Response({"error": "Bu e-posta ile zaten kayıtlısınız.","is_active":user.is_active}, status=status.HTTP_400_BAD_REQUEST)
            if user.check_password(password):                 
                send_verification_email(user)
                return Response({
                    "message": "Zaten kayıtlısınız ancak henüz hesabınızı aktifleştirmediniz. Doğrulama kodu tekrar gönderildi.","is_active":user.is_active
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Bu e-posta ile kayıtlı bir kullanıcı var. Şifre eşleşmiyor.","is_active":user.is_active}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass  

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_verification_email(user)

        return Response({
            "message": "Doğrulama kodu e-postanıza gönderildi.",
            "is_active":user.is_active
        }, status=status.HTTP_200_OK)


User = get_user_model()

class VerifyEmailCodeView(APIView):
    def post(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        user = User.objects.get(email=request.data["email"])
        tokens =  user.tokens()
        return Response({
            "message": "Doğrulama başarılı.",
            "token": tokens
        }, status=200)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)        
        if user is not None:
            if user.is_active ==False:             
                send_verification_email(user) 
                return Response({
                "message": "lütfen doğrulama işlemi için size gelen kodu girin"   ,
                "is_active": user.is_active,
                "is_barber": user.is_barber         
                },status= status.HTTP_200_OK)   
                                         
            user = authenticate(email=email, password=password)    
            tokens = user.tokens()
            get_user = user.get_user()
            return Response({
                "token": tokens,
                "user":get_user,
                "is_active": user.is_active,
                "is_barber": user.is_barber   
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({"error": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(str(refresh_token))
            token.blacklist()
            return Response({"message": "Successfully logged out!"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
   
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello, {request.user.email}!"})

from rest_framework_simplejwt.views import TokenObtainPairView
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    username_field = User.email