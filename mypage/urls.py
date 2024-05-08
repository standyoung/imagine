from django.urls import path
from mypage.views import *

app_name = 'mypage'

urlpatterns = [
    path('like', mypage_like, name='like'),
]
