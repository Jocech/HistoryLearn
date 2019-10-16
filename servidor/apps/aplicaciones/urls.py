from django.urls import path
from .views import Index,Inicio,Juego,Recuperacion,Registro

urlpatterns = [
    path('', Index, name='Index'),
    path('aplicaciones/inicio.html', Inicio, name='Inicio'),
    path('aplicaciones/juego.html', Juego, name='Juego'),
    path('aplicaciones/recuperacion.html', Recuperacion, name='Recuperacion'),
    path('aplicaciones/registro.html', Registro, name='Registro'),
]