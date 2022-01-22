import django
from django.test import TestCase
from zetonApp.models import Instruktor, Kursant
from rest_framework import status
from django.contrib.auth.models import User

class ModelKursantTest(TestCase):
    def test_create_kursant(self):
        User.objects.create_superuser(username='superuser',password='user12345', email='admin@example.com')
        self.client.login(username='superuser',password='user12345')
        response = self.client.post("/api/kursant/", {
        "imie": "Jesse",
        "nazwisko": "Pinkman",
        "pesel": "00220710895", 
        "email": "diesel@email.com", })

        kursant = Kursant.objects.first()

        self.assertEqual(kursant.imie, "Jesse")
        self.assertEqual(kursant.nazwisko, "Pinkman")
        self.assertEqual(kursant.pesel, "00220710895")
        self.assertEqual(kursant.email, "diesel@email.com")
        self.assertEqual(response.status_code, 201)

    def test_create_instruktor(self):
            User.objects.create_superuser(username='superuser',password='user12345', email='admin@example.com')
            self.client.login(username='superuser',password='user12345')
            response = self.client.post("/api/instruktor/", {
            "imie": "Walter",
            "nazwisko": "White",
            "przedmiot": "muzyka",
            "pesel": "99220710895", 
            "email": "heisenberg@email.com", 
            "tytul_naukowy": "Magister",})

            instruktor = Instruktor.objects.first()

            self.assertEqual(instruktor.imie, "Walter")
            self.assertEqual(instruktor.nazwisko, "White")
            self.assertEqual(instruktor.przedmiot, "muzyka")
            self.assertEqual(instruktor.pesel, "99220710895")
            self.assertEqual(instruktor.email, "heisenberg@email.com")
            self.assertEqual(instruktor.tytul_naukowy, "Magister")
            self.assertEqual(response.status_code, 201)

