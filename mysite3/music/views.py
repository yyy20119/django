from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse('音乐频道首页')
    return render(request,'music/index.html')


