from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import BookStore, Book


# Create your views here.
def add_book(request):

    if request.method=='GET':
        return render(request,'bookstore/add_book.html')

    elif request.method=='POST':
        title=request.POST.get('title')
        if not title:
            return HttpResponse('数据有误 请退回重新填写')
        pub=request.POST.get('pub')
        price=request.POST.get('price')
        market_price=request.POST.get('m_price')
        #TODO pub price market_price 自行检查用户是否提交
        Book.objects.create(title=title,pub=pub,price=price,market_price=market_price)
        return HttpResponse('添加成功')

def all_book(request):
    all_book=Book.objects.all()
    return render(request,'bookstore/all_book.html',locals())

def detail(request,book_id):
    try:
        book=Book.objects.get(id=book_id)
    except Exception as e:
        return HttpResponse('您当前查询的书籍有误')
    return render(request,'bookstore/detail.html',locals())

def update_book(request,book_id):
    books=Book.objects.filter(id=book_id)
    if not books:
        return HttpResponse('当前所查阅书籍有误')
    if request.method!='POST':
        return HttpResponse('当前请求异常')
    market_price=request.POST.get('m_price')
    book=books[0]
    book.market_price=market_price
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')

def delete_book(request,book_id):
    try:
        book=Book.objects.get(id=book_id)
        book.delete()
    except Exception as e:
        return HttpResponse('您提交数据有误,请刷新当前页面后重试')
    return HttpResponseRedirect('/bookstore/all_book')