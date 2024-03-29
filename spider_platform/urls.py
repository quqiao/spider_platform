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
from django.urls import path, re_path, include
from platform1_0 import views
from django.conf.urls import url  # Django2.0


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('platform1/', include("platform1_0.urls")),  # 爬虫抓取框架1.0版本
    re_path('platform2/', include("platform2_0.urls")),  # 爬虫抓取框架2.0版本
    re_path('demo/', include("demo.urls")),  # django 练习的版本
    re_path('DataAnalysis/', include("DataAnalysis.urls")),  # 抓取数据分析
]
