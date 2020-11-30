from django.urls import path
from . import views

app_name = 'bp'
urlpatterns = [
    path('', views.index, name='index'),
    path('prov', views.prov, name='prov'),
]