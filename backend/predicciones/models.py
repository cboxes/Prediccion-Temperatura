from django.db import models

# Create your models here.

class Predicciones(models.Model):
    id = models.PositiveSmallIntegerField
    Temperatura = models.FloatField()
    Valor_Prediccion = models.FloatField()
    RMSE = models.FloatField()
    MAPE = models.FloatField()
    Modelo = models.CharField(max_length=100)
    DS = models.CharField(max_length=1)
    VAR = models.CharField(max_length=100)
    NVAR = models.PositiveSmallIntegerField()

        
    