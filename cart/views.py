from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from .models import Product, CartItem

def payment_view(request):
    # Lógica para procesar el pago
    return render(request, 'cart/payment.html')

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