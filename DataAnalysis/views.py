from django.shortcuts import render
import pandas as pd

# Create your views here.

def home(request):
    return render(request, 'data_home.html')

def index_result(request):
    if request.method == 'GET':
        r = request.GET["name"]  # key就是前面输入框里的name属性对应值name="q"
        io = r'F:\django\spider_platform\DataAnalysis\data\medical_data_20201109.xlsx'
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
        return render(request, 'DataResult.html', {'name': r, 'data1': data_hz, 'data2': data_ly, 'data3': data_rj,
                                                   'data4': data_hd, 'data5': data_jc, 'data6': data_yt})
