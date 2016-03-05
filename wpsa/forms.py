from django import forms
from django.forms import ModelForm
from .models import Workplace

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
class WorkplaceForm(ModelForm):
    class Meta:
        model = Workplace
        fields = ['province','city', 'ws_type']
        #article = Article.objects.get(pk=1)
        #form = ArticleForm(instance=article)