from django.shortcuts import render
from .models import Gif, Category


def Homepage(request): 

    gifs = Gif.objects.all()

    context = {'gifs': gifs}
    return render(request, 'Homepage.html', context)

# def search(model, value):

#     result = None
#     try:
#         model_instance = model.objects.get(name = value)
#         result = model_instance
#     except model.DoesNotExist:
#         pass
#     try:
#         model_instance = model.objects.get(phone_number = value)
#         result = model_instance
#     except model.DoesNotExist:
#         pass

#     return result


# def search_person(request, search_value: str):

#     context = {}

#     person_info = search(Person,  search_value)

#     if person_info is not None:
#         context = {'person': person_info}

#     return render(request, 'person_info.html', context)


# def profile_view(request, search_value: str):

#     context = {}

#     person_info = search(Person,  search_value)

#     if person_info is not None:
#         person_profile = person_info.profile
        
#         profile_languages = person_profile.languages.all().order_by('name')

#         context = {'person_info': person_info, 'person_profile': person_profile, 'languages': profile_languages}

#     return render(request, 'profile.html', context)

