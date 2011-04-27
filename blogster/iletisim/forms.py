# -*- coding: utf-8-*-
from django.forms import ModelForm
from blogster.iletisim.models import iletisimForm

class Formu(ModelForm):
	def __init__(self, data=None, *args, **kwargs):
		if data=={}:
			data=None
		ModelForm.__init__(self, data, *args, **kwargs)
	class Meta:
		model = iletisimForm




