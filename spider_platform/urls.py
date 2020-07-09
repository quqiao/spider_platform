"""spider_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from target_page import views
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home', views.home),
    url(r'^result_home', views.result_home),
    url(r'^index/', views.index),
    url(r'^result_index', views.index_result),
    url(r'^hezongyy_py/', views.index_result),
    url(r'^get_demo/', views.toast),
    url(r'^demo/', views.demo),
    # url(r'^login', views.demo),
    re_path('submit/', include("target_page.urls")),

    # url(r'^qq/', views.test_qq),
    # url(r'^result/', views.result_qq),
]
