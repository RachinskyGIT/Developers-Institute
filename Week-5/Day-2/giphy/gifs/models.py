from django.db import models
import datetime as dt

class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    # categories = models.ManyToManyField('Category', related_name='gif_categories')


    class Meta:
        app_label = 'gifs'

    def __str__(self):
        return f'{self.title}, {self.uploader_name}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(Gif, related_name='categories', blank=True)
    # gifs = models.ManyToManyField(Gif, related_name='category_gifs',  blank=True)

    
    class Meta:
        app_label = 'gifs'

    def __str__(self) -> str:
        return f'{self.name}'
    