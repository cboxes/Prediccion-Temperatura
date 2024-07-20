from rest_framework.routers import DefaultRouter
from .views import PrediccionesViewSet

#from predicciones.api.views import PrediccionesViewSet
# from django.urls import path

predicciones_router = DefaultRouter()

predicciones_router.register(r'predicciones', PrediccionesViewSet)


# urlpatterns = [
#      path('list-view/',PrediccionesViewSet.as_view({'get':'list'}),name='list-view')
#  ]