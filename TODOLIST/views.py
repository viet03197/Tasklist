from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
        messages.success(request, 'New Task Added!')
        return redirect('home')
    else:
        db = Task.objects.filter(owner=request.user)
        paginator = Paginator(db, 5)
        page = request.GET.get('page')
        db = paginator.get_page(page)
        return render(request, 'home.html', {'db': db})

def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')

def edit(request, id):
    if request.method == "POST":
        task = Task.objects.get(pk=id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, 'Task Successfully Edited!')
        return redirect('home')
    else:
        task = Task.objects.get(pk=id)
        return render(request, 'edit.html', {'task': task})

def about(request):
    data = {'title': 'About Me',
            'pagetitle': 'About'}
    return render(request, 'about.html', data)

def contact(request):
    data = {'title': 'Contact',
            'pagetitle': 'Contact'}
    return render(request, 'contact.html', data)