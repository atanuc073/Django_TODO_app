
from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks=Task.objects.filter(isCompleted=False).order_by("-updated_at")
    print(tasks)
    context={"tasks":tasks}
    return render(request,"home.html",context)
    # return HttpResponse("Hello, world. You're at the todo_main index.")