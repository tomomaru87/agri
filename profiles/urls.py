
from django.urls import path
from profiles.views import Index,Detail,Create,Update,Delete

urlpatterns = [
    path('', Index.as_view(),name='profiles'),
    path('detail/<pk>/',Detail.as_view(),name='profiles_detail'),
    path('create/',Create.as_view(),name='profiles_create'),
    path('update/<pk>',Update.as_view(),name='profiles_update'),
    path('delete/<pk>', Delete.as_view(), name="profiles_delete"),

]
