# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:51:10 2016

@author: jin
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]