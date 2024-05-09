from django.urls import path
from account.views import *
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),  #127.0.0.1:8000/account/login/
    path('signup/', views.signup, name='signup'),  # 127.0.0.1:8000/account/login/
    path('logout', views.logout, name='logout'),
]