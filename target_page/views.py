# from django.shortcuts import render
#
# # Create your views here.
import requests
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.template import TemplateDoesNotExist
from selenium.common.exceptions import InvalidSelectorException

from target_page.web_page import hezongyy_py, ysb_lyg, longyi_tjzq, longyi_yp, scjuchuang_py, ypzdw_jtj
from target_page.models import hezongyy_py1, ysb_lyg1, longyi_tjzq1, longyi_yp1, scjuchuang_py1, ypzdw_jtj1
import re


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
        try:
            r = request.GET["url"]  # key就是前面输入框里的name属性对应值name="q"
            c = request.GET["number"]
            shuzi = re.findall("\d+", r)
            shuzi1 = ''.join(shuzi)
            if "hezongyy.com/puyao" in r:   # 判断合纵药易购普药专区
                hezongyy_py.crawl_hezongyy(int(c))  # 调用采集数据
                hezongyy_py.save_mysql()  # 调用保存到数据库中
                users = hezongyy_py1.objects.all()  # 数据库中读取数据
                return render(request, 'hezongyy_py.html', {'users': users})

            elif "http://www.longyiyy.com/events" in r:  # 判断龙一医药网特价专区
                longyi_tjzq.crawl_longyi_tjzq(int(shuzi1), int(c))
                longyi_tjzq.save_csv()
                # longyi_tjzq.save_mysql()
                # users = longyi_tjzq1.objects.all()
                # return render(request, 'longyi_tjzq.html', {'users': users})

            elif "http://www.longyiyy.com/goods" in r:  # 判断龙一医药网药品专区
                longyi_yp.crawl_longyi_yp(int(c))
                longyi_yp.save_mysql()
                users = longyi_yp1.objects.all()
                return render(request, 'longyi_yp.html', {'users': users})

            elif "https://www.ypzdw.com/jshop" in r:  # 判断药品终端网阶梯价专区
                ypzdw_jtj.crawl_ypzdw_jtj(int(c))
                ypzdw_jtj.save_mysql()
                users = ypzdw_jtj1.objects.all()
                return render(request, 'ypzdw_jtj.html', {'users': users})


            elif "www.scjuchuang.com/goods" in r:  # 判断四川聚创医药普药专区
                scjuchuang_py.crawl_scjuchuan_py(int(c))
                scjuchuang_py.save_mysql()
                users = scjuchuang_py1.objects.all()
                return render(request, 'scjuchuang_py.html', {'users': users})

            elif r == "ysbang":
                ysb_lyg.crawl_hezongyy(int(c))  # 调用采集数据
                ysb_lyg.save_csv()  # 调用保存到数据库中
                # users = ysb_lyg1.objects.all()  # 数据库中读取数据
                # return render(request, 'ysb_lyg.html', {'users': users})
                return HttpResponse("抓取结果：完成")
            else:
                return HttpResponseRedirect("/toast1")
        except (TypeError, ValueError):
            return HttpResponseRedirect("/toast2")
        except InvalidSelectorException:
            return HttpResponseRedirect("/toast3")
        except TemplateDoesNotExist:
            return HttpResponseRedirect("/toast4")
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

def toast1(request):
    messages.success(request, "暂时无法抓取该url,请返回重新输入！！！！！！")
    return render(request, 'toast1.html')

def toast2(request):
    messages.success(request, "字符串没有转换成数字，请联系管理员解决！！！！！！")
    return render(request, 'toast2.html')

def toast3(request):
    messages.success(request, "selenium出现问题，请联系管理员解决！！！！！！")
    return render(request, 'toast3.html')

def toast4(request):
    messages.success(request, "Django出现问题，请联系管理员解决！！！！！！")
    return render(request, 'toast4.html')

def demo_css(request):
    return render(request, 'demo_css.html')

def demo_js(request):
    return render(request, 'demo_js.html')
