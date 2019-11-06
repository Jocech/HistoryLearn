from django.urls import path
from .views import Index,Inicio,Juego,Recuperacion,Registro,login,register

urlpatterns = [
    path('', login, name='Index'),
    path('aplicaciones/inicio.html', Inicio, name='Inicio'),
    path('aplicaciones/juego.html', Juego, name='Juego'),
    path('aplicaciones/recuperacion.html', Recuperacion, name='Recuperacion'),
    path('aplicaciones/registro.html', register, name='Registro'),
]