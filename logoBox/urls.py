__author__ = '0701052m'

from django.conf.urls import patterns, url
from logoBox import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),

        #url(r'^')
        )