from random import randrange
import requests
import json
import os

Smile_url = os.getenv('GIPHY_API_SMILE')

def kick():
    
    kick=['https://media.giphy.com/media/u2LJ0n4lx6jF6/giphy.gif','https://media.giphy.com/media/qiiimDJtLj4XK/giphy.gif','https://media.giphy.com/media/l2QE2CQyK2ZyVEGJy/giphy.gif',
        'https://media.giphy.com/media/l1J3AS8RShMebsmgU/giphy.gif','https://media.giphy.com/media/MU1gQlfzyi7qE/giphy.gif','https://media.giphy.com/media/3o7OswTkQnFNyxZmNy/giphy.gif']

    random_index = randrange(len(kick))
    kick1=kick[random_index]
    return kick1

def smile():
    page=requests.get(Smile_url)
    data=page.json()
    return(data["data"]["url"])
