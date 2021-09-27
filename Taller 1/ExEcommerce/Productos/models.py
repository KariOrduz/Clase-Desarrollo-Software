from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class TipoElectrodomestico(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank= True)

    def __str__(self):
        return self.nombre

    @property
    def numTipos(self):
        return len(TipoElectrodomestico.objects.all())

    @property 
    def numProductos(self):
        productos = Producto.objects.filter(tipo=self)
        productos = self.producto_set.all()
        return len(productos)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoElectrodomestico, on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.TextField()
    foto = models.ImageField(null=True, blank=True)
    calificacion = models.FloatField(default=0.0)

    def __str__(self):
        return self.nombre

    @property
    def tipoProducto(self):
        return self.tipo.nombre

    def calcularCalificacion(self):
        pass
 
class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.FloatField(default=0.0)
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return self.usuario + " - " + self.producto.nombre

    @property
    def productoNombre(self):
        return self.producto.nombre
