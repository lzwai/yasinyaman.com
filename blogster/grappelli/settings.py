# coding: utf-8

from django.conf import settings

# Admin Site Title
ADMIN_HEADLINE = getattr(settings, "GRAPPELLI_ADMIN_HEADLINE", 'Yasin YAMAN')
ADMIN_TITLE = getattr(settings, "GRAPPELLI_ADMIN_TITLE", 'Yasin YAMAN')

# Link to your Main Admin Site (no slashes at start and end)
ADMIN_URL = getattr(settings, "GRAPPELLI_ADMIN_URL", '/admin/')