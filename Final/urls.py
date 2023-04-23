"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GamesRate.views import mostrar_juego, BuscarJuegos, JuegosDetail,JuegosCreate, JuegosUpdate, JuegosDelete,SignUp, Login,Logout, ProfileUpdate, ProfileCreate, MensajeCreate,MensajeDelete,MensajeList
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_juego, name="juego"),
    path('juegos/create', JuegosCreate.as_view(), name="juegos-create"),
    path('juegos/list', BuscarJuegos.as_view(), name="juegos-list"),
    path('juegos/<pk>/detail', JuegosDetail.as_view(), name="juegos-detail"),
    path('juegos/<pk>/update', JuegosUpdate.as_view(), name="juegos-update"),
    path('juegos/<pk>/delete', JuegosDelete.as_view(), name="juegos-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('mensaje/enviar', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
