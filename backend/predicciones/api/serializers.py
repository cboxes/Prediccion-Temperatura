from rest_framework import serializers
from ..models import Predicciones

class PrediccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predicciones
        fields = (
            'id',
            'Temperatura',
            'Valor_Prediccion',
            'RMSE',
            'MAPE',
            'Modelo',
            'DS',
            'VAR',
            'NVAR'
        )
    