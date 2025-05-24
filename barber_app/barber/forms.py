from django import forms
from .models import Barber, Category, Service, ServiceComment, ServiceLike, ServiceImage, Post, PostMedia, PostLike, PostComment

class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = ['user', 'identity_number', 'first_name', 'last_name', 'bio', 'email', 'profile_image', 'identity_card', 'status', 'is_improved','categories']
    widgets = {
            'categories': forms.CheckboxSelectMultiple(),  # Checkbox widget kullanımı
        }
  
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['barber', 'title', 'description', 'duration', 'price']

class ServiceCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceComment
        fields = ['user', 'service', 'comment_text']

class ServiceLikeForm(forms.ModelForm):
    class Meta:
        model = ServiceLike
        fields = ['user', 'service']

class ServiceImageForm(forms.ModelForm):
    class Meta:
        model = ServiceImage
        fields = ['service', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['barber', 'content', 'category']

class PostMediaForm(forms.ModelForm):
    class Meta:
        model = PostMedia
        fields = ['post', 'media_type', 'file']

class PostLikeForm(forms.ModelForm):
    class Meta:
        model = PostLike
        fields = ['post', 'user']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['post', 'user', 'content']
