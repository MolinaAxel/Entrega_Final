# Generated by Django 4.1.7 on 2023-04-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesRate', '0009_juego_estrellas'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
