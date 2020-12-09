from django.urls import path, re_path, include  # Django版本2.0以上
from DataAnalysis import views
from django.conf.urls import url  # Django2.0

urlpatterns = [
    # iframe
    # re_path('iframe/', views.iframe),
    url(r'^home/', views.home),
    url(r'^result_data', views.index_result),
    url(r'^toast1/', views.toast1),
    ]