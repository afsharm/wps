from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Workplace, Comment
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .forms import NameForm, WorkplaceForm
from django.core.mail import send_mail

class IndexView(generic.ListView):
	template_name = 'wpsa/index.html'
	context_object_name = 'active_wp'
	def get_queryset(self):
	   return Workplace.objects.order_by('-start_date')[:50]

class DetailView(generic.DetailView):
	model = Workplace
	template_name = 'wpsa/detail.html'

def addcomment(request, wp_id):
	wp = get_object_or_404(Workplace, pk=wp_id)
	c = Comment(body = request.POST['body'], create_date = timezone.now(), published=1, spam=1, commenter_id=-1, workplace_id=wp_id)
	c.save()
	return HttpResponseRedirect(reverse('wpsa:detail', args=(wp_id,)))

def get_name(request):
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a from instance and populate it with data from the request:
        form = NameForm(request.POST)
        #check whether it's valid:
        if form.is_valid():
            #process the data in form.cleaned_data as required
            #...
            #redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        
        #if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()
        
        return render(request, 'name.html', {'form': form})

def contact_from(request):
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a from instance and populate it with data from the request:
        form = ContactForm(request.POST)
        #check whether it's valid:
        if form.is_valid():
            #process the data in form.cleaned_data as required
            #...
            #redirect to a new URL:
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['info@example.com']
            
            if cc_myself:
                recipients.append(sender)
                
            send_mail(subject, message, sender, recipients)            
            return HttpResponseRedirect('/thanks/')
        
        #if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()
        
        return render(request, 'name.html', {'form': form})

def register_wp(request):
    if request.method == 'POST':
        form = WorkplaceForm(request.POST, request.FILES)
        if form.is_valid():
            time_now = timezone.now()
            wp = form.save(commit=False)
            wp.create_date = time_now 
            wp.start_date = time_now
            wp.end_date = time_now
            wp.register_date = time_now
            wp.expire_date = time_now
            wp.published = 1
            wp.advertiser_id = 0
            wp.save()
        return HttpResponseRedirect(reverse('wpsa:detail', args=(wp.id,)))        
    else: #GET or anything else
        form = WorkplaceForm()
        return render(request, 'wpsa/register_wp.html', {'form': form})
