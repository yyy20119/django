from django.conf.urls import url

from . import views

#file:sports/urls.py
urlpatterns=[
    url(r'^index$',views.index)

]