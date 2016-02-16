from django.conf.urls import url
from . import views

app_name = 'wpsa'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<wp_id>[0-9]+)/addcomment/$', views.addcomment, name='addcomment')
]