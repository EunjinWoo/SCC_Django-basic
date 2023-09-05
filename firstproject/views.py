from django.http import HttpResponse
from django.shortcuts import render

def pingpong(request):
    return render(request, 'pong.html')

def index(request):
    # print(request.GET)
    name = request.GET.get('name')
    # return HttpResponse(f'<h1> Index 안녕하세요 {name}님 </h1>')
    return render(request, 'index.html')

def getdata(request):
    print(request.POST.get("todo"))
    return HttpResponse('ok')