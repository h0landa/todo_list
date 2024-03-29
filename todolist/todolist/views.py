from django.shortcuts import render
from .forms_app import TaskForm


def home(request):
    return render(request, 'index.html')

def registerTask(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'task_form.html', context)