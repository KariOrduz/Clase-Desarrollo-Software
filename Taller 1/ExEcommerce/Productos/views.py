from django.http import response
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from Productos.models import *
from Productos.Serializers import *

class TipoAPI(viewsets.ModelViewSet):
    serializer_class = TipoSerial
    queryset = TipoElectrodomestico.objects.all()
    
class TipoAPI2(viewsets.ModelViewSet):
    serializer_class = ProductoSerial
    queryset = Producto.objects.all()

#class TipoAPI3(viewsets.ModelViewSet):
    #serializer_class = ComentarioSerial
    #queryset = Comentario.objects.all()

class TipoAPI3(viewsets.ViewSet):
    #Permite especificar la lógica de los registros CRUD
    def list(self, request): #GET
        comentarios = Comentario.objects.all()
        serializador = ComentarioSerial(comentarios, many=True)
        #return Response({"Hola": "Esto es una prueba"})
        return Response(serializador.data)

    def create(self, request): #POST
        #request => ["usuario": "nomUsuario", "producto": 5, "contenido"]
        serializador = ComentarioSerial(data=request.data)
        if serializador.is_valid(): #¿El cometario que se creará, cúmple los requisitos para almacenar en la tabla SQL?
            serializador.save()
            return Response({"Éxito": True})
        return Response(serializador.errors, HTTP_400_BAD_REQUEST)
