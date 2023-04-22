import json
import django
from django.conf import settings
import os
from faker import Faker

# Set the value of the environment variable DJANGO_SETTINGS_MODULE to 'animals.settings' if it is not already set.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animals.settings")

# Load the Django settings and set up the environment for Django.
# This should be called once at the beginning of every script that uses Django.
django.setup()


# Get the path to the JSON file relative to the Django project directory
json_file_path = os.path.join(settings.BASE_DIR, 'animals.json')

# Read data from JSON file
with open(json_file_path, 'r') as f:
    data = json.load(f)


fake = Faker()
# # Generate a new family object
# for i in range(len(data['families']), len(data['families'])+5):
#     new_family = {
#     'id': i,
#     'name': Faker().domain_word()
# }
#     if new_family not in data['families']:
#         data['families'].append(new_family) 

# Generate a new animal object
# new_animal = {
#     'id': len(data['animals']) + 1,
#     'name': fake.name(),
#     'legs': fake.random_int(min=2, max=10),
#     'weight': round(fake.uniform(0.1, 100), 2),
#     'height': round(fake.uniform(0.1, 10), 2),
#     'speed': fake.random_int(min=1, max=100),
#     'family': fake.random_int(min=1, max=len(data['families']))
# }
# # Append the new animal to the 'animals' list
# data['animals'].append(new_animal)

# # Write data back to JSON file
# with open(json_file_path, 'w') as f:
#     json.dump(data, f)

# print(data)
for i in range(5):
    new_animal = {
        'id': len(data['animals']) + 1,
        'name': fake.name(),
        'legs': fake.random_int(min=1, max=7),
        'weight': round(fake.pyfloat(min_value=0.1, max_value=100, right_digits=2), 2),
        'height': round(fake.pyfloat(min_value=0.1, max_value=10, right_digits=2), 2),
        'speed': fake.random_int(min=1, max=100),
        'family': fake.random_int(min=1, max=len(data['families']))
    }

    # Check if there is an existing animal with the same name in the same family
    for animal in data['animals']:
        if animal['name'] == new_animal['name'] and animal['family'] == new_animal['family']:
            print(f"There is already an animal with the name '{new_animal['name']}' in family '{data['families'][new_animal['family']-1]['name']}'")
            break
    else:
        # If there is no existing animal with the same name in the same family, add the new animal to the data
        
        data['animals'].append(new_animal)
        print(new_animal)
        # Write data back to JSON file
        with open(json_file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Added a new animal with the name '{new_animal['name']}' to family '{data['families'][new_animal['family']-1]['name']}'")

