from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=20)
    url = models.URLField(validators=[URLValidator()])
    url_imagen = models.URLField(validators=[URLValidator()])
