
from django.shortcuts import render
from cart.models import Product

def index(request):
    # Obtener todos los productos
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'producto/index.html', context)

def brotes(request):
    # Obtener todos los productos
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'producto/brotes.html', context)

def arbustos(request):
    # Obtener todos los productos
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'producto/arbustos.html', context)

def sustrato(request):
    # Obtener todos los productos
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'producto/sustrato.html', context)

def macetero(request):
    # Obtener todos los productos
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'producto/macetero.html', context)

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

def nosotros(request):
    return render(request, 'producto/nosotros.html')