from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    # t=loader.get_template('test.html')
    # html=t.render()
    # return HttpResponse(html)

    dic={'username':'guoxiaonao','age':18}
    return render(request,'test.html',dic)

def test_p(request):
    dic={}
    dic['lst']=['小红','小明','小兰']
    dic['dict']={'username':'guoxiaonao','age':18}
    dic['class_obj']=Dog()
    dic['say_hi']=say_hi
    return render(request,'test_p.html',dic)

class Dog:
    def say(self):
        return 'hahaha'

def say_hi():
    return 'hello'

def test_if(request):
    #/test_if?x=1
    x=int(request.GET.get('x',0))
    dic={'x':x}
    return render(request,'test_if.html',dic)


def mycal(request):
    if request.method=='GET':
        return render(request, 'mycal.html')
    elif request.method=='POST':
        x = request.POST.get('x')
        if not x:
            error='Please give me x!!'
            dic={'error':error}
            return render(request,'mycal.html',dic)
        try:
            x=int(x)
        except Exception as e:
            print('x is error')
            print(x)
            try:
                x=int(float(x))
            except Exception as e:
                error='The x is must be number'
                dic={'error':error}
                return render(request,'mycal.html',dic)

        y = int(request.POST.get('y'))
        op=request.POST.get('op')
        result=999999999999999
        if op=='add':
            result=x+y
        elif op=='sub':
            result=x-y
        elif op=='mul':
            result=x*y
        elif op=='div':
            result=x/y

        return render(request,'mycal.html',locals())

def test_for(request):
    lst=['小红','小兰','小绿']
    return render(request,'test_for.html',locals())

def base_view(request):

    lst=['哈哈','嘿嘿']
    return render(request,'base.html',locals())

def music_view(request):
    lst = ['哈哈', '嘿嘿']
    return render(request,'music.html',locals())

def sports_view(request):
    return render(request,'sports.html')










