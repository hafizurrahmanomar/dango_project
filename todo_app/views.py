from django.http import HttpResponse
from django.shortcuts import redirect, render


from myapp import models

from .models import Task
from .forms import TaskForm


# Create your views here.

def task_list(request):
    tasks = Task.objects.all()  
    completed = request.GET.get("completed")
    if completed == "true":
        tasks = tasks.filter(completed=True)
    elif completed == "false":
        tasks = tasks.filter(completed=False)
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)  
    return render(request, 'task_details.html', {'task': task})

# Newly manually adding data a task

def add_task(request):

        _title = 'New Task'
        _description = 'Task Description'
        _completed = False
        _created_at = "2025-01-01 00:00:00"
        _update_at = "2025-01-01 00:00:00"
        task = Task(title=_title, description=_description, completed=_completed, created_at=_created_at, update_at=_update_at)
            
        task.save()
            
        # return HttpResponse("")
        return redirect('task_list')

def delete_task(request, pk):
    try:
        
        task = Task.objects.get(pk=pk)
        task.delete()
        task.save()
        return redirect('task_list')
    except Task.DoesNotExist:
        return HttpResponse("Task not found", status=404) 
    
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.completed = not task.completed  
        task.save()
        return redirect('task_list')
    except Task.DoesNotExist:
        return HttpResponse("Task not found", status=404)
    
def add_task_form(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})







