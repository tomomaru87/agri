
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('profiles/',include('profiles.urls')),
    path('accounts/',include('accounts.urls')),
]
