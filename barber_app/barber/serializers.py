from rest_framework import serializers
from . import models

class ServiceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceComment
        fields = '__all__' 