from .tasks import interchange_column
from .models import Task
from celery.task.control import revoke

from django.http import HttpResponse
from django.contrib import messages


def start(request):
    found = False
    pointer = 1
    if request.method == "POST":
        name = request.POST.get('name')
        try:
            t = Task.objects.get(name=name)
            pointer = t.pointer
            found = True
        except:
            t = Task(name=name)
        task = interchange_column.delay(name)
        t.task_id = task.id
        t.save()
        if found:
            response = "Your Task is resumed"
        else:
            response = "Your new task has started"
        return HttpResponse(response)
    else:
        return HttpResponse("Start a task?")


def pause(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if revoke_task(name):
            response = "Your Tasked has been paused"
        else:
            response = "Some Error Occured"
        return HttpResponse(response)
    else:
        return HttpResponse("Pause a task?")


def stop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if revoke_task(name):
            t = Task.objects.get(name=name)
            try:
                t.delete()
                response = "Your Tasked has been stopped"
            except:
                response = "Some error occured"
        else:
            response = "Some error occured"
        return HttpResponse(response)

    else:
        return HttpResponse("Stop a task?")


def revoke_task(name):
    t = Task.objects.get(name=name)
    task_id = t.task_id
    try:
        revoke(task_id, terminate=True)
        return True
    except:
        return False
