from django.shortcuts import render

# Create your views here.


def demo_css(request):
    return render(request, 'demo_css.html')

def demo_js(request):
    return render(request, 'demo_js.html')

def demo_bootstrap(request):
    return render(request, 'demo_bootstrap.html')

