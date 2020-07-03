__author__ = "quqiao"

# !/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path, re_path  # Django版本2.0以上
from target_page import views
from django.conf.urls import url  # Django2.0

app_name = 'namespace'
urlpatterns = [
    # iframe
    re_path('iframe/', views.iframe),
    ]
