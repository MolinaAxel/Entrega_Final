from django.shortcuts import render
from GamesRate.models import Juego, Profile, Mensaje
from GamesRate.forms import JuegoForm, BuscarPersonasForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def about(request):
    return render(request, "GamesRate/about.html")

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

class JuegosCreate(LoginRequiredMixin, CreateView):
    model = Juego
    success_url = reverse_lazy("juegos-list")
    fields = '__all__'

class JuegosUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Juego
    success_url = reverse_lazy("juegos-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        juego_id = self.kwargs.get('pk')
        return Juego.objects.filter(dueño=user_id, id=juego_id).exists()

    def handle_no_permission(self):
        return render(self.request, "GamesRate/not_found.html")
    

class JuegosDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Juego
    success_url = reverse_lazy("juegos-list")

    def test_func(self):
        user_id = self.request.user.id
        juego_id = self.kwargs.get('pk')
        return Juego.objects.filter(dueño=user_id, id=juego_id).exists()

    def handle_no_permission(self):
        return render(self.request, "GamesRate/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('juegos-list')

class Login(LoginView):
    next_page = reverse_lazy("juegos-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Profile;
    success_url = reverse_lazy("juegos-list")
    fields = '__all__'

    def test_func(self):
        user_idd = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user_id=user_idd, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "GamesRate/not_found.html")

class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("juegos-list")
    fields = '__all__'

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy("juegos-list")

class MensajeList(LoginRequiredMixin,ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()


class MensajeDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-list")


    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "GamesRate/not_found.html")