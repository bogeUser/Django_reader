#conding: utf-8

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def more(request):
    return render(request, 'more.html')

def detail(request):
    return render(request, 'detail.html')

def chapter(request):
    return render(request, 'chapter.html')

