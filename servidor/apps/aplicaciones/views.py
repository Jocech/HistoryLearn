from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

# ...

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('Inicio')
    # Si llegamos al final renderizamos el formulario
    return render(request, "aplicaciones/index.html", {'form': form})
# Create your views here.


def Index(request):
    return render(request, 'aplicaciones/index.html')

def Inicio(request):
    return render(request, 'aplicaciones/inicio.html')

def Juego(request):
    return render(request, 'aplicaciones/juego.html')

def Recuperacion(request):
    return render(request, 'aplicaciones/recuperacion.html')

def Registro(request):
    return render(request, 'aplicaciones/registro.html')