from django.db import models
from .columm import CATEGORIA_COR


class Atributo(models.Model):
    nome = models.CharField("Atributo", max_length=20)


class CategoriaPaleta(models.Model):
    nome = models.CharField("Nome", max_length=20)
    tituloDaPagina = models.CharField("Título da Página", max_length=50)    


class CategoriaCor(models.Model):
    nomeDaCor = models.CharField("Nome da Cor", max_length=20)
    codigoDaCor = models.CharField("Cor", max_length=10)
    corDoTexto = models.CharField("Cor do Texto", max_length=20)
    categoriaDaCor = models.CharField("Cor do Texto", choices=CATEGORIA_COR, max_length=20)


    class Meta():
        """Nome do modelo no admin"""
        verbose_name = 'Categorias de Cor'
        verbose_name_plural = 'Categorias de Cor'


class CategoriaComodo(models.Model):
    nome = models.CharField("Nome do Cômodo", max_length=50)
    codigoDaCor = models.CharField("Cor", max_length=10)
    iconeNome = models.CharField("icone", max_length=10)


class Cidade(models.Model):
    """Usando"""
    """Fazer relacionamento com o model acima"""
    cidade = models.CharField("Cidade", max_length=20)
    # Só nome e estado(relacionameto)

    estado = models.CharField("Estado", max_length=20)
    siglaEstado = models.CharField("Sigla do Estado", max_length=3)

    def __str__(self):
        """Como esse dado vai ser apresentado"""
        return (f"{self.cidade}-{self.siglaEstado}")


class Cor(models.Model):
    nome = models.CharField("Nome", max_length=20)
    referencia = models.CharField("Referência", max_length=20)
    CodigoDaCor = models.CharField("Código", max_length=20)
    # Relacionamento com Categoria de cor


    class Meta():
        """Nome do modelo no admin"""
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
        # ordering = ['nome']


class Comodo(models.Model):
    pass


class Embalagem(models.Model):
    pass


class Estado(models.Model):
    estado = models.CharField("Estado", max_length=20)
    siglaEstado = models.CharField("Sigla do Estado", max_length=3)





"""Verificar isso aqui"""
# class Tintas(models.Model):
#     nome = models.CharField("Nome", blank=False, null=False, max_length=50)
#     referencia = models.CharField("Referência", blank=False, null=False, max_length=50)
#     codigoDaCor = models.CharField("Código da cor", blank=False, null=False, max_length=50)
#     categoriaDaCor = models.CharField("Categoria da cor", blank=False, null=False, max_length=50)


# class Produtos(models.Model):
#     pass


    
    