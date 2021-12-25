from django.db import models


class Cidades(models.Model):
    cidade = models.CharField("Cidade", max_length=20)
    estado = models.CharField("Estado", max_length=20)
    siglaEstado = models.CharField("Sigla do Estado", max_length=3)
    
    