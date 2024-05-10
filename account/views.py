from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts   import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login

from django.forms import model_to_dict
from django.contrib import auth


from .forms import AccountAuthForm
# create한 login 함수랑 겹치면 안됨

from .models import User

# Create your views here.
def logout(request):
    if request.method == 'POST':
        auth.auth_logout(request)
    return redirect('/')

def login(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')

    elif request.method == 'POST':
        errMsg = {}
        username = request.POST['username']
        password = request.POST['password']
        # user = auth.authenticate(username=username, password=password)
        user = User.objects.get(username=username)
        # if user is not None:
        #     auth_login(request, user)

        # 로그인 성공
        if user.password == password:
            request.session['me'] = user.username
            return redirect('home:home')
        # 로그인 실패
        else :
            return render(request, 'home/home.html', errMsg)

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

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect
