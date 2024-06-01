from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ImageUploadForm
from .models import ImageUpload
# from .caption_generator import generate_caption
# from .song_recommender import recommend_song



def home(request):
    return render(request, 'home/home.html')

def upload(request):
    if request.method == 'POST':
        fileName = request.POST['filename']
        img = request.FILES.get("img")
        caption = request.POST['caption']

        if request.FILES.get("img") is not None:
            ImageUpload.file=request.FILES.get("img")

        imageupload = ImageUpload(
            filename=fileName,
            img=img,
            caption=caption,
        )

        imageupload.save()
        return redirect(request, 'home:upload')
    else:
        imageUploadForm = ImageUploadForm
        context = {'imageUploadForm': imageUploadForm}

        return render(request, 'home/home.html')

def result(request):
    return render(request, 'home/result.html')

