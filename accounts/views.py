from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

# create한 login 함수랑 겹치면 안됨
from django.contrib.auth import login as auth_login

from django.contrib.auth.hashers import make_password

from .models import User


# Create your views here.
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        print("Logged out successfully")
    return redirect('/')


def login(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')

    elif request.method == 'POST':
        errMsg = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"username : {username}, password : {password}")
        user = authenticate(request, username=username, password=password)

        # 로그인 성공
        if user is not None:
            auth_login(request, user)
            print("logged in successfully")
            return redirect('home:home')

        # 로그인 실패
        else:
            errMsg = {"로그인을 실패했습니다."}
            print("login failed")
            return render(request, 'account/login.html', errMsg)


# 회원가입
def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')

    elif request.method == 'POST':
        # 입력 데이터 user 객체에 저장
        user = User(
            username=request.POST['username'],
            password=make_password(request.POST['password']),
            nickname=request.POST['nickname'],
            birth=request.POST['birth'],
            gender=request.POST['gender'],
            email=request.POST['email'] + "@" + request.POST['email-detail']
        )
        user.save()

        # 회원가입 후, 로그인 진행
        new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if new_user is not None:
            auth_login(request, new_user)
            return redirect('home:home')  # 홈으로 이동


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect


def google_login(request):
    pass
#     client_id = CLIENT_ID
#     return redirect(f"{GOOGLE_REDIRECT}?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")
