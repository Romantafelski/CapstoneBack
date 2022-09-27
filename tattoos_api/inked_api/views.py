from django.shortcuts import render
from rest_framework import generics
from .serializers import TattooSerializer
from .models import Tattoo


class TattooList(generics.ListCreateAPIView):
    queryset = Tattoo.objects.all().order_by('id') 
    serializer_class = TattooSerializer

class TattooDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tattoo.objects.all().order_by('id')
    serializer_class = TattooSerializer
