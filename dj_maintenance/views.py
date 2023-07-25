from django.shortcuts import render


def index(request, resource=None):
    return render(request, 'dj-dj_maintenance/index.html')
