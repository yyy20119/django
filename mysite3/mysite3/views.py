from django.http import HttpResponse
from django.shortcuts import render


def shebao(request):
    if request.method=='GET':
        return render(request,'shebao.html')
    elif request.method=='POST':
        base=int(request.POST.get('base'))
        if base>23118:
            base=23118
        if base<3082:
            base=3082
        is_city=request.POST.get('is_city')
        if is_city=='1':
            pass
        else:
            pass
        return HttpResponse('test is ok')

def test_url(request):
    return render(request,'test_url.html')

def page_view(request):
    return HttpResponse('This is page html')

def pagen_view(request,n):
    html='This is %s page html'%n
    return HttpResponse(html)

def test_static(request):
    return render(request,'test_static.html')














