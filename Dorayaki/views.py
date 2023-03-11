from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    cardItems = [
        {
            "name": "cat",
            "nums": [3.14, 2.72],
            "descriptions": ["Description", "Description"],
            "img": "Dorayaki/images/cat_img.png",
            "audio": "Dorayaki/audios/cat_sound.mp3"
        },
        {
            "name": "dog",
            "nums": [3.14, 2.72],
            "descriptions": ["Description", "Description"],
            "img": "Dorayaki/images/dog_img.png",
            "audio": "Dorayaki/audios/dog_sound.mp3"
        },
        {
            "name": "duck",
            "nums": [3.14, 2.72],
            "descriptions": ["Description", "Description"],
            "img": "Dorayaki/images/duck_img.png",
            "audio": "Dorayaki/audios/duck_sound.mp3"
        },
        {
            "name": "cow",
            "nums": [3.14, 2.72],
            "descriptions": ["Description", "Description"],
            "img": "Dorayaki/images/cow_img.png",
            "audio": "Dorayaki/audios/cow_sound.mp3"
        },
        {
            "name": "sheep",
            "nums": [3.14, 2.72],
            "descriptions": ["Description", "Description"],
            "img": "Dorayaki/images/sheep_img.png",
            "audio": "Dorayaki/audios/sheep_sound.mp3"
        },
        {
            "name": "pig",
            "nums": [3.14, 2.72],
            "descriptions": ["Description", "Description"],
            "img": "Dorayaki/images/pig_img.png",
            "audio": "Dorayaki/audios/pig_sound.mp3"
        }
    ]
    return render(request, "Dorayaki/index.html", {
        "cardItems": cardItems
    })