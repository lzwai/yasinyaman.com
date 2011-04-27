from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from blogster.iletisim.models import iletisimForm
from blogster.iletisim.forms import Formu


def iletisimonsayfa(request):
    
    if request.method == 'POST':
        form = Formu(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/iletisim/gonderildi/')
    else:
        form = Formu()
    return render_to_response('iletisim/form.html', {'form': form})

def gonderildi(request):
		return render_to_response('iletisim/send.html')


