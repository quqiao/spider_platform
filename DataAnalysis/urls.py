from django.urls import path, re_path, include  # Django版本2.0以上
from DataAnalysis import views
from django.conf.urls import url  # Django2.0

urlpatterns = [
    # iframe
    # re_path('iframe/', views.iframe),
    path('query_name/', views.query_name),
    path('query_manufacturer/', views.query_manufacturer),
    path('query_name_manufacturer/', views.query_name_manufacturer),
    path('query_name_result', views.query_name_result),
    path('query_manufacturer_result', views.query_manufacturer_result),
    path('query_name_manufacturer_result', views.query_name_manufacturer_result),
    path('toast1/', views.toast1),
    ]