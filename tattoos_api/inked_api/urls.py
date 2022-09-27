from django.urls import path
from . import views

urlpatterns = [
    path('api/inked', views.TattooList.as_view(), name='inked_list'), 
    path('api/inked/<int:pk>', views.TattooDetail.as_view(), name='inked_detail'), 
]
