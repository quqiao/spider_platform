__author__ = "quqiao"

# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path, include  # Django版本2.0以上
from demo import views
from django.conf.urls import url  # Django2.0

urlpatterns = [
    url(r'^demo_css/', views.demo_css),
    url(r'^demo_js/', views.demo_js),
    url(r'^demo_bootstrap/', views.demo_bootstrap),
    ]