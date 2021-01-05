# from django.shortcuts import render
#
# # Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.template import TemplateDoesNotExist
from selenium.common.exceptions import InvalidSelectorException
from platform1_0.web_page import ysb_lyg, ypzdw_jtj, hezongyy_py
from platform1_0.web_page.huodong import longyi_tjzq
from platform1_0.web_page.yaopin import longyi_yp, scjuchuang_yp, scytyy_yp
from platform1_0.models import hezongyy_py1, longyi_yp1, scjuchuang_py1, ypzdw_jtj1, scytyy_ypzq1
import re

def index(request):
    return render(request, 'HomePage/index.html')

def index_result(request):
    if request.method == 'GET':
        try:
            r = request.GET["url"]  # key就是前面输入框里的name属性对应值name="q"
            c = request.GET["number"]
            shuzi = re.findall("\d+", r)
            shuzi1 = ''.join(shuzi)
            if "hezongyy.com/puyao" in r:   # 判断合纵药易购普药专区
                hezongyy_py.clear_list()
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
                scjuchuang_yp.crawl_scjuchuan_py(int(c))
                scjuchuang_yp.save_mysql()
                users = scjuchuang_py1.objects.all()
                return render(request, 'scjuchuang_py.html', {'users': users})

            elif "http://www.scytyy.net/goods" in r:  # 判断四川粤通药品中心
                scytyy_yp.crawl_scytyy_ypzq(int(c))
                scytyy_yp.save_mysql()
                users = scytyy_ypzq1.objects.all()
                return render(request, 'scytyy_ypzq.html', {'users': users})

            elif r == "ysbang":
                ysb_lyg.crawl_hezongyy(int(c))  # 调用采集数据
                ysb_lyg.save_csv()  # 调用保存到数据库中
                # users = ysb_lyg1.objects.all()  # 数据库中读取数据
                # return render(request, 'ysb_lyg.html', {'users': users})
                return HttpResponse("抓取结果：完成")
            elif r == None or c == None:
                return HttpResponseRedirect("/platform1/toast1")
            else:
                return HttpResponseRedirect("/platform1/toast1")
        except (TypeError, ValueError):
            return HttpResponseRedirect("/platform1/toast2")
        except InvalidSelectorException:
            return HttpResponseRedirect("/platform1/toast3")
        except TemplateDoesNotExist:
            return HttpResponseRedirect("/platform1/toast4")
    else:
        render(request, 'HomePage/index.html')

def toast1(request):
    messages.success(request, "输入为空或者暂时无法抓取,请返回重新输入！！！！！！")
    return render(request, 'toast/toast1.html')

def toast2(request):
    messages.success(request, "字符串没有转换成数字，请联系管理员解决！！！！！！")
    return render(request, 'toast/toast2.html')

def toast3(request):
    messages.success(request, "selenium出现问题，请联系管理员解决！！！！！！")
    return render(request, 'toast/toast3.html')

def toast4(request):
    messages.success(request, "Django出现问题，请联系管理员解决！！！！！！")
    return render(request, 'toast/toast4.html')



