"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/admin
    url(r'^admin/', admin.site.urls),
    #http://127.0.0.1:8000
    url(r'^$',views.index),
    url(r'^page(\d+)',views.page_view),
    #http://127.0.0.1:8000/100/add/200
    url(r'^(\d+)/(\w+)/(\d+)',views.cal),
    #http://127.0.0.1:8000/person/xiaoming/18
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
    url(r'^birthday/(\d+)/(\d+)/(\d+)',views.birthday_view)
]
