from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    dirección = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    teléfono = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Cotización(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    fechaSolicitud = models.DateField()
    numeroSeguimiento = models.PositiveIntegerField()
    peso = models.PositiveIntegerField()
    dimensiones = models.IntegerField()
    fechaInicio = models.DateField()
    lugarOrigen = models.CharField(max_length=50)
    lugarDestino = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente.nombre
    
    class Meta:
        verbose_name_plural = "Cotizaciones"


class Vehículo(models.Model):
    modelo = models.CharField(max_length=50)

    def __str__(self):
            return self.modelo
    

class Bitacora(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    numeroSeguimiento = models.PositiveIntegerField()
    comentario = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    valor = models.FloatField()
    transportista = models.ManyToManyField(User, related_name='Transportistas', blank=True)

    def __str__(self):
        return self.estado

    def __str__(self):
        return self.cliente.nombre
    
    def get_transportistas(self):
        return self.transportista.filter(groups__name='Transportistas').exclude(is_superuser=True)
    