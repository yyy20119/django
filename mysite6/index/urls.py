from django.conf.urls import url

from index.views import *

urlpatterns = [
    url(r'^set_cookies$',set_cookies),
    url(r'^get_cookies$',get_cookies),
    url(r'^set_session$',set_session),
    url(r'^get_session$',get_session),
    url(r'^test_cache$',test_cache),
    url(r'^test_csrf$',test_csrf),
]