# from django.shortcuts import render
#
# # Create your views here.
import requests
from django.shortcuts import render, reverse
from django.http import HttpResponse
import ahttp

def index(request):
    return render(request, 'index.html')

def index_result(request):
    if request.method == 'GET':
        r = request.GET["q"]  # key就是前面输入框里的name属性对应值name="q"
        if r == "www":
            return HttpResponse("测试结果：www")
        if r == "xxx":
            return HttpResponse("测试结果：xxx")
    else:
        render(request, 'index.html')



# def test_qq(request):
#     '''请求页面'''
#     return render(request, 'get_demo.html')
#
# def result_qq(request):
#     '''返回结果'''
#     if request.method == 'GET':
#         # 获取提交的数据
#         r = request.GET["q"]  # key就是前面输入框里的name属性对应值name="q"
#         # url = "http://" + r
#         req = ahttp.get(r)
#         res = req.run()
#         # res = requests.get(r)
#         # req = res.text
# #         # res = ""
# #         # try:
# #         #     if int(r) % 2:
# #         #         res = "大吉大利！"
# #         #     else:
# #         #         res = "恭喜发财！"
# #         # except:
# #         #     res = "请输入正确QQ号！"
# #
#         return HttpResponse("测试结果：%s" % res.text)
#     else:
#         render(request, 'get_demo.html')
