from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Juego(models.Model):
    nombre = models.TextField(max_length=100)
    genero = models.TextField(max_length=50)
    estrellas = models.IntegerField(default=0)
    opinion = models.TextField(max_length=200)
    dueño = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="dueño")
    imagen = models.ImageField(upload_to="juegos", null=True, blank=True)
    creado_el = models.DateTimeField(auto_now_add= True)



    def __str__(self):
        return f"{self.id} - {self.nombre} - GENERO: {self.genero} - {self.estrellas} Estrellas"

class Profile(models.Model):
    email = models.TextField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE , related_name="profile")
    imagen = models.ImageField(upload_to="profile", null=True, blank=True)

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")


