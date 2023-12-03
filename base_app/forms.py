from django import forms
from .models import PictureFile


class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureFile
        fields = ('picture', 'description_picture')

