from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import DateTimeFilter,NumberFilter,FilterSet


class MainView(TemplateView):
    template_name = 'base.html'

class KursantView(viewsets.ModelViewSet):
    queryset = Kursant.objects.all()
    serializer_class = KursantSerializer

    def get_queryset(self):
        user=self.request.user
        if user.is_anonymous:
            return Kursant.objects.none()
        elif user.is_superuser:
            return Kursant.objects.all()
        else:
            return Kursant.objects.filter(email=user.email)
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['nazwisko']
    search_fields = ['nazwisko']
    ordering_fields=['imie','nazwisko']
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    

class InstruktorView(viewsets.ModelViewSet):
    queryset = Instruktor.objects.all()
    serializer_class = InstruktorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['przedmiot']
    search_fields = ['przedmiot']
    ordering_fields=['przedmiot','nazwisko']
    permission_classes = [permissions.IsAdminUser]

class KursFilter(FilterSet):
    min_students=NumberFilter(field_name='miejsca', lookup_expr='gte')
    max_students=NumberFilter(field_name='miejsca', lookup_expr='lte')
    class Meta:
        model = Kurs
        fields = ['min_students', 'max_students']

class KursView(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['przedmiot']
    search_fields = ['przedmiot']
    ordering_fields=['przedmiot','miejsca']
    filter_class = KursFilter
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class ZetonFilter(FilterSet):
    from_date=DateTimeFilter(field_name='data_zakupu', lookup_expr='gte')
    to_date=DateTimeFilter(field_name='data_zakupu', lookup_expr='lte')
    class Meta:
        model = Zeton
        fields = ['from_date', 'to_date']

class ZetonView(viewsets.ModelViewSet):
    queryset = Zeton.objects.all()
    serializer_class = ZetonSerializer

    def get_queryset(self):
        user=self.request.user
        if user.is_anonymous:
            return Zeton.objects.none()
        elif user.is_superuser:
            return Zeton.objects.all()
        else:
            return Zeton.objects.filter(kursant__email=user.email)
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['kurs__przedmiot']
    search_fields = ['kurs__przedmiot']
    ordering_fields=['data_zakupu','kurs__przedmiot']
    filter_class = ZetonFilter
    permission_classes = [permissions.IsAuthenticated]

