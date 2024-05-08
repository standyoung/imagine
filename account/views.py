
from django.views       import View
from django.http        import JsonResponse, HttpResponse
from django.shortcuts   import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# create한 login 함수랑 겹치면 안됨

from .models import User

# @require_http_methods(['GET', 'POST'])
# def signup(request):
#     User = get_user_model()
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)  # 데이터가 채워진 회원가입 form (binding form)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)  # 회원가입 후, 로그인까지 바로 진행
#             return redirect("account/login.html")
#     else:
#         form = UserCreationForm()  # 회원가입 form
#     context = {"form": form}
#     return render(request, "account/signup.html", context)

# Create your views here.
def logout(request):
    # return render(request, 'home/home.html')
    pass

def login(request):
    return render(request, 'account/login.html')

# 회원가입
def signup(request):
    # 로그인이 된 상태면 home으로
    # if request.user.is_authenticated:
    #     return redirect('home:home')

    if request.method == 'POST':
        user = User()
        user.uid=request.POST['uid']
        user.pwd=request.POST['pwd']
        user.name=request.POST['name']
        user.birth=request.POST['birth']
        user.gender=request.POST['gender']
        user.email=request.POST['email']
        user.save()
        # 회원가입 후, 로그인까지 바로 진행
        return render(request,'home/home.html')
    return render(request, 'account/signup.html')

def signup_done(request):
    pass