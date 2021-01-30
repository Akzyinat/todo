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
    return render(request, "add.html")

def changed(request):
    return render(request, "change.html")

def deleted(request):
    return render(request, "delete.html")