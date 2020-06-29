# from django.shortcuts import render
#
# # Create your views here.
import requests
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
import ahttp
from target_page.web_page import hezongyy_py
from target_page.models import hezongyy_py1

def index(request):
    return render(request, 'index.html')

def index_result(request):
    if request.method == 'GET':
        r = request.GET["url"]  # key就是前面输入框里的name属性对应值name="q"
        c = request.GET["number"]
        if r == "www":
            hezongyy_py.crawl_hezongyy(int(c))  # 调用采集数据
            hezongyy_py.save_mysql()  # 调用保存到数据库中
            users = hezongyy_py1.objects.all()  # 数据库中读取数据
            return render(request, 'hezongyy_py.html', {'users': users})
        if r == "xxx":
            return HttpResponse("测试结果：xxx")
        else:
            return HttpResponseRedirect("/get_demo")

    else:
        render(request, 'index.html')

def toast(request):
    messages.success(request, "暂时无法抓取该url,请返回重新输入")
    return render(request, 'get_demo.html')
