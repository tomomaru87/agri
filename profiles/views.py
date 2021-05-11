from django.shortcuts import render
from django.views.generic import  ListView,DetailView
from .models import post
# Create your views here.

class Index(ListView):
    model = post


class Detail(DetailView):
    model = post
    