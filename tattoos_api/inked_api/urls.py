from django.urls import path
from . import views

urlpatterns = [
    path('api/tattoo', views.TattooList.as_view(), name='inked_list'), 
    path('api/tattoo/<int:pk>', views.TattooDetail.as_view(), name='inked_detail'), 
]

