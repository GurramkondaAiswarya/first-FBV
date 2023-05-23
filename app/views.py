from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('good evening')
def meghana(request):
    return HttpResponse('good night')
def anitha(request):
    return HttpResponse('hello')