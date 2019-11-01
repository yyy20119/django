from django.conf.urls import url

from note.views import *

urlpatterns = [
    url(r'^add$', add),
    url(r'^$', list),
    url(r'^del/(\d+)',del_view),
]