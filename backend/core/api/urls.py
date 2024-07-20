from rest_framework.routers import DefaultRouter
from django.urls import path, include
from predicciones.api.urls import predicciones_router

router = DefaultRouter()

#prediciones
router.registry.extend(predicciones_router.registry)

urlpatterns = [
    path('',include(router.urls)),
]
