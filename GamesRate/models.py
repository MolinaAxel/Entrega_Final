from django.db import models

# Create your models here.
class Juego(models.Model):
    nombre = models.TextField(max_length=100)
    genero = models.TextField(max_length=50)
    estrellas = models.IntegerField(default=0)
    opinion = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.id} - {self.nombre} - GENERO: {self.genero} - {self.estrellas} Estrellas"