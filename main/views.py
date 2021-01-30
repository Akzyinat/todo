from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test 3")

def added(request):
    return HttpResponse("add.html")

def changed(request):
    return HttpResponse("change.html")

def deleted(request):
    return HttpResponse("delete.html")