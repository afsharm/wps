from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf.urls import url
from . import views

app_name = 'wpsa'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^register_wp/$', views.register_wp, name='register_wp'),
	url(r'^(?P<wp_id>[0-9]+)/addcomment/$', views.addcomment, name='addcomment')
]

#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
