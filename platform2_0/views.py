from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def home(request):
    return render(request, 'data_home.html')

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
        return render(request, 'data_home.html')

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