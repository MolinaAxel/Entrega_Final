from django.shortcuts import render
from GamesRate.models import Juego
from GamesRate.forms import JuegoForm

def mostrar_juego(request):

    juegos = Juego.objects.all()
    total_juegos = len(juegos)
    context = {"juegos":juegos,
               "total_juegos":total_juegos,
               "form":JuegoForm()}
    return render(request, "GamesRate/juegos.html", context)

def crear_juego(request):

    f = JuegoForm(request.POST)
    context = {
        "form":f
    }

    if f.is_valid():
        Juego(nombre=f.data["nombre"], genero=f.data["genero"], estrellas=f.data["estrellas"], opinion=f.data["opinion"]).save()
        context['form'] = JuegoForm()

    
    context["juegos"] = Juego.objects.all()
    context["total_juegos"] = len(Juego.objects.all())
        
    return render(request, "GamesRate/juegos.html", context)




