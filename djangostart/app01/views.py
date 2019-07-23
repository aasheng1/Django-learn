from django.shortcuts import render,HttpResponse

# Create your views here.

def demo01(request):
    html = '<h1>i am demo01</h1>'
    print(html)
    return HttpResponse(html)