from django.db import models

from garagem.models import Modelo, Cor, Acessorio
from uploader.models import Image

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculo')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculo")
    descricao = models.CharField(max_length=255)
    foto = models.ManyToManyField(
        Image,
        related_name="+",)

    def __str__(self):
        return f"{self.modelo} (Modelo: {self.modelo} - Ano: {self.ano} - Cor: {self.cor} ) "
    
    class Meta:
        verbose_name = "veículo"
