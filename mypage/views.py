from django.shortcuts import render, redirect

# Create your views here.
def mypage_like(request):
    return render(request, 'mypage/like.html')
