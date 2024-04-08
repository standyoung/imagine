from django.shortcuts import render
def index(request):
    return render(request,'app_default/templates/index.html')
