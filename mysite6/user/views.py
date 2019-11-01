from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
# Create your views here.



def reg(request):
    if request.method=='GET':
        return render(request,'user/register.html')

    elif request.method=='POST':
        username=request.POST.get('username')
        if not username:
            return HttpResponse('请输入用户名')
        password_1=request.POST.get('password_1')
        password_2=request.POST.get('password_2')
        if not password_1 or not password_2:
            return HttpResponse('请输入密码')
        if password_1!=password_2:
            return HttpResponse('两次输入密码不一致')
        old_users=User.objects.filter(username=username)
        if old_users:
            return HttpResponse('当前用户名已注册')
        try:
            user=User.objects.create(username=username,password=password_1)
        except Exception as e:
            print('reg error')
            return HttpResponse('当前用户名已注册')

        resp=HttpResponse('注册成功')
        resp.set_cookie('username',username,3600*24)
        resp.set_cookie('uid',user.id,3600*24)
        return resp

    return HttpResponse('test is ok')

def login(request):
    if request.method=='GET':
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponseRedirect('/user/index')
        if 'username' in request.COOKIES and 'uid' in request.COOKIES:
            request.session['username']=request.COOKIES['username']
            request.session['uid']=request.COOKIES['uid']
            return HttpResponseRedirect('/user/index')

        return render(request,'user/login.html')
    elif request.method=='POST':
        save_cookies=False
        if 'save_cookies' in request.POST.keys():
            save_cookies=True

        username=request.POST.get('username')
        if not username:
            dic={'msg':'请提交用户名'}
            return render(request,'user/login.html',dic)
        password=request.POST.get('password')
        if not password:
            dic={'msg':'请提交密码'}
            return render(request, 'user/login.html', dic)
        user=User.objects.filter(username=username)
        if not user:
            print('---user login %s 用户名不存在'%username)
            dic={'msg':'用户名或密码错误'}
            return render(request,'user/login.html', dic)
        if user[0].password!=password:
            print('---user login %s 密码不正确'%username)
            dic={'msg':'用户名或密码错误'}
            return render(request, 'user/login.html', dic)
        request.session['username']=username
        request.session['uid']=user[0].id
        resp=HttpResponseRedirect('/user/index')
        if save_cookies:
            resp.set_cookie('username',username,60*60*24*30)
            resp.set_cookie('uid',user[0].id,60*60*24*30)
        return resp

def index(request):
    print('--------user index----------')
    print(request.session.get('username'))
    print(request.session.get('uid'))
    if 'username' in request.session and 'uid' in request.session:
        is_login=True
        username=request.session['username']
    else:
        is_login=False
    print(is_login)
    print('--------user index over-----------')
    return render(request,'user/index.html',locals())

def logout(request):
    if 'username' in request.session and 'uid' in request.session:
        del request.session['username']
        del request.session['uid']

    resp=HttpResponseRedirect('/user/index')
    if 'username' in request.COOKIES and 'uid' in request.COOKIES:
        resp.delete_cookie('username')
        resp.delete_cookie('uid')
    return resp





















