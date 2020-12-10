from django.urls import path, re_path, include  # Django版本2.0以上
from DataAnalysis import views
from django.conf.urls import url  # Django2.0

urlpatterns = [
    # iframe
    # re_path('iframe/', views.iframe),
    url(r'^query_name/', views.query_name),
    url(r'^query_manufacturer/', views.query_manufacturer),
    url(r'^query_name_manufacturer/', views.query_name_manufacturer),
    url(r'^query_name_result', views.query_name_result),
    url(r'^query_manufacturer_result', views.query_manufacturer_result),
    url(r'^query_name_manufacturer_result', views.query_name_manufacturer_result),
    url(r'^toast1/', views.toast1),
    ]