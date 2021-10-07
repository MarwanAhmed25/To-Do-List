from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import ListForm


def tasks(req):
    objs = Task.objects.all()
    context = {'tasks': objs}
    return render(req, 'base/tasks_list.html', context)


def task_create(req):
    form = ListForm()
    if req.method == 'POST':
        form = ListForm(req.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(req, 'base/task_create.html', context)


def task_detail(req, slug):
    task = Task.objects.get(slug=slug)
    context = {'task': task}
    return render(req, 'base/task_detail.html', context)


def task_delete(req, slug):
    task = Task.objects.get(slug=slug)
    if req.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'task': task}
    return render(req, 'base/task_delete.html', context)


def task_update(req, slug):
    task = Task.objects.get(slug=slug)
    form = ListForm(instance=task)
    if req.method == 'POST':
        form = ListForm(req.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(req, 'base/list_form.html', context)
