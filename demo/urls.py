__author__ = "quqiao"

# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path, re_path, include  # Django版本2.0以上
from demo import views
from django.conf.urls import url  # Django2.0
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'cards', views.CardViewSet)
urlpatterns = [
    # url(r'^demo_css/', views.demo_css),
    # url(r'^demo_js/', views.demo_js),
    # url(r'^demo_bootstrap/', views.demo_bootstrap),
    # path("archive/<year>/<month>.html", views.archive),
    # url(r'^', include(router.urls)),
    path('add_data', views.add_Data),
    path('query_data', views.query_Data),
    path('delete_data', views.delete_Data),
    path('modify_data', views.modify_Data),
    path('add_book', views.add_book),
    ]