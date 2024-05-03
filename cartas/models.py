from django.db import models

# Create your models here.
class NoctaCard(models.Model):
    codigo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    rasgo1 = models.CharField(max_length=200)
    rasgo2 = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    vida = models.IntegerField()
    mana = models.IntegerField()
    dano = models.IntegerField()
    skin = models.BooleanField(default=False)
    edicion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)