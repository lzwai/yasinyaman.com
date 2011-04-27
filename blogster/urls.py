# -*- coding: utf-8-*-
import os, sys
from django.conf.urls.defaults import *
from blogster.grappelli.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()
from blogster.blogs.views import *
from blogster.portfolyo.views import *
from blogster.anasayfa.views import *


#dersfeeds = {'latest': Blogss,}


from blogster.iletisim.views import *
KlasorYolu = os.path.dirname(__file__)
urlpatterns = patterns('',
    (r'^$', anasayfa),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^portfolyo/$', portfolyo),
    (r'^anasayfa/$', anasayfa),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^blogs/$', blogs),
    (r'^blogsrss/$', blogsrss),
    (r'^arsivblogs/$', blogsarsiv),
    (r'^blogs/([\w\-]+)/$', detay),
    (r'^siparis/gonderildi/', 'blogster.siparis.views.gonderildi'),
    (r'^siparis/','blogster.siparis.views.siparisonsayfa'),
    (r'^iletisim/gonderildi/', 'blogster.iletisim.views.gonderildi'),
    (r'^iletisim/','blogster.iletisim.views.iletisimonsayfa'),
    (r'^admin/(.*)', admin.site.root),
    (r'^grappelli/', include('grappelli.urls')),
    #(r'^feeds/rss/$', RssBlogsFeed()),
   # (r'^feeds/atom/$', AtomBlogsFeed()),
  #  (r'^dersfeeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': dersfeeds}),
    (r'^robots.txt$', 'django.views.generic.simple.direct_to_template', { 'template': 'robots.txt' }, 'index'),
    (r'^sitemap.xml$', 'django.views.generic.simple.direct_to_template', { 'template': 'sitemap.xml' }, 'index'),
    (r'^ttk_internet_sitesi$', 'django.views.generic.simple.direct_to_template', { 'template': 'ttk_internet_sitesi.htm' }, 'index'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(KlasorYolu, "static/")}),
)
