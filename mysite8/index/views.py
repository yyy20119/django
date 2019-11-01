import csv
import os

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from index.models import Book


def mymiddle(request):

    print('----------views start-----------')


    return HttpResponse('test is ok')

def book(request):
    all_books=Book.objects.all()
    paginator=Paginator(all_books,2)
    current_page=request.GET.get('page',1)
    page=paginator.page(current_page)
    return render(request,'index/book.html',locals())

def book_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment:filename=book.csv'
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 2)
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)

    writer=csv.writer(response)
    writer.writerow(['id','title'])
    for book in page:
        writer.writerow([book.id,book.title])
    return response



def test_upload(request):
    if request.method=='GET':
        return render(request,'index/test_upload.html')
    elif request.method=='POST':
        myfile=request.FILES['myfile']
        file_path=os.path.join(settings.MEDIA_ROOT,myfile.name)
        with open(file_path,'wb') as f:
            data=myfile.file.read()
            f.write(data)

        return HttpResponse('上传成功')

