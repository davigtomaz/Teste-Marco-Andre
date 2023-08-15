from django.db import models

from garagem.models import Categoria, Marca

class Modelo(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelo")
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelo")

