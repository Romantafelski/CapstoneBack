from django.urls import path
from . import views

urlpatterns = [
    path('', views.TattooList.as_view(), name='inked_list'), 
    path('<int:pk>', views.TattooDetail.as_view(), name='inked_detail'), 
]


