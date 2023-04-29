"""This script automaticly inserts N gifs for all website's categories"""

import os
import django
import requests

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'giphy.settings')

# Initialize Django
django.setup()

from gifs.models import Category, Gif
categories = Category.objects.all()

how_many_gifs=10
#how many gifs we inserting for each category
for i in range(how_many_gifs):
    # Retrieve from GIPHY 1 random GIF for each category 
    for category in categories:
        response = requests.get(f'https://api.giphy.com/v1/gifs/random?api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&tag={category.name}&rating=G&limit=10')
        
        # Create Gif objects and associate them with the category
        gifs_title = response.json()['data']['title']
        gifs_url = response.json()['data']["images"]["original"]["webp"]
        gif = Gif.objects.create(
            uploader_name = 'admin',
            title =gifs_title,
            url = gifs_url,
        )
        gif.categories.add(category)
        
