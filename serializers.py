import re
from rest_framework import serializers
from .models import Chofer, Camion


class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'


class ChoferSerializer(serializers.ModelSerializer):
    camion_detalle = CamionSerializer(source='camion', read_only=True)

    class Meta:
        model = Chofer
        fields = '__all__'

    def validate_rut(self, value):
        """Validación simple de formato de RUT chileno (ej: 12345678-K)"""
        rut_clean = value.replace('.', '').replace('-', '').upper()

        if not re.match(r'^\d{7,8}[0-9K]$', rut_clean):
            raise serializers.ValidationError(
                "El formato de RUT ingresado no es válido. Ejemplo: 12.345.678-K")

        return value
