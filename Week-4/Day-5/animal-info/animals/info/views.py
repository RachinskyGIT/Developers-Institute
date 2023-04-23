from django.shortcuts import render
import json
from .models import Animal, Family
# import utils

# Create your views here.
def read_data(location: str, key: str):

    with open(location, 'r') as file:
        data = json.load(file)

    sub_data = data[key]
    return sub_data

def find_instance(data_list: list, id: int) -> dict:
    for instance in data_list:
        if instance['id'] == id:
            return instance
    return None

def all_animals(request): 

    animals = Animal.objects.all()

    context = {'animals': animals}
    return render(request, 'animals.html', context)

def animal(request, id: int):
    # animals = read_data('data.json', 'animals')
    # isinstance = find_instance(animals, id)

    # context = {'animal': isinstance}
    # return render(request, 'animal.html', context)
    animal = Animal.objects.get (id = id)
    return render (request, 'animal.html',{'animal': animal})

def speed(request): 

    animals = Animal.objects.all()

    context = {'animals': animals}
    return render(request, 'speed.html', context)