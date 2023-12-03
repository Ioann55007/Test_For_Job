from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from .models import PictureFile


class PictureSerializer(serializers.ModelSerializer):
    picture = Base64ImageField()

    class Meta:
        model = PictureFile
        fields = ('picture', 'description_picture')
