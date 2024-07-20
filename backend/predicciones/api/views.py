from rest_framework  import viewsets
from .serializers import PrediccionesSerializer
from ..models import Predicciones


class PrediccionesViewSet(viewsets.ModelViewSet):
    queryset = Predicciones.objects.all()
    serializer_class = PrediccionesSerializer


