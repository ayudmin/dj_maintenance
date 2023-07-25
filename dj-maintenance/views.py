from django.shortcuts import render


def index(request, resource=None):
    return render(request, 'maintenance/index.html')
