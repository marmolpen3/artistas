from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=20)
    url = models.URLField(validators=[URLValidator()])
    url_imagen = models.URLField(validators=[URLValidator()])

class Etiqueta(models.Model):
    valor = models.CharField(max_length=80)

class UsuarioArtista(models.Model):
    usuario = models.IntegerField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    tiempo_escuchado = models.IntegerField()

class UsuarioEtiquetaArtista(models.Model):
    usuario = models.IntegerField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    dia = models.PositiveSmallIntegerField()
    mes = models.PositiveSmallIntegerField()
    anyo = models.PositiveSmallIntegerField()