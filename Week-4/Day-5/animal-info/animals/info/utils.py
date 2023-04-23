from django.shortcuts import render
import json

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

    animals = read_data('data.json', 'animals')
    context = {'animals': animals}

    return render(request, 'animals.html', context)


def animal(request: HttpRequest, id: int):
    animals = read_data('data.json', 'animals')
    isinstance = find_instance(animals, id)

    context = {'animal': isinstance}

    return render(request, 'animal.html', context)