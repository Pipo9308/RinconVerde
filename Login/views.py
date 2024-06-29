from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, ProductoForm
from cart.models import Product

@login_required
def panel(request):
    productos = Product.objects.all()
    return render(request, 'Login/panel.html', {'productos': productos})
@login_required
def listar_productos(request):
    productos = Product.objects.all()
    return render(request, 'login/listar_productos.html', {'productos': productos})
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto guardado correctamente!')
        else:
            messages.error(request, 'Error al guardar el producto.')
    else:
        form = ProductoForm()
    
    return render(request, 'login/crear_producto.html', {'form': form})
@login_required
def modificar_producto(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        selected_product = get_object_or_404(Product, pk=product_id)
        form = ProductoForm(request.POST, instance=selected_product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('modificar_producto')
    else:
        form = ProductoForm()
    
    products = Product.objects.all()
    return render(request, 'login/modificar_producto.html', {
        'products': products,
        'form': form,
    })
@login_required
def eliminar_producto(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            product.delete()
            messages.success(request, f'El producto "{product.name}" ha sido eliminado correctamente.')
            return redirect('eliminar_producto')  # Redirige a la misma página para actualizar la lista de productos
        else:
            messages.error(request, 'Error al intentar eliminar el producto.')
    
    # Obtener todos los productos para mostrar en el combo box
    products = Product.objects.all()
    
    return render(request, 'login/eliminar_producto.html', {'products': products})

def logout_view(request):
    logout(request)
    return redirect('index')

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
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel')  # Redirige a la página de inicio u otra página
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})