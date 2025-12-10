from django.db import models
from espectro_cores.models import Cor

class TemaDiario(models.Model):
    nome = models.CharField(max_length=200)
    cor_correta = models.ForeignKey(Cor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Create your models here.
