from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import serializers
from .models import *
from django.http import QueryDict
from rest_framework.request import Request
from demo import models
from django.db.models import Avg, Max, Min, Count, Sum
from django.shortcuts import render, HttpResponse, redirect
from demo.My_forms import EmpForm
from django.views import View
from django.core.exceptions import ValidationError

# Create your views here.

"""css实例"""
def demo_css(request):
    return render(request, 'demo_css.html')

"""js实例"""
def demo_js(request):
    return render(request, 'demo_js.html')

"""bootstrap实例"""
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
# def add_book(request):
#     chong = models.Author.objects.filter(name="令狐冲").first()  # 获取作者对象
#     ying = models.Author.objects.filter(name="任盈盈").first()  # 获取作者对象
#     book = models.Book.objects.filter(title="菜鸟教程").first()  # 获取书籍对象
#     book.authors.add(chong, ying)  # 给书籍对象的 authors 属性用 add 方法传作者对象
#     return HttpResponse(book)
"方式二：传对象id形式，无返回值。"
def add_book(request):
    chong = models.Author.objects.filter(name="令狐冲").first()  # 获取作者对象
    pk = chong.pk  # 获取作者对象的id
    book = models.Book.objects.filter(title="冲灵剑法").first()  # 获取书籍对象
    book.authors.add(pk)  # 给书籍对象的 authors 属性用 add 方法传作者对象的id
    return HttpResponse(book)

"""数据库请求----聚合查询（aggregate)"""
"聚合查询函数是对一组值执行计算，并返回单个值"
"Django 使用聚合查询前要先从 django.db.models 引入 Avg、Max、Min、Count、Sum（首字母大写）"
def aggregate(request):
    res = models.Book.objects.aggregate(Avg("price"))  # 计算所有图书的平均价格
    res = models.Book.objects.aggregate(c=Count("id"), max=Max("price"), min=Min("price"))  # 计算所有图书的数量、最贵价格和最便宜价格:
    print(res, type(res))
    return HttpResponse("<p>聚合查询成功！</p>")

"""Django Form组件"""
"用于对页面进行初始化，生成 HTML 标签，此外还可以对用户提交对数据进行校验（显示错误信息）"
"先显示字段属性中的错误信息，然后再显示局部钩子的错误信息。"
"若显示了字段属性的错误信息，就不会显示局部钩子的错误信息。"
"若有全局钩子，则全局钩子是等所有的数据都校验完，才开始进行校验，并且全局钩子的错误信息一定会显示"
def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form":form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})

"""Django cookie 与 session"""
"Cookie 是存储在客户端计算机上的文本文件，并保留了各种跟踪信息"
"三步骤：" \
"服务器脚本向浏览器发送一组 Cookie;例如：姓名、年龄或识别号码等" \
"浏览器将这些信息存储在本地计算机上，以备将来使用;" \
"当下一次浏览器向 Web 服务器发送任何请求时，浏览器会把这些 Cookie 信息发送到服务器，服务器将使用这些信息来识别用户"
# def login(request):
#     if request.method == "GET":
#         return render(request, "login.html")
#     username = request.POST.get("username")
#     password = request.POST.get("pwd")
#     user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
#     print(user_obj.username)
#     if not user_obj:
#         return redirect("/demo/login/")
#     else:
#         rep = redirect("/demo/index/")
#         rep.set_cookie("is_login", True)
#         return rep
# def index(request):
#     print(request.COOKIES.get('is_login'))
#     status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
#     if not status:
#         return redirect('/demo/login/')
#     return render(request, "index.html")
def logout(request):
    rep = redirect('/demo/login/')
    rep.delete_cookie("is_login")
    return rep  # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/demo/login/')
    return render(request, "order.html")

"""Session(保存再服务端的键值对)"""
"服务器在运行时可以为每一个用户的浏览器创建一个其独享的 session 对象"


"""Django 中间件"""
"Django 中间件是修改 Django request 或者 response 对象的钩子"
"可以理解为是介于 HttpRequest 与 HttpResponse 处理之间的一道处理过程"
"Django 中间件作用:" \
"修改请求，即传送到 view 中的 HttpRequest 对象。"
"修改响应，即 view 返回的 HttpResponse 对象。"
def index(request):
    print("index视图......")
    return HttpResponse("ok")

"""Django 视图 - FBV 与 CBV"""
"FBV（function base views） 基于函数的视图，就是在视图里使用函数处理请求"
# def login(request):
#     if request.method == "GET":
#         return HttpResponse("GET 方法")
#     if request.method == "POST":
#         user = request.POST.get("user")
#         pwd = request.POST.get("pwd")
#         if user == "runoob" and pwd == "123456":
#             return HttpResponse("POST 方法")
#         else:
#             return HttpResponse("POST 方法1")
"CBV（class base views） 基于类的视图，就是在视图里使用类处理请求。"
class Login(View):
    def get(self, request):
        return HttpResponse("GET 方法")

    def post(self, request):
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法 1")
