from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .forms import activate_user

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


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        # 認証トークンを検証して、
        result = activate_user(uidb64, token)
        # コンテクストのresultにTrue/Falseの結果を渡します。
        return super().get(request, result=result, **kwargs)