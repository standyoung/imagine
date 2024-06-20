from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('upload', upload_image, name='upload_image'),
    path('result', result, name='result'),
    path('preview', preview, name='preview'),
]
