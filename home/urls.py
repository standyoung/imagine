from django.urls import path
from . import views
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
]
