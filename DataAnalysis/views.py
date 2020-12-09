from django.shortcuts import render
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, 'data_home.html')

def index_result(request):
    if request.method == 'GET':
        try:
            r = request.GET["name"]  # key就是前面输入框里的name属性对应值name="q"
            t = request.GET["time"]  # 取需要的时间
            io = r'F:\django\spider_platform\DataAnalysis\data\medical_data_%s.xlsx' % t
            try:
                pandasData = pd.read_excel(io, sheet_name='合纵', index_col='药名')
                data_hz = dict(pandasData.loc[r])
            except KeyError:
                data_hz = '暂无该药品'
            try:
                pandasData = pd.read_excel(io, sheet_name='龙一', index_col='药名')
                data_ly = dict(pandasData.loc[r])
            except KeyError:
                data_ly = '暂无该药品'
            try:
                pandasData = pd.read_excel(io, sheet_name='蓉锦', index_col='药名')
                data_rj = dict(pandasData.loc[r])
            except KeyError:
                data_rj = '暂无该药品'
            try:
                pandasData = pd.read_excel(io, sheet_name='华鼎', index_col='药名')
                data_hd = dict(pandasData.loc[r])
            except KeyError:
                data_hd = '暂无该药品'
            try:
                pandasData = pd.read_excel(io, sheet_name='聚创', index_col='药名')
                data_jc = dict(pandasData.loc[r])
            except KeyError:
                data_jc = '暂无该药品'
            try:
                pandasData1 = pd.read_excel(io, sheet_name='粤通', index_col='药名')
                data_yt = dict(pandasData1.loc[r])
            except KeyError:
                data_yt = '暂无该药品'
            return render(request, 'DataResult.html', {'name': r, 'time': t, 'data1': data_hz, 'data2': data_ly, 'data3': data_rj,
                                                       'data4': data_hd, 'data5': data_jc, 'data6': data_yt})
        except 	FileNotFoundError:
            return HttpResponseRedirect("/DataAnalysis/toast1")


def toast1(request):
    messages.success(request, "输入的日期无效或者不存在抓取数据，请重试！！！！！！！！！！！！！！！！！")
    return render(request, 'toast/toast1.html')