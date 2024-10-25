from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    dni = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)