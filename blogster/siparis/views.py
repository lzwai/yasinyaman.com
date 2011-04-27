from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from blogster.siparis.models import siparisForm
from blogster.siparis.forms import Formu

def siparisonsayfa(request):
    
    if request.method == 'POST':
        form = Formu(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/siparis/gonderildi/')
    else:
        form = Formu()
    return render_to_response('siparis/form.html', {'form': form})

def gonderildi(request):
		return render_to_response('siparis/send.html')


