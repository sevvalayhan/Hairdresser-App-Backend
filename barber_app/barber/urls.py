from django.urls import path
from . import views
urlpatterns = [
    path('get-service-comments', views.ServiceCommentListView.as_view(), name='get_service_comments'),
    path('get-service', views.ServiceListView.as_view(), name='get_service'),
    path('get-service-like', views.ServiceLikeListView.as_view(), name='get_service_like'),
    path('get-barber', views.BarberListView.as_view(), name='get_barber'),
    path('get-category', views.CategoryListView.as_view(), name='get_category'),
    path('get-post', views.PostListView.as_view(), name='get_post'),
    path('get-post-media', views.PostMediaListView.as_view(), name='get_post_media'),
    path('get-post-like', views.PostLikeListView.as_view(), name='get_post_like'),
    path('get-post-comment', views.PostCommentListView.as_view(), name='get_post_comment'),
]