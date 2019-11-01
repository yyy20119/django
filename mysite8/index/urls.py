from django.conf.urls import url

from index import views

urlpatterns=[
    url(r'^mymiddle$',views.mymiddle),
    url(r'^book$',views.book),
    url(r'^test_upload$',views.test_upload),
    url(r'^book_csv$',views.book_csv)
]