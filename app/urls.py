from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib import admin
import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^get-prime-factors/$', views.prime_factors, name='prime-factors'),
)