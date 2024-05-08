from django.urls import path
from django.contrib.auth import views as auth_views
from account.views import *

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),  #127.0.0.1:8000/account/login/
    path('signup/', signup, name='signup'),  # 127.0.0.1:8000/account/login/
]