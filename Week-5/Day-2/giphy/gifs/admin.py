from django.contrib import admin
from .models import Gif, Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)

admin.site.register(Gif)
admin.site.register(Category, CategoryAdmin)