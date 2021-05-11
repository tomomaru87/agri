
from django.urls import path
from profiles.views import Index,Detail

urlpatterns = [
    path('profiles/', Index.as_view(),name='profiles'),
    path('profiles/detail',Detail.as_view(),name='profiles_detail'),
   
]
