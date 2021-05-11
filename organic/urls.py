
from django.contrib import admin
from django.urls import path,include
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/',include('profiles.urls')),
    path('',include('accounts.urls')),
    path("signup/", views.SignUpView.as_view(), name="signup"),

]
