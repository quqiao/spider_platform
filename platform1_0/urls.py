__author__ = "quqiao"

# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path, include  # Django版本2.0以上
from platform1_0 import views
from django.conf.urls import url  # Django2.0
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('index/', views.index),
    url(r'^result_index', views.index_result),
    url(r'^hezongyy_py/', views.index_result),
    url(r'^longyi_tjzq/', views.index_result),
    url(r'^longyi_yp/', views.index_result),
    url(r'^scjuchuang_py/', views.index_result),
    url(r'^ypzdw_jtj/', views.index_result),
    url(r'^scytyy_ypzq/', views.index_result),
    url(r'^toast1/', views.toast1),
    url(r'^toast2/', views.toast2),
    url(r'^toast3/', views.toast3),
    url(r'^toast4/', views.toast4),
    ]
