import os
from uuid import uuid4

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models
from .forms import ImageUploadForm
from .models import ImageUpload
# from .caption_generator import generate_caption
# from .song_recommender import recommend_song
from django.urls import reverse


def home(request):
    return render(request, 'home/home.html')


def upload_image(request):
    return render(request, 'home/home.html')


def preview(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)  # DB에 바로 저장하지 않음
            # 임시 경로에 이미지를 저장
            response_data = {
                'image_url': image_instance.image.url
            }
            return JsonResponse(response_data)
    return render(request, 'home/home.html')


def save(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home/home.html')  # 성공 페이지로 render
    return redirect('failure')  # 실패 페이지로 redirect


def result(request):
    return render(request, 'home/result.html')
