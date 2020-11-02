from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.


def demo_css(request):
    return render(request, 'demo_css.html')

def demo_js(request):
    return render(request, 'demo_js.html')

def demo_bootstrap(request):
    return render(request, 'demo_bootstrap.html')

def archive(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))