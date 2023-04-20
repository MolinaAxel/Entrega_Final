from django.shortcuts import render
from GamesRate.models import Juego
from GamesRate.forms import JuegoForm, BuscarPersonasForm
from django.views.generic import ListView

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

class BuscarJuegos(ListView):
    model = Juego
    context_object_name = "juegos"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
            return Juego.objects.filter(nombre__icontains=f.data
            ["criterio_nombre"]).all()
        else:
            return Juego.objects.none()
