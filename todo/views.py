# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from  .forms import TodoForm
from .models import Todo
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
        todo_list = Todo.objects.order_by('id')
        todoform = TodoForm()
        context={'todo_list': todo_list, 'form': todoform}
        return render(request, 'todo/index.html', context)



def addtodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request, id):
    todo = Todo.objects.get(pk=id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    Todo.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteall(request):
    Todo.objects.all().delete()
    return redirect('index')