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
from .models import Province, County


def index(request):
    return HttpResponse("Hello World, it is the index")


def sample(request):
    response_data = {}
    response_data['name'] = 'ON'
    response_data['Capital'] = 'Toronto123'
    return JsonResponse(response_data)


def province(request):
    pro = Province.objects.all().order_by('name').values()
    ret = {"province": list(pro)}
    return JsonResponse(ret)


def allcounty(request):
    provinces = Province.objects.all().order_by('name').values()
    counties = County.objects.all().order_by('name').values()
    ret = {
        "validity": 1440,
        "provinces": list(provinces),
        "counties": list(counties)
    }
    return JsonResponse(ret)
