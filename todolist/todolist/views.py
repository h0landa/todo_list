from django.shortcuts import render, redirect
from .forms_app import TaskForm
from .models import Task

def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def registerTask(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        description = request.POST.get('description')
        Task.objects.create(
            title=title,
            description=description
        )
        return redirect('home')
    
    return render(request, 'task_form.html')

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        task.title = request.POST.get('task')
        task.description = request.POST.get('description')
        task.save()
        return redirect('home')
    
    context = {'form': form, 'task':task}
    return render(request, 'task_form.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
    context = {'task': task}

    return render(request, 'confirm_delete.html', context)
