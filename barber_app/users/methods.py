from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.html import strip_tags
from django.core.cache import cache
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
import random
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
def send_verification_email(user):    
    ttl = cache.ttl(f"verify:{user.email}")    
    print('ttl: {ttl}')   
    if not ttl or ttl <= 0:            
        verification_code = str(random.randint(100000, 999999))
        cache.set(f'verify:{user.email}', verification_code, timeout=30)    
        context = {"email": user.email, "verification_code": verification_code}
        html_content = render_to_string("account/email/verify_email.html", context)
        plain_message = strip_tags(html_content)
        send_mail(
            subject="Doğrulama Kodu",
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            html_message=html_content,
        )  
        