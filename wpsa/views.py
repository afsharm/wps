from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Workplace
from django.template import loader
from django.http import Http404

def index(request):
	active_wp = Workplace.objects.order_by('-start_date')[:5]
	context = {'active_wp': active_wp}
	return render(request, 'wpsa/index.html', context)

def detail(request, wp_id):
	wp = get_object_or_404(Workplace, pk=wp_id)
	return render(request, 'wpsa/detail.html', {'wp': wp})