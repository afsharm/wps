from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.core.mail import send_mail
import json
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello World, it is the index")

def prov(request):
    response_data = {}
    response_data['name'] = 'ON'
    response_data['Capital'] = 'Toronto'
    return JsonResponse(response_data)