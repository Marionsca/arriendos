from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class UserProfile(models.Model):
    roles = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador')
    )# una tupla de tupla el primer campo es el que va a guardar la bd y le da el pase a choice para elegir arrendatario o arrendador
    direccion = models.CharField(max_length=255)
    telefono_personal = models.CharField(max_length=20, null=True)
    rol = models.CharField(max_length=50, default='arrendatario', choices=roles) #el choice me permite que sea un arrendatario o arrendador
    user = models.OneToOneField(
        User,
        related_name='userprofile',
        on_delete=models.CASCADE
    )

#modelo region, tienen codigo max 5 y con llave primaria
class Region(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
#modelo comuna tiene codigo y depende de region por que 1 region tiene muchas comunas, 
class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region,
        on_delete=models.RESTRICT, #si se borra una region no se puede borrar la comuna
        related_name='comunas'
    )

class Inmueble(models.Model):
    inmuebles = (#se puede elegir casa, depto o parcela y tienen los campos que estan abajo
        ('casa', 'Casa'),
        ('departamento','Departamento'),
        ('parcela', 'Parcela')
    )
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
    num_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    num_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    num_baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=255)
    precio_mensual_arriendo = models.IntegerField(validators=[MinValueValidator(1000)])
    tipo_de_inmueble = models.CharField(max_length=20, choices=inmuebles)
    comuna = models.ForeignKey(
        Comuna,
        related_name='inmuebles',
        on_delete=models.RESTRICT
    )
    propietario = models.ForeignKey(
        User,
        related_name='inmuebles',
        on_delete=models.RESTRICT
    )