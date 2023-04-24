from django.db import models
import datetime as dt

class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'gifs'


class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField('Gif', related_name='categories')
    class Meta:
        app_label = 'gifs'

