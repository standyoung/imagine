from django.urls import path, include
from accounts.views import *
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),  #127.0.0.1:8000/accounts/login/
    path('signup/', views.signup, name='signup'),  # 127.0.0.1:8000/accounts/login/
    path('logout', views.logout, name='logout'),
    # path('accounts/', include('allauth.urls')),
    # path('google/', views.google_login, name='google'),
]