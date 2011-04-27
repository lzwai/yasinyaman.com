# -*- coding: utf-8-*-

import os,sys
DYOL= os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    # ('yasnyaman', 'yasnyaman@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'  
DATABASE_NAME = ''             
DATABASE_USER = ''         
DATABASE_PASSWORD = ''      
DATABASE_HOST = '' 
DATABASE_PORT = '' 
TIME_ZONE = 'Europe/Istanbul'

LANGUAGE_CODE = 'tr-TR'

SITE_ID = 1

USE_I18N = True


MEDIA_ROOT = os.path.join(DYOL, "static/")


MEDIA_URL = "/static/"
STATIC_DOC_ROOT = "/static/"

ADMIN_MEDIA_PREFIX = "/media/"


SECRET_KEY = 'vx*g(q^i5%mhh*9lz9ab94uj*@841&0w*geg5ted^f524coq(v'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'blogster.flatpages.middleware.FlatpageFallbackMiddleware',
    'blogster.pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'blogster.urls'

TEMPLATE_DIRS = (os.path.join(DYOL, "templates"))


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.admin',
    'grappelli',
    'blogster.flatpages',
    'blogster.blogs',
    'blogster.portfolyo',
    'blogster.siparis',
    'blogster.anasayfa',
    'blogster.iletisim',
    'blogster.pagination',

)
