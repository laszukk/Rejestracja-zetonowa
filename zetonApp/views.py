from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import *


class MainView(TemplateView):
    template_name = 'base.html'


class KursantView(viewsets.ModelViewSet):
    queryset = Kursant.objects.all()
    serializer_class = KursantSerializer

class InstruktorView(viewsets.ModelViewSet):
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer

class KursView(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer

class ZetonView(viewsets.ModelViewSet):
    queryset = Zeton.objects.all()
    serializer_class = ZetonSerializer
