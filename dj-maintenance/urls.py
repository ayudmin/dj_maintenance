from django.urls import path
from django_maintenance import views

app_name = 'dj-maintenance'

urlpatterns = [
    path('', views.index, name='dj-maintenance-index'),
    path('<path:resource>', views.index),
]
