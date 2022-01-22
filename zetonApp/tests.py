import django
from django.test import TestCase
from zetonApp.models import Kursant

def test__add_kursant(authorized_client):
    data_to_save = {
        'imie': 'Pan',
        'nazwisko': 'Kursant',
        'pesel': '00220710895',
        'email': 'pankurs@gmail.com',
    }

    url = 'http://127.0.0.1:8000/api/kursant'

    response = authorized_client.post(
        url,
        data_to_save,
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.json() == data_to_save
    all_kursanci = Kursant.objects.all()
    assert all_kursanci.count() == 1

    saved_kursant = all_kursanci.first()
    assert saved_kursant.imie == 'Pan'
    assert saved_kursant.nazwisko == 'Kursant'
    assert saved_kursant.pesel == '00220710895'
    assert saved_kursant.email == 'pankurs@gmail.com'
