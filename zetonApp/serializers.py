from xml.dom import ValidationErr
from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

class KursantSerializer(serializers.ModelSerializer):
    zetony = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zeton-detail')
    class Meta:
        model = Kursant
        fields = '__all__'


class InstruktorSerializer(serializers.ModelSerializer):
    kursy = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='kurs-detail')
    class Meta:
        model = Instruktor
        fields = '__all__'


class KursSerializer(serializers.ModelSerializer):
    instruktor = serializers.SlugRelatedField(queryset=Instruktor.objects.all(), slug_field='nazwisko')
    zapisani = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='kursant-detail')
    class Meta:
        model = Kurs
        fields = '__all__'


class KursantForeignKey(serializers.SlugRelatedField):
    def get_queryset(self):
        queryset = Kursant.objects.all()
        request = self.context.get('request', None)
        if not request.user.is_superuser:
            queryset = queryset.filter(email=request.user.email)
        return queryset

class ZetonSerializer(serializers.ModelSerializer):
    kursant =KursantForeignKey(slug_field="pesel")
    kurs = serializers.SlugRelatedField(queryset=Kurs.objects.all(), slug_field='nazwa')

    def validate(self, data):
        data_dict=dict(data)
        if Zeton.objects.filter(kurs=data_dict['kurs'], kursant=data_dict['kursant']).exists():
            raise ValidationError({'kurs': ['Nie można zapisać dwa razy na ten sam kurs',]})
        return super().validate(data)

    class Meta:
        model = Zeton
        fields = '__all__'
        
    