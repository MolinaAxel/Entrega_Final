from django.shortcuts import render
from GamesRate.models import Juego
from GamesRate.forms import JuegoForm, BuscarPersonasForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



def mostrar_juego(request):

    juegos = Juego.objects.all()
    total_juegos = len(juegos)
    context = {"juegos":juegos,
               "total_juegos":total_juegos
               }
    return render(request, "GamesRate/juegos.html", context)

class BuscarJuegos(ListView):
    model = Juego #estados
    context_object_name = "juegos"

    def get_queryset(self): #metodos
        f = BuscarPersonasForm(self.request.GET) 
        if (f.is_valid()):
            return Juego.objects.filter(nombre__icontains=f.data
            ["criterio_nombre"]).all()
        else:
            return Juego.objects.none()
    
class JuegosDetail(DetailView):
    model = Juego # esto es igual a Juego.objects.get(id=pk)

class JuegosCreate(CreateView):
    model = Juego
    success_url = reverse_lazy("juegos-list")
    fields = '__all__'

class JuegosUpdate(UpdateView):
    model = Juego
    success_url = reverse_lazy("juegos-list")
    fields = '__all__'

class JuegosDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy("juegos-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('juegos-list')