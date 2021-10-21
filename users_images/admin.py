from django.contrib import admin
from .models import Image

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'image_name', 'date', 'image_path', 'image_field']
    list_filter = ['user']


admin.site.register(Image, ImageAdmin)
