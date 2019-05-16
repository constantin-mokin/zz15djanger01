from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        return HttpResponse('len is {}' .format(max(len(name))))
    return HttpResponse('It is GET request')

def index2(request):
    if request.method == "POST":
        name = request.POST.get('calendar')
        # if name == 01.01.2019 :#####
        return HttpResponse('Happy New Year')
    else:
        return HttpResponse()
