"""mysite2 URL Configuration

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
    url(r'^admin/', admin.site.urls),
    #http://127.0.0.1:8000/index
    url(r'^index',views.index),
    #http://127.0.0.1:8000/test_p
    url(r'^test_p',views.test_p),
    url(r'^test_if',views.test_if),
    url(r'^mycal',views.mycal),
    url(r'^test_for',views.test_for),
    url(r'^base',views.base_view),
    url(r'^music',views.music_view),
    url(r'^sports',views.sports_view),

]
