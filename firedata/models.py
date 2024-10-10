from django.db import models


class MunicipioQUeimada(models.Model):
    municipio = models.CharField(max_length=100, primary_key=True)
    data_hora = models.DataTimeField()
    estado = models.CharField(max_length=100)
    bioma = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    frp = models.FloatField()
    precipita = models.FloatField(null=True, blank=True)
    dias_sem_chuva = models.FloatField()

    def __str__(self):
        return f'{self.municipio} - {self.data_hora}'