from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ImageUpload
# from .caption_generator import generate_caption
# from .song_recommender import recommend_song



def home(request):
    return render(request, 'home/home.html')

def upload(request):
    if request.method == 'POST':
        img = request.FILES["img"]

        return render(request, 'home/result.html')

    return render(request, 'home/home.html')

