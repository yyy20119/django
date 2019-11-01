from django.conf.urls import url

from user import views


urlpatterns = [
    url(r'^reg$', views.reg),
    url(r'^login$', views.login),
    url(r'^index$', views.index),
    url(r'^logout$', views.logout),


]