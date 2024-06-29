from django.shortcuts import render, redirect

from .forms import RegistroForm
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib import messages

def index(request):
    return render(request, 'producto/index.html')

def brotes(request):
    return render(request, 'producto/brotes.html')

def arbustos(request):
    # tu lógica de vista actual

    # redirigir a la vista de brotes
    return redirect('brotes')

def sustrato(request):
    return render(request, 'producto/sustrato.html')

def macetero(request):
    return render(request, 'producto/macetero.html')

def login(request):
    return render(request, 'login/login.html')

def cart_view(request):
    # Aquí va la lógica de tu vista para el carrito de compras
    context = {
        # Define aquí el contexto necesario para tu plantilla de carrito
    }
    return render(request, 'ruta_a_tu_template.html', context)

def privacy_view(request):
    # Lógica de tu vista para la política de privacidad
    context = {
        # Define aquí el contexto necesario para tu plantilla de política de privacidad
    }
    return render(request, 'ruta_a_tu_template.html', context)

def terms_view(request):
    # Lógica de la vista aquí
    return render(request, 'producto/terms.html')



def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Cambia 'index' por la URL a la que deseas redirigir después de registrar
    else:
        form = RegistroForm()
    
    return render(request, 'login/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        emails = request.POST.get('email')
        passwords = request.POST.get('password')

        
        user = authenticate(request, username=emails, password=passwords)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige a la página de inicio después del inicio de sesión exitoso
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')

    # Si es GET o si hay errores de autenticación, renderiza nuevamente el formulario de inicio de sesión
    return render(request, 'login/login.html')