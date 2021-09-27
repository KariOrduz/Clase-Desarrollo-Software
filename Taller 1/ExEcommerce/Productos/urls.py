#Direcciones de las API's

from rest_framework import urlpatterns
from Productos.views import TipoAPI, TipoAPI2, TipoAPI3
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tipo', TipoAPI)
router.register('producto', TipoAPI2)
router.register('comentario', TipoAPI3, basename="comentario")


urlpatterns = [
    path('crud/', include(router.urls)),
]

#localhost:8000/productos/api/crud/tipo

