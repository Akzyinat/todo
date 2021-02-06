from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test 3")

def added(request):
    return render(request, "add.html")

def changed(request):
    return render(request, "change.html")

def deleted(request):
    return render(request, "delete.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)