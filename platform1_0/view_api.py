# -*- coding: utf-8 -*-
from platform1_0.models import longyi_yp1
from django.http import JsonResponse
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
import json
from django.core import serializers
import time

"""添加药品"""
@csrf_exempt
def add_yp(request):
    """POST请求"""
    name = request.POST.get('name', '')
    cj = request.POST.get('cj', '')
    gg = request.POST.get('gg', '')
    xq = request.POST.get('xq', '')
    price = request.POST.get('price', '')
    if name == '' or cj == '' or gg == '' or xq == '' or price == '':
        return JsonResponse({'status': 10021, 'message': '参数错误'}, json_dumps_params={'ensure_ascii': False})
    result = longyi_yp1.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10022, 'message': '药品名已存在'}, json_dumps_params={'ensure_ascii': False})
    try:
        longyi_yp1.objects.create(name=name, cj=cj, gg=gg, xq=xq, price=price)
    except ValidationError:
        error = '开始日期格式错误，必须是:YYYY-MM-DD HH:MM:SS'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': '添加成功'})

def query_yp(request):
    """GET请求"""
    datas = []
    results = longyi_yp1.objects.all()
    if results:
        for i in results:
            longyi = {}
            # 给字典添加键值对
            longyi['name'] = i.name
            longyi['cj'] = i.cj
            longyi['xq'] = i.xq
            longyi['gg'] = i.gg
            longyi['price'] = i.price
            datas.append(longyi)
        return JsonResponse({'status': 200, 'message': '查询成功', 'datas': datas})
    else:
        return JsonResponse({'status': 10022, 'message': '查询的数据不存在'})

@csrf_exempt
def update_yp(request):
    """post请求，修改药品名称"""
    name1 = request.POST.get('name1', '')
    name2 = request.POST.get('name2', '')
    if name1 == '':
        return JsonResponse({'status': 10001, 'message': '输入为空'})
    result = longyi_yp1.objects.filter(name=name1)
    if result:
        longyi_yp1.objects.filter(name=name1).update(name=name2)
        return JsonResponse({'status': 200, 'message': '修改成功'})
    else:
        return JsonResponse({'status': 10002, 'message': '无法查到该药品'})





