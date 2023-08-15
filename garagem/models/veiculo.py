from django.db import models

from garagem.models import Modelo, Cor

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculo')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.modelo} (Marca: {self.marca} - Ano: {self.ano} - Cor: {self.cor})"
    
    class Meta:
        verbose_name = "veículo"
