# Generated by Django 3.2.9 on 2021-12-10 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zetonApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instruktor',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='instruktor',
            old_name='PESEL',
            new_name='pesel',
        ),
        migrations.RenameField(
            model_name='kursant',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='kursant',
            old_name='PESEL',
            new_name='pesel',
        ),
    ]
