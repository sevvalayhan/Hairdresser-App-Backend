from django.urls import path
from . import views

urlpatterns = [
    path('get-service-comments', views.ServiceCommentListView.as_view(), name='get_service_comments')
]