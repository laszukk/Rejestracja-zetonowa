from django.db import models

class Kursant(models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    pesel = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko


class Instruktor(models.Model):
    przedmiotKurs = (
    ('informatyka','Informatyka'),
    ('grafika', 'Grafika'),
    ('matematyka','Matematyka'),
    ('malarstwo','Malarstwo'),
    ('muzyka','Muzyka'),
    ('angielski','J.angielski'))

    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    przedmiot = models.CharField(max_length=20, choices=przedmiotKurs)
    pesel = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    tytul_naukowy = models.CharField(max_length=45)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class Kurs(models.Model):
    id_instruktor = models.ForeignKey(Instruktor, on_delete=models.CASCADE)
    przedmiot = models.CharField(max_length=20, choices=Instruktor.przedmiotKurs)
    grupa = models.IntegerField()
    miejsca = models.IntegerField()
    ilosc_godzin = models.IntegerField()
    sylabus = models.TextField()

class Zeton(models.Model):
    id_kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    id_instruktor = models.ForeignKey(Instruktor, on_delete=models.CASCADE)
    data_zakupu = models.DateField()
