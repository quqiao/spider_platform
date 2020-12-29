from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from django.http import QueryDict
from rest_framework.request import Request
# Create your views here.


def demo_css(request):
    return render(request, 'demo_css.html')

def demo_js(request):
    return render(request, 'demo_js.html')

def demo_bootstrap(request):
    return render(request, 'demo_bootstrap.html')

def archive(request, year="2018", month="01"):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))

def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}
    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()
    if query_params != {}:
        return query_params
    else:
        return result_data


# class CardSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Card
#         fields = "__all__"
#
# class CardViewSet(viewsets.ModelViewSet):
#     queryset = Card.objects.all()
#     serializer_class = CardSerializer
#
#     def get(self, request, *args, **kwargs):
#         params = get_parameter_dic(request)
#         return JsonResponse(data=params)
#
#     def post(self, request, *args, **kwargs):
#         params = get_parameter_dic(request)
#         return JsonResponse(data=params)
#
#     def put(self, request, *args, **kwargs):
#         params = get_parameter_dic(request)
#         return JsonResponse(data=params)
