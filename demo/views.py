from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from django.http import QueryDict
from rest_framework.request import Request
from demo import models
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

"""数据库请求----ORM单表实例"""
"对象.save() 新增"
# def add_Data(request):
#     NBA = models.NBA_data(qy="阿夫迪亚", ccrq="16:23", df=3, zg=1, lb=1)
#     NBA.save()
#     return HttpResponse("<p>数据添加成功！</p>")
"通过 ORM 提供的 objects 提供的方法 create 来实现"
def add_Data(request):
    NBA = models.NBA_data.objects.create(qy="维斯布鲁克", ccrq="30:52", df=25, zg=12, lb=8)
    return HttpResponse("<p>数据添加成功！</p>")
"使用all()方法查询所有内容"
# def query_Data(request):
#     NBA = models.NBA_data.objects.all()
#     for i in NBA:
#         print(i.df)
#     # print(NBA, type(NBA))
#     return HttpResponse("<p>查找成功！</p>")
"filter()方法用于查询符合条件的数据"
# def query_Data(request):
#     # NBA = models.NBA_data.objects.filter(pk=2)
#     # for i in NBA:
#     #     print(i.df)
#     NBA = models.NBA_data.objects.filter(df=27)
#     for i in NBA:
#         print(i.zg)
#     return HttpResponse("<p>查找成功！</p>")
"exclude()方法用于查询不符合条件的数据"
def query_Data(request):
    NBA = models.NBA_data.objects.exclude(pk=2)
    return HttpResponse("<p>查找成功！</p>")
"get()方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误。"
"order_by() 方法用于对查询结果进行排序"
"reverse() 方法用于对查询结果进行反转"
"count() 方法用于查询数据的数量返回的数据是整数"
"exists() 方法用于判断查询的结果 QuerySet 列表里是否有数据。"
"values() 方法用于查询部分字段的数据。"
"values_list() 方法用于查询部分字段的数据"
"distinct() 方法用于对数据进行去重。"
"删除：使用模型类的 对象.delete()"
def delete_Data(request):
    NBA = models.NBA_data.objects.filter(pk=3).delete()
    return HttpResponse("<p>删除成功！</p>")
"修改：模型类的对象.属性 = 更改的属性值......模型类的对象.save()"
# def modify_Data(request):
#     NBA = models.NBA_data.objects.filter(pk=1).first()
#     NBA.lb = 5
#     NBA.save()
#     return HttpResponse("<p>更新成功！</p>")
"QuerySet 类型数据.update(字段名=更改的数据)（推荐）"
def modify_Data(request):
    NBA = models.NBA_data.objects.filter(pk__in=[1]).update(zg=19)
    return HttpResponse("<p>更新成功！</p>")

"""数据库请求----ORM多表实例"""
"""添加数据"""
"一对多（外键ForeignKey）"
"方式一：传对象的形式，返回值的数据类型是对象，书籍对象"
# def add_book(request):
#     pub_obj = models.Publish.objects.filter(pk=1).first()  # 获取出版社对象
#     book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)  # 给书籍的出版社属性publish传出版社对象
#     print(book, type(book))
#     return HttpResponse(book)
"方式二：传对象 id 的形式(由于传过来的数据一般是 id,所以传对象 id 是常用的)。"
# def add_book(request):
#     pub_obj = models.Publish.objects.filter(pk=2).first()  # 获取出版社对象
#     pk = pub_obj.pk  # 获取出版社对象的id
#     book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)  # 给书籍的关联出版社字段 publish_id 传出版社对象的id
#     print(book, type(book))
#     return HttpResponse(book)
"多对多(ManyToManyField)：在第三张关系表中新增数据"
"方式一：传对象形式，无返回值。"
def add_book(request):
    chong = models.Author.objects.filter(name="令狐冲").first()  # 获取作者对象
    ying = models.Author.objects.filter(name="任盈盈").first()  # 获取作者对象
    book = models.Book.objects.filter(title="菜鸟教程").first()  # 获取书籍对象
    book.authors.add(chong, ying)  # 给书籍对象的 authors 属性用 add 方法传作者对象
    return HttpResponse(book)





