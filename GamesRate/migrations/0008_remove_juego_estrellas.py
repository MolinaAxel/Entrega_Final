# Generated by Django 4.1.7 on 2023-04-22 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GamesRate', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='estrellas',
        ),
    ]