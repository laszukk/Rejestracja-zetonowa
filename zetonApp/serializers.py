from rest_framework import serializers
from .models import *


class KursantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kursant
        fields = '__all__'


class InstruktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruktor
        fields = '__all__'


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = '__all__'


class ZetonSzkolenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zeton
        fields = '__all__'