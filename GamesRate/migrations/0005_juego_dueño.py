# Generated by Django 4.1.7 on 2023-04-21 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GamesRate', '0004_rename_descripcion_juego_opinion'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='dueño',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dueño', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
