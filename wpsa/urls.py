from django.conf.urls import url
from . import views

app_name = 'wpsa'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<wp_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<wp_id>[0-9]+)/addcomment/$', views.addcomment, name='addcomment')
]