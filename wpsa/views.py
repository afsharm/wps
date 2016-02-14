from django.shortcuts import render
from django.http import HttpResponse

from .models import Workplace

def index(request):
	active_wp = Workplace.objects.order_by('-start_date')[:5]
	output = ', '.join([wp.city for wp in active_wp])
	return HttpResponse(output)

def detail(request, wp_id):
	return HttpResponse("Hi, this is %s" % wp_id)