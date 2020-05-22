'''
from django.shortcuts import render


def home(request):
	return render(request, 'web/index.html')
'''

from django.views.generic import TemplateView

class IndexView(TemplateView):

	template_name = "web/index.html"
