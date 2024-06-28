from django.shortcuts import render, redirect

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
