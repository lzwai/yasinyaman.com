# -*- coding: utf-8-*-

# Create your views here
from blogster.blogs.models import Blogs, Yorum
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from blogster.blogs.forms import Formu
from django.http import HttpResponseRedirect


def blogs(request):
    kayitlar = Blogs.objects.all().order_by('-tarih').filter(yayinda=1).filter(arsiv=0)
    return render_to_response("blog.html", {'kayitlar':kayitlar},context_instance=RequestContext(request))

def blogsarsiv(request):
    arsivkayitlar = Blogs.objects.all().order_by('-tarih').filter(yayinda=1).filter(arsiv=1)
    return render_to_response("arsivblog.html", {'arsivkayitlar':arsivkayitlar},context_instance=RequestContext(request))

def blogsrss(request):
    kayitlarrss = Blogs.objects.all().order_by('-tarih').filter(yayinda=1).filter(arsiv=0)
    return render_to_response("blogrss.htm", {'kayitlarrss':kayitlarrss},context_instance=RequestContext(request))

def blogsarsivrss(request):
    arsivkayitlarrss = Blogs.objects.all().order_by('-tarih').filter(yayinda=1).filter(arsiv=1)
    return render_to_response("arsivblogrss.html", {'arsivkayitlar':arsivkayitlar},context_instance=RequestContext(request))


#def detay(request, slug):
 #   kayitlars, saybil=int()
  #  detay=kayitlars.get(slug=slug,)
   # saybil.update({'detay':detay})
    #return render_to_response("blogd.html",saybil)


def detay(request, slug):
    kayitlars, saybil=int()
    detay=kayitlars.get(slug=slug,)
    ipa = request.META['REMOTE_ADDR']
    saybil.update({'detay':detay,"ipa":ipa})
    if request.method == 'POST':
        form = Formu(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/blogs/')
    else:
        form = Formu()
    return render_to_response('blogd.html', saybil)






def yorum(request, slug):
    altposts, altpagedata = init1()
    altkategoridetay = altposts.get(slug=slug,)
    altpagedata.update({'yorumdetay': yorumdetay})
    
   
def init1():
    altposts = Yorum.objects.all()
    altpagedata = {'post_list': altposts,}
    return altposts, altpagedata
	
def int():
    kayitlars = Blogs.objects.all()
    saybil = {'post_list': kayitlars,}
    return kayitlars, saybil
	
