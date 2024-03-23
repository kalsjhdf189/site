from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def first(request):
    return render(request, 'first.html')

def second(request):
    return render(request, 'second.html')
