from rest_framework import serializers
from .models import MunicipioQUeimada

class MunicipioQueimadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipioQUeimada
        fields = ['munipio',
                  'data_hora',
                  'estado',
                  'bioma'
                  'latitude',
                  'longitude',
                  'frp',
                  'precipita',
                  'dias_sem_chuva',
                  ]