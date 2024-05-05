from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import CreateTaskForm


def display_tasks(request):
    tasks = Task.objects.all().order_by('pub_date')
    return render(request, "polls/display_tasks.html", {'tasks': tasks})


def create_task(request):
    if request.method == "POST":
        task = CreateTaskForm(request.POST)
        if task.is_valid():
            task.save()
            return HttpResponse("Your task was submitted successfully")

    else:
        task = CreateTaskForm
    return render(request, 'polls/create_task.html', {"task": task})


def done(request):
    task_list = Task.objects.filter(status=True)
    context = {"tasks": task_list}
    return render(request, "polls/display_tasks.html", context)


def delete_task(request, name):
    pass


def update_task(request, name):
    pass
