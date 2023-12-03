from django.contrib import admin

from .models import PictureFile


@admin.register(PictureFile)
class PictureAdmin(admin.ModelAdmin):
    fields = ('picture', 'description_picture')

