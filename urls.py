from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ChoferViewSet, CamionViewSet,
    login_view, logout_view,
    choferes_page, camiones_page,
    home_view, about_view, services_view, contact_view
)

router = DefaultRouter()
router.register(r'camiones', CamionViewSet, basename='camiones')
router.register(r'choferes', ChoferViewSet, basename='choferes')

urlpatterns = [
    # Páginas Web Institucionales / Templates
    path('', home_view, name='home_page'),
    path('quienes-somos/', about_view, name='about_page'),
    path('servicios/', services_view, name='services_page'),
    path('contacto/', contact_view, name='contact_page'),

    # API REST Endpoints (DRF)
    path('api/', include(router.urls)),

    # Frontend Gestión Flota (Autenticado)
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('choferes/', choferes_page, name='choferes_page'),
    path('camiones/', camiones_page, name='camiones_page'),
]
