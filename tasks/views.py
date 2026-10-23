from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()

        if title:
            Task.objects.create(title=title)

        return redirect("task_list")

    tasks = Task.objects.order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def complete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()

    return redirect("task_list")
