from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from .models import Product, CartItem, Boleta, BoletaDetalle
from django.db import transaction

def view_invoices(request):
    session_key = request.session.session_key
    
    if not session_key:
        return redirect('index')  # Manejar el caso sin sesión de manera adecuada
    
    # Obtener todas las boletas asociadas a la sesión actual
    boletas = Boleta.objects.filter(detalles__session_key=session_key).distinct()
    
    return render(request, 'cart/view_invoices.html', {'boletas': boletas})

def payment_view(request):
    session_key = request.session.session_key
    
    if not session_key:
        return redirect('cart:view_cart')  # Redirige si no hay sesión activa
    
    cart_items = CartItem.objects.filter(session_key=session_key)
    total_price = sum(item.total_price() for item in cart_items)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        
        # Utilizamos una transacción para garantizar la consistencia de la base de datos
        with transaction.atomic():
            # Crear la boleta
            boleta = Boleta.objects.create(
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                precio_total=total_price,
            )
            
            # Agregar productos y cantidades al detalle de la boleta
            for cart_item in cart_items:
                BoletaDetalle.objects.create(
                    boleta=boleta,
                    product=cart_item.product,
                    cantidad=cart_item.quantity,
                    session_key=session_key
                )
                
                # Actualizar el stock del producto
                product = cart_item.product
                product.stock -= cart_item.quantity
                product.save()
        
            # Limpiar el carrito después de procesar la compra
            CartItem.objects.filter(session_key=session_key).delete()
        
        messages.success(request, 'Compra realizada con éxito. Gracias por su compra!')
        return redirect('cart:view_invoices')  # Redirigir a la vista de las boletas
    
    return render(request, 'cart/payment.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            messages.error(request, "Invalid product.")
            return redirect('cart:view_cart')  # Cambia 'producto:index' por la URL de la página de productos en 'producto'

        if quantity > product.stock:
            messages.error(request, f"Only {product.stock} units available in stock.")
            return redirect('cart:view_cart')  # Cambia 'producto:index' por la URL de la página de productos en 'producto'
        
        # Recuperar o crear la sesión
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        # Verificar si ya existe un item en el carrito para este producto y sesión
        cart_item, created = CartItem.objects.get_or_create(product=product, session_key=session_key)
        
        if not created:
            # Si el item ya existe, actualizamos la cantidad
            cart_item.quantity += quantity
        else:
            # Si es un nuevo item, establecemos la cantidad
            cart_item.quantity = quantity
        
        # Verificar si la cantidad total excede el stock disponible
        if cart_item.quantity > product.stock:
            messages.error(request, f"Only {product.stock} units available in stock.")
            return redirect('cart:view_cart')  # Cambia 'producto:index' por la URL de la página de productos en 'producto'
        
        # Guardar el item del carrito actualizado
        cart_item.save()
        
        messages.success(request, f"{product.name} added to cart.")
        return redirect('cart:view_cart')  # Redirige a la vista 'view_cart' del carrito
        
    else:
        return redirect('cart:view_cart')  # Cambia 'producto:index' por la URL de la página de productos en 'producto'


def view_cart(request):
    session_key = request.session.session_key
    
    # Verificar si hay una sesión activa
    if not session_key:
        return render(request, 'cart/view_cart.html', {'cart_items': []})
    
    # Filtrar los ítems del carrito por la sesión actual
    cart_items = CartItem.objects.filter(session_key=session_key)
    
    if request.method == 'POST':
        # Obtener el ID del carrito y la cantidad a actualizar o eliminar
        cart_item_id = request.POST.get('cart_item_id')
        action = request.POST.get('action')
        
        if action == 'update':
            new_quantity = int(request.POST.get('quantity', 0))
            cart_item = get_object_or_404(CartItem, id=cart_item_id, session_key=session_key)
            product = cart_item.product
            
            # Verificar si la nueva cantidad solicitada excede el stock disponible
            if new_quantity > product.stock:
                messages.error(request, f"Only {product.stock} units available in stock.")
            else:
                cart_item.quantity = new_quantity
                cart_item.save()
        
        elif action == 'delete':
            CartItem.objects.filter(id=cart_item_id, session_key=session_key).delete()
    
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})