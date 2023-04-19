from django.shortcuts import render
from GamesRate.models import Juego
from GamesRate.forms import JuegoForm

def mostrar_juego(request):

    juegos = Juego.objects.all()
    total_personas = len(juegos)
    context = {"juegos":juegos,
               "total_persona":total_personas,
               "form":JuegoForm()}
    return render(request, "GamesRate/juegos.html", context)

def crear_juego(request):
    juegos = Juego.objects.all()
    total_personas = len(juegos)
    f = JuegoForm(request.POST)
    context = {"juegos":juegos,
               "total_persona":total_personas,
               "form":f,
               }
    if f.is_valid():
        Juego(nombre=f.data["nombre"], genero=f.data["genero"], estrellas=f.data["estrellas"], opinion=f.data["opinion"]).save()

        
    return render(request, "GamesRate/juegos.html", context)




