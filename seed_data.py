import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flota_project.settings')
django.setup()

from flota_app.models import Chofer, Camion
from django.contrib.auth.models import User


def run_seed():
    print("Cargando datos de prueba para evaluación INACAP...")

    # 1. Crear Superusuario Administrador
    admin, _ = User.objects.get_or_create(
        username='admin', is_staff=True, is_superuser=True)
    admin.set_password('admin123')
    admin.save()

    # 2. Crear Usuario Profesor (del PDF Receta)
    profe, _ = User.objects.get_or_create(
        username='profe', is_staff=True, is_superuser=True)
    profe.set_password('123456')
    profe.save()

    # 3. Crear Usuario Chofer
    chofer_user, _ = User.objects.get_or_create(username='chofer_a')
    chofer_user.set_password('chofer123')
    chofer_user.save()

    # 4. Crear Camiones de la Flota
    camion1, _ = Camion.objects.get_or_create(
        patente='AB123CD',
        defaults={
            'marca': 'Volvo',
            'modelo': 'FH16 750',
            'capacidad_toneladas': 28.5
        }
    )

    camion2, _ = Camion.objects.get_or_create(
        patente='XY987ZT',
        defaults={
            'marca': 'Mercedes-Benz',
            'modelo': 'Actros 2651',
            'capacidad_toneladas': 22.0
        }
    )

    camion3, _ = Camion.objects.get_or_create(
        patente='KR542LP',
        defaults={
            'marca': 'Scania',
            'modelo': 'R500 V8',
            'capacidad_toneladas': 30.0
        }
    )

    # 5. Crear Choferes
    Chofer.objects.get_or_create(
        rut='12.345.678-9',
        defaults={
            'user': chofer_user,
            'nombre': 'Juan Pérez Morales',
            'licencia': 'A5',
            'telefono': '+56911223344',
            'camion': camion1
        }
    )

    Chofer.objects.get_or_create(
        rut='15.987.654-3',
        defaults={
            'nombre': 'Carlos Gómez Silva',
            'licencia': 'A4',
            'telefono': '+56955667788',
            'camion': camion2
        }
    )

    Chofer.objects.get_or_create(
        rut='17.842.109-K',
        defaults={
            'nombre': 'Rodrigo Alvarado Castro',
            'licencia': 'A5',
            'telefono': '+56987654321',
            'camion': camion3
        }
    )

    print("¡Datos cargados con éxito!")
    print("==================================================")
    print("USUARIOS CREADOS PARA EVALUACIÓN:")
    print("1) Admin (Superuser):  admin    / admin123")
    print("2) Profe (Superuser):  profe    / 123456")
    print("3) Chofer (Operador):  chofer_a / chofer123")
    print("==================================================")


if __name__ == '__main__':
    run_seed()