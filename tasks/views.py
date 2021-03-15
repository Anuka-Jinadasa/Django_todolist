from django.shortcuts import render , redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = taskAdd()

    if request.method == 'POST':
        form = taskAdd(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'tasks' : tasks , 'form' : form}
    return render(request, 'tasks/list.html' , context)

def update(request, pk):
    task = Task.objects.get(id = pk)

    form = taskAdd(instance=task)

    if request.method == 'POST':
        form = taskAdd(request.POST ,instance=task )
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'tasks/updateTask.html', context)


def delete(request, pk):
    item = Task.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/deleteTask.html', context)
