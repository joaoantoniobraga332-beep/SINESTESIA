
from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=120, blank=True)
    hex = models.CharField(max_length=7, help_text='#RRGGBB')

    def __str__(self):
        return f"{self.nome or self.hex} ({self.hex})"


# Create your models here.
