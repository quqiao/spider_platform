from django.shortcuts import render
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
# Create your views here.

"""通过药品名查询"""
def query_name(request):
    times = ["20201109", "20201119", "20201209"]
    context = {'times': times}
    return render(request, 'query_name.html', context)

"""通过厂家名查询"""
def query_manufacturer(request):
    return render(request, 'query_manufacturer.html')

"""通过药品名+厂家组合查询"""
def query_name_manufacturer(request):
    return render(request, 'query_name_manufacturer.html')

"""药品名查询结果展示"""
def query_name_result(request):
    if request.method == 'POST':
        try:
            r = request.POST.get("name")  # key就是前面输入框里的name属性对应值name="name"
            t = request.POST.get("time")  # 取需要的时间
            io = r'F:\django\spider_platform\DataAnalysis\data\medical_data_%s.xlsx' % t
            sheetnames = ['合纵', '龙一', '蓉锦', '华鼎', '聚创', '粤通']
            dataAll = []

            for sheetname in sheetnames:
                pandasData = pd.read_excel(io, sheet_name=sheetname, index_col='药名')
                try:
                    data = dict(pandasData.loc[r])
                    dataAll.append(data)
                except KeyError:
                    dataAll.append('None')
            context = {'name': r, 'time': t, 'data1': dataAll[0], 'data2': dataAll[1], 'data3': dataAll[2],
                       'data4': dataAll[3], 'data5': dataAll[4], 'data6': dataAll[5]}
            return render(request, 'query_name_result.html', context)
        except FileNotFoundError:
            return HttpResponseRedirect("/DataAnalysis/toast1")

"""厂家名查询结果展示"""
def query_manufacturer_result(request):
    if request.method == 'POST':
        try:
            r = request.POST.get("manufacturer")  # key就是前面输入框里的name属性对应值name="name"
            t = request.POST.get("time")  # 取需要的时间
            io = r'F:\django\spider_platform\DataAnalysis\data\medical_data_%s.xlsx' % t
            sheetnames = ['合纵', '龙一', '蓉锦', '华鼎', '聚创', '粤通']
            dataAll = []

            for sheetname in sheetnames:
                pandasData = pd.read_excel(io, sheet_name=sheetname, index_col='厂家')
                try:
                    data = dict(pandasData.loc[r])
                    dataAll.append(data)
                except KeyError:
                    dataAll.append('None')
            context = {'name': r, 'time': t, 'data1': dataAll[0], 'data2': dataAll[1], 'data3': dataAll[2],
                       'data4': dataAll[3], 'data5': dataAll[4], 'data6': dataAll[5]}
            return render(request, 'query_manufacturer_result.html', context)
        except FileNotFoundError:
            return HttpResponseRedirect("/DataAnalysis/toast1")

"""药品名+厂家组合查询结果展示"""
def query_name_manufacturer_result(request):
    if request.method == 'GET':
        try:
            m = request.GET["manufacturer"]  # key就是前面输入框里的manufacturer属性对应值
            n = request.GET["name"]  # key就是输入框的
            t = request.GET["time"]  # 取需要的时间
            io = r'F:\django\spider_platform\DataAnalysis\data\medical_data_%s.xlsx' % t
            sheetnames = ['合纵', '龙一', '蓉锦', '华鼎', '聚创', '粤通']
            dataAll = []
            for sheetname in sheetnames:
                pandasData = pd.read_excel(io, sheet_name=sheetname, index_col=[2, 3])
                try:
                    data = dict(pandasData.loc[(n, m), :])
                    dataAll.append(data)
                except KeyError:
                    dataAll.append('None')
            context = {'manufacturer': m, 'name': n, 'time': t, 'data1': dataAll[0], 'data2': dataAll[1], 'data3': dataAll[2],
                                                       'data4': dataAll[3], 'data5': dataAll[4], 'data6': dataAll[5]}
            return render(request, 'query_name_manufacturer_result.html', context)
        except FileNotFoundError:
            return HttpResponseRedirect("/DataAnalysis/toast1")

"""日期输入无效提示"""
def toast1(request):
    messages.success(request, "输入的日期无效或者不存在抓取数据，请重试！！！！！！！！！！！！！！！！！")
    return render(request, 'toast/toast1.html')