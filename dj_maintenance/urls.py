from django.urls import path
from dj_maintenance import views

app_name = 'dj_maintenance'

urlpatterns = [
    path('', views.index, name='dj_maintenance-index'),
    path('<path:resource>', views.index),
]
