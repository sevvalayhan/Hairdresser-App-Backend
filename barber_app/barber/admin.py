from django.contrib import admin
from . import models

admin.site.register(models.Barber)
admin.site.register(models.Category)
admin.site.register(models.Service)
admin.site.register(models.ServiceImage)
admin.site.register(models.ServiceComment)
admin.site.register(models.ServiceLike)
admin.site.register(models.Post)
admin.site.register(models.PostMedia)
admin.site.register(models.PostComment)
admin.site.register(models.PostLike)