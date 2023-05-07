from django.contrib import admin
from .models import Director, Film


# class CategoryAdmin(admin.ModelAdmin):
#     fields = ('name',)

admin.site.register(Director)
admin.site.register(Film) #, CategoryAdmin