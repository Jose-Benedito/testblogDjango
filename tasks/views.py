from http.client import HTTPResponse
from django.shortcuts import render

from django.http import HttpResponse #import do pacote HTTPResponse

# Create your views here.

#teste da página
def helloWorld(request):
    return HttpResponse("Hello Benedito, eu sou Django")

# Gerando uma página na view

def taskList(request):
    return render(request, 'tasks/list.html')

# Gerando uma págian com argumento
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})