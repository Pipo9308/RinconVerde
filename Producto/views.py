from django.shortcuts import render

def index(request):
    return render(request, 'producto/brotes.html')  # Cambiado de 'index.html' a 'producto/index.html'
