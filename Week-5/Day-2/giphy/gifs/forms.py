from django import forms
from gifs.models import Gif, Category

class GifForm(forms.Form):
    uploader_name = forms.CharField(label='Your name', max_length=50)
    title = forms.CharField(label='Title', max_length=100)
    url = forms.URLField()
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Gif
        fields = ('uploader_name', 'title', 'url', 'categories')

class CategoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)

    class Meta:
        model = Category
        fields = ('name')