from django.db import models


class PictureFile(models.Model):
    objects = models.Manager()
    picture = models.ImageField(upload_to='')
    description_picture = models.TextField()

