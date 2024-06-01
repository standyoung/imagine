from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('upload', upload, name='upload'),
    path('result', result, name='result'),
]