
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import IndexView, AboutView ,CompanyView,SignUpView,ActivateView
from accounts import views
from django.views.generic import TemplateView

# 実はページを表示するだけならこのように1行で書くことが出来ます。
index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
  
    path("home/", login_required(index_view), name="home"),
    path('', include("django.contrib.auth.urls")),
    path('', IndexView.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('company/',CompanyView.as_view(),name='company'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('home/activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),

]