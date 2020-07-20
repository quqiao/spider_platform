# from django.shortcuts import render
#
# # Create your views here.
import requests
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
import os
from spider_platform import settings
import json
import ahttp
from target_page.web_page import hezongyy_py, ysb_lyg
from target_page.models import hezongyy_py1, ysb_lyg1
from lxml import etree


def home(request):
    return render(request, 'home.html')

def result_home(request):
    if request.method == 'GET':
        r = request.GET["empty"]
        # html = etree.parse(r, etree.HTMLParser())
        # result = etree.tostring(html)
        # print(r)
        # ssr = json.loads(r)
        # print(ssr)
        return HttpResponse(r)

    else:
        return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')

def index_result(request):
    if request.method == 'GET':
        r = request.GET["url"]  # key就是前面输入框里的name属性对应值name="q"
        c = request.GET["number"]
        if "hezongyy.com/puyao" in r:
            hezongyy_py.crawl_hezongyy(int(c))  # 调用采集数据
            hezongyy_py.save_mysql()  # 调用保存到数据库中
            users = hezongyy_py1.objects.all()  # 数据库中读取数据
            return render(request, 'hezongyy_py.html', {'users': users})
        if r == "ysbang":
            ysb_lyg.crawl_hezongyy(int(c))  # 调用采集数据
            ysb_lyg.save_csv()  # 调用保存到数据库中
            # users = ysb_lyg1.objects.all()  # 数据库中读取数据
            # return render(request, 'ysb_lyg.html', {'users': users})
            return HttpResponse("抓取结果：完成")
        else:
            return HttpResponseRedirect("/get_demo")
    else:
        render(request, 'index.html')

def iframe(request):
    if request.method == "GET":
        return render(request, 'iframe.html')
    elif request.method == "POST":
        import time
        time.sleep(3)
        print(request.POST)
        ret = {'code': True, 'data': request.POST.get('username')}
        import json
        return HttpResponse(json.dumps(ret))


def toast(request):
    messages.success(request, "暂时无法抓取该url,请返回重新输入")
    return render(request, 'get_demo.html')

def toast2(request):
    messages.success(request, "暂时无法抓取该url,请返回重新输入")
    return render(request, 'index.html')


def demo_css(request):
    return render(request, 'demo_css.html')

def demo_js(request):
    return render(request, 'demo_js.html')
