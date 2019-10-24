from django.http import HttpResponse

post_html='''
<form method='post' action="/birthday/1995/7/1">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>
'''

def index(request):
    html='<h1>这是我的首页<h1>'
    return HttpResponse(html)

def page_view(request,n):


    print(request.GET.getlist('a'))
    html='<h1>这是编号为%s的网页</h1>'%n

    print(dict(request.GET))
    return HttpResponse(post_html)

def cal(request,a,s,b):
    res=0
    a=float(a)
    b=float(b)
    if s=='add':
        res=a+b
    elif s=='sub':
        res=a-b
    elif s=='mul':
        res=a*b
    return HttpResponse(res)

def person_view(request,name,age):
    res='姓名:'+name
    res+=' 年龄:'+age
    return HttpResponse(res)

def birthday_view(request,a,b,c):
    res = ''
    if request.method=='POST':
        res+=request.POST.get('username')

    if len(a)==4:
        res+='生日为: %s年%s月%s日'%(a,b,c)
    else:
        res+='生日为: %s年%s月%s日'%(c,b,a)
    return HttpResponse(res)