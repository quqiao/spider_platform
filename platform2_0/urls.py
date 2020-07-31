__author__ = "quqiao"

# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path, include  # Django版本2.0以上
from platform2_0 import views
from django.conf.urls import url  # Django2.0

urlpatterns = [
    # iframe
    re_path('iframe/', views.iframe),
    url(r'^home', views.home),
    url(r'^result_home', views.result_home),
    ]