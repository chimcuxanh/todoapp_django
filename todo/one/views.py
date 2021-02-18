from django.shortcuts import render, redirect
from .models import *
from .forms import *


def today(request):
    tasks = Task.objects.all()

    form = TaskFrom()

    if request.method == 'POST':
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'one/one.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskFrom(instance=task)

    if request.method == 'POST':
        form = TaskFrom(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'one/update_form.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':

        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'one/delete.html', context)
