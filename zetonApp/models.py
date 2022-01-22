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
    instruktor = models.ForeignKey(Instruktor,related_name="kursy", on_delete=models.CASCADE,null=True)
    przedmiot = models.CharField(max_length=20, choices=Instruktor.przedmiotKurs)
    grupa = models.IntegerField()
    miejsca = models.IntegerField()
    ilosc_godzin = models.IntegerField()
    nazwa = models.TextField()

    def __str__(self):
        return self.przedmiot + ' GR ' + str(self.grupa)

class Zeton(models.Model):
    kurs = models.ForeignKey(Kurs, related_name="zapisani",on_delete=models.CASCADE, verbose_name="kurs",null=True)
    kursant = models.ForeignKey(Kursant,related_name="zetony", on_delete=models.CASCADE,verbose_name="kursant",null=True)
    data_zakupu = models.DateField(auto_now_add=True)

