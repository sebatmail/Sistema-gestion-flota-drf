from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Camion, Chofer


class CamionAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)
        self.camion = Camion.objects.create(
            patente='AB123CD',
            marca='Volvo',
            modelo='FH16',
            capacidad_toneladas=25.0
        )

    def test_list_camiones(self):
        response = self.client.get('/api/camiones/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_camion(self):
        payload = {
            'patente': 'CD456EF',
            'marca': 'Scania',
            'modelo': 'R500',
            'capacidad_toneladas': 30.5
        }
        response = self.client.post('/api/camiones/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Camion.objects.count(), 2)

    def test_edit_camion_put(self):
        """Prueba requerimiento del profesor: edición completa de camión"""
        payload = {
            'patente': 'AB123CD',
            'marca': 'Volvo Updated',
            'modelo': 'FH16 2026',
            'capacidad_toneladas': 28.0
        }
        response = self.client.put(f'/api/camiones/{self.camion.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.camion.refresh_from_db()
        self.assertEqual(self.camion.marca, 'Volvo Updated')
        self.assertEqual(float(self.camion.capacidad_toneladas), 28.0)

    def test_edit_camion_patch(self):
        """Prueba de edición parcial de camión"""
        payload = {'modelo': 'FH16 Super'}
        response = self.client.patch(f'/api/camiones/{self.camion.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.camion.refresh_from_db()
        self.assertEqual(self.camion.modelo, 'FH16 Super')

    def test_delete_camion(self):
        response = self.client.delete(f'/api/camiones/{self.camion.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Camion.objects.count(), 0)


class ChoferAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)
        self.camion = Camion.objects.create(
            patente='XY987ZT',
            marca='Mercedes-Benz',
            modelo='Actros',
            capacidad_toneladas=20.0
        )
        self.chofer = Chofer.objects.create(
            nombre='Juan Pérez',
            rut='12.345.678-9',
            licencia='A5',
            telefono='+56911223344',
            camion=self.camion
        )

    def test_list_choferes(self):
        response = self.client.get('/api/choferes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_chofer_valid_rut(self):
        payload = {
            'nombre': 'Carlos Gómez',
            'rut': '15.987.654-3',
            'licencia': 'A4',
            'telefono': '+56955667788',
        }
        response = self.client.post('/api/choferes/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Chofer.objects.count(), 2)

    def test_create_chofer_invalid_rut(self):
        payload = {
            'nombre': 'Invalido',
            'rut': '123-INVALID',
            'licencia': 'A4',
            'telefono': '+56900000000',
        }
        response = self.client.post('/api/choferes/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_chofer_put(self):
        """Prueba requerimiento crítico: edición de chofer"""
        payload = {
            'nombre': 'Juan Pérez Editado',
            'rut': '12.345.678-9',
            'licencia': 'A5',
            'telefono': '+56999887766',
            'camion': self.camion.id
        }
        response = self.client.put(f'/api/choferes/{self.chofer.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.chofer.refresh_from_db()
        self.assertEqual(self.chofer.nombre, 'Juan Pérez Editado')
        self.assertEqual(self.chofer.telefono, '+56999887766')

    def test_delete_chofer(self):
        response = self.client.delete(f'/api/choferes/{self.chofer.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Chofer.objects.count(), 0)


class WebTemplateViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='password123')

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gestión Profesional de Flota")

    def test_about_page(self):
        response = self.client.get('/quienes-somos/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Quiénes Somos")

    def test_services_page(self):
        response = self.client.get('/servicios/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "API Endpoints")
        self.assertContains(response, "Panel de Administración")

    def test_contact_page_get_and_post(self):
        # GET
        response = self.client.get('/contacto/')
        self.assertEqual(response.status_code, 200)
        # POST
        response_post = self.client.post('/contacto/', {
            'nombre': 'Profesor Marcelo Alvarado',
            'email': 'marcelo@inacap.cl',
            'telefono': '+56911223344',
            'mensaje': 'Excelente trabajo con vistas y DRF.'
        })
        self.assertEqual(response_post.status_code, 200)
        self.assertContains(response_post, "Mensaje enviado con éxito")

    def test_login_and_logout(self):
        login_res = self.client.post('/login/', {
            'username': 'admin',
            'password': 'password123'
        })
        self.assertEqual(login_res.status_code, 302)
        self.assertRedirects(login_res, '/choferes/')

