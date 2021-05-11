from django.urls import path
from .views import IndexView, AboutView ,CompanyView



urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('company/',CompanyView.as_view(),name='company'),
]

