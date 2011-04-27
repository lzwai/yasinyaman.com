# -*- coding: utf-8-*-

# Create your views here.
from blogster.portfolyo.models import Portfolyo
from django.shortcuts import render_to_response

def portfolyo(request):
    kayitlarport = Portfolyo.objects.all().order_by('-tarih')
    return render_to_response("port.html", {'kayitlarport':kayitlarport})
