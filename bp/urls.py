from django.urls import path
from . import views

app_name = 'bp'
urlpatterns = [
    path('', views.index, name='index'),
    path('sample', views.sample),
    path('province', views.province),
]