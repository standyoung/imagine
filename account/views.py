from django.contrib.auth.forms import AuthenticationForm
from django.forms import model_to_dict
from django.views       import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts   import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# create한 login 함수랑 겹치면 안됨

from .models import User

# Create your views here.
def logout(request):
    auth_logout(request)
    return redirect('/')

def login(request):
    response_data = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') # 아이디 비밀번호 입력받은 것 확인
        userObject = auth_authenticate(request=request,username=username,password=password)

        if userObject is not None:
            print(userObject)
            auth_login(request, userObject)
        else:
            print("Authentication failed")
            # 실패 원인 확인을 위해 사용자 목록 출력 (보안상 실제 배포에서는 사용하지 마세요)
            all_users = User.objects.all()
            print("Existing users:", [u.username for u in all_users])
            print("Existing users:", [u.password for u in all_users])

            return render(request, 'account/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'account/login.html')
    return render(request, 'home/home.html')



# 회원가입
def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')

    elif request.method == 'POST':
        # 입력 데이터 user 객체에 저장
        user = User(
            username=request.POST['username'],
            password=request.POST['password'],
            # pwd=make_password(request.POST['pwd']),
            nickname=request.POST['nickname'],
            birth=request.POST['birth'],
            gender=request.POST['gender'],
            email=request.POST['email']+"@"+request.POST['email-detail']
        )
        user.save()

        # 회원가입 후, 로그인까지 바로 진행
        return render(request,'home/home.html')
    return render(request, 'account/signup.html')

def signup_done(request):
    pass