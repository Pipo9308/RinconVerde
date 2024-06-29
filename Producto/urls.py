"""
URL configuration for RinconVerde project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('brotes/', views.brotes, name='brotes'),
    path('arbustos/', views.arbustos, name='arbustos'),
    path('sustrato/', views.sustrato, name='sustrato'),
    path('macetero/', views.macetero, name='macetero'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart_view, name='cart'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    path('nosotros/', views.nosotros, name='nosotros'),
]





