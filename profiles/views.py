from django.shortcuts import render
from django.views.generic import  ListView,DetailView
from .models import post
from django.urls import reverse_lazy
# Create your views here.

class Index(ListView):
    model = post


class Detail(DetailView):
    model = post
    
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class Create(CreateView):
    model = post
# 編集対象にするフィールド
    fields =["title" , "body" , "category" , "tags"]

class Update(UpdateView):
    model = post
    fields = ["title","body","category","tags"]

class Delete(DeleteView):
    model = post
    success_url = reverse_lazy("profiles")