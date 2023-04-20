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
from GamesRate.views import mostrar_juego, crear_juego, BuscarJuegos, JuegosDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('juegos', mostrar_juego, name="juego"),
    path('juegos/create', crear_juego, name="juegos-create"),
    path('juegos/list', BuscarJuegos.as_view(), name="juegos-list"),
    path('juegos/<pk>/detail', JuegosDetail.as_view(), name="juegos-detail"),
]
