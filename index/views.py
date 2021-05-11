from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = '佐藤'
        return ctxt


class AboutView(TemplateView):
    template_name='about.html'


class CompanyView(TemplateView):
    template_name='campany.html'