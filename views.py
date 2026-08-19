from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets, permissions
from .models import Chofer, Camion
from .serializers import ChoferSerializer, CamionSerializer

# --- Vistas API (DRF) ---

class CamionViewSet(viewsets.ModelViewSet):
    """
    API ViewSet para gestión integral de Camiones (CRUD completo: GET, POST, PUT, PATCH, DELETE).
    """
    queryset = Camion.objects.all().order_by('id')
    serializer_class = CamionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChoferViewSet(viewsets.ModelViewSet):
    """
    API ViewSet para gestión integral de Choferes (CRUD completo: GET, POST, PUT, PATCH, DELETE).
    """
    queryset = Chofer.objects.all().select_related('camion', 'user').order_by('id')
    serializer_class = ChoferSerializer
    permission_classes = [permissions.IsAuthenticated]


# --- Vistas Públicas / Web Template ---

def home_view(request):
    """Página de Inicio / Home del Sistema"""
    total_camiones = Camion.objects.count()
    total_choferes = Chofer.objects.count()
    return render(request, 'home.html', {
        'total_camiones': total_camiones,
        'total_choferes': total_choferes,
    })


def about_view(request):
    """Página Quiénes Somos / Sobre la Empresa"""
    return render(request, 'about.html')


def services_view(request):
    """Página de Servicios con accesos directos a API y Admin"""
    return render(request, 'services.html')


def contact_view(request):
    """Página de Contacto con formulario de empresa"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        return render(request, 'contact.html', {
            'success': True,
            'nombre': nombre,
        })
    return render(request, 'contact.html')


# --- Vistas de Autenticación y Gestión de Flota ---

def login_view(request):
    if request.user.is_authenticated:
        return redirect('choferes_page')

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('choferes_page')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas. Verifique usuario y contraseña.'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_page')


@login_required(login_url='/login/')
def choferes_page(request):
    camiones_disponibles = Camion.objects.all()
    return render(request, 'choferes.html', {
        'camiones': camiones_disponibles
    })


@login_required(login_url='/login/')
def camiones_page(request):
    return render(request, 'camiones.html')
