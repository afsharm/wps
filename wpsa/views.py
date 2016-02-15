from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Workplace, Comment
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone

def index(request):
	active_wp = Workplace.objects.order_by('-start_date')[:5]
	context = {'active_wp': active_wp}
	return render(request, 'wpsa/index.html', context)

def detail(request, wp_id):
	wp = get_object_or_404(Workplace, pk=wp_id)
	return render(request, 'wpsa/detail.html', {'wp': wp})

def addcomment(request, wp_id):
	wp = get_object_or_404(Workplace, pk=wp_id)
	c = Comment(comment = request.POST['comment'], create_date = timezone.now(), published=1, spam=1, commenter_id=-1, workplace_id=wp_id)
	c.save()
	return HttpResponseRedirect(reverse('wpsa:detail', args=(wp_id)))