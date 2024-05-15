from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Task
from .forms import CreateTaskForm, UpdateTaskForm


def display_tasks(request):
    tasks = Task.objects.all().order_by('pub_date')
    return render(request, "polls/display_tasks.html", {'tasks': tasks})


def create_task(request):
    if request.method == "POST":
        task = CreateTaskForm(request.POST)
        if task.is_valid():
            task.save()
            return HttpResponseRedirect(reverse("display_tasks"))
    else:
        task = CreateTaskForm
    return render(request, 'polls/create_task.html', {"task": task})


def done(request):
    task_list = Task.objects.filter(status=True)
    context = {"tasks": task_list}
    return render(request, "polls/done.html", context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect(reverse("display_tasks"))
    return redirect("display_tasks")


def update_task(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("display_tasks"))
    else:
        form = UpdateTaskForm(instance=task_instance)
    return render(request, "polls/update_task.html", {"form": form})
