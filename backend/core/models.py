from django.db import models


class Cidade(models.Model):
    cidade = models.CharField("Cidade", max_length=20)
    estado = models.CharField("Estado", max_length=20)
    siglaEstado = models.CharField("Sigla do Estado", max_length=3)


class Cor(models.Model):
    pass


"""Verificar isso aqui"""
# class Tintas(models.Model):
#     nome = models.CharField("Nome", blank=False, null=False, max_length=50)
#     referencia = models.CharField("Referência", blank=False, null=False, max_length=50)
#     codigoDaCor = models.CharField("Código da cor", blank=False, null=False, max_length=50)
#     categoriaDaCor = models.CharField("Categoria da cor", blank=False, null=False, max_length=50)


# class Produtos(models.Model):
#     pass


    
    