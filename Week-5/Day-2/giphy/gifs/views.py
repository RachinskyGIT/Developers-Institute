from django.shortcuts import render
from .models import Gif, Category
from .forms import GifForm, CategoryForm
from django.http import HttpResponse


def Homepage(request): 

    gifs = Gif.objects.all()

    context = {'gifs': gifs}
    return render(request, 'Homepage.html', context)


def add_gif_view(request):
    
    if request.method == 'POST':
        print("POST data: ", request.POST)
        print('POSTING DATA')
        gif_filled_form = GifForm(request.POST) # put the data from the request into the ModelForm

        if gif_filled_form.is_valid(): # check if all fields contain the correct data
            # gif_filled_form.save().categories.add(Category.objects.get(name=gif_filled_form.cleaned_data['categories'])) # save data into database
            gif = gif_filled_form.save(commit=False)
            gif.save()
            gif.categories.set(gif_filled_form.cleaned_data['categories'])
            return HttpResponse("SUCCESSFULLY SAVED")


        else:
            print(gif_filled_form.errors)
            return HttpResponse(gif_filled_form.errors)

    # GET mode - getting content out
    if request.method == 'GET':
        gif_form = GifForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': gif_form}

    return render(request, 'add_gif.html', context)


def add_category_view(request):
    
    if request.method == 'POST':
        print("POST data: ", request.POST)
        print('POSTING DATA')
        category_filled_form = CategoryForm(request.POST) # put the data from the request into the ModelForm

        if category_filled_form.is_valid(): # check if all fields contain the correct data
            category_filled_form.save() # save data into database
            return HttpResponse("SUCCESSFULLY SAVED")


    if request.method == 'GET':
        category_form = CategoryForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': category_form}
    

    return render(request, 'add_category.html', context)

