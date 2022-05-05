from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse #import do pacote HTTPResponse

from .models import Task # importa o model
# Create your views here.

def taskList(request):
    tasks = Task.objects.all() # select de todos os resultados 
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id) # pega a chave primária (pk) com get
    return render(request, 'tasks/task.html', {'task': task})
    
#teste da página
def helloWorld(request):
    return HttpResponse("Hello Benedito, eu sou Django")

# Gerando uma página na view

# Gerando uma págian com argumento
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})