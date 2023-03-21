from django.shortcuts import render


def index(request):
    """A to return the index page"""
    return render(request, 'home/index.html')
