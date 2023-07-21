from django.urls import path
from django_maintenance import views

app_name = 'maintenance'

urlpatterns = [
    path('', views.index, name='maintenance_index'),
    path('<path:resource>', views.index),
]
