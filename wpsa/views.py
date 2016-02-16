from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Workplace, Comment
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

class IndexView(generic.ListView):
	template_name = 'wpsa/index.html'
	context_object_name = 'active_wp'
	def get_queryset(self):
		return Workplace.objects.order_by('-start_date')[:5]

class DetailView(generic.DetailView):
	model = Workplace
	template_name = 'wpsa/detail.html'

def addcomment(request, wp_id):
	wp = get_object_or_404(Workplace, pk=wp_id)
	c = Comment(body = request.POST['body'], create_date = timezone.now(), published=1, spam=1, commenter_id=-1, workplace_id=wp_id)
	c.save()
	return HttpResponseRedirect(reverse('wpsa:detail', args=(wp_id)))