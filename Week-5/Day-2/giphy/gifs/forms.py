from django import forms
from gifs.models import Gif, Category

# class GifForm(forms.Form):
#     uploader_name = forms.CharField(label='Your name', max_length=50)
#     title = forms.CharField(label='Title', max_length=100)
#     url = forms.URLField()
#     categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

#     class Meta:
#         model = Gif
#         fields = ('uploader_name', 'title', 'url', 'categories')

# class CategoryForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)

#     class Meta:
#         model = Category
#         fields = ('name')


class GifForm(forms.ModelForm):

    class Meta:
        model = Gif
        fields = ('title', 'url', 'uploader_name', 'categories')
        
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),  widget=forms.CheckboxSelectMultiple)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
        # fields = ('__all__')