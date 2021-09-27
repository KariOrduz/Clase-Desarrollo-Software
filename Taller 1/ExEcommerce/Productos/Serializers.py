
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from Productos.models import *

class TipoSerial(serializers.ModelSerializer):
    class Meta:
        model = TipoElectrodomestico
        #fields = '__all__'
        fields = ["nombre", "foto", "numTipos", "numProductos"]

class ProductoSerial(serializers.ModelSerializer):
    class Meta:
        model = Producto
        #fields = '__all__'
        fields = ["nombre", "descripcion", "foto", "precio", "calificacion","tipoProducto"]

class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        #fields = '__all__'
        fields = ["usuario", "productoNombre", "calificacion", "fecha", "contenido"]



