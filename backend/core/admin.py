from django.contrib import admin
from .models import Atributo, CategoriaPaleta, CategoriaCor, CategoriaComodo, Cidade, Cor, Comodo, Embalagem, Estado

# Register your models here.
admin.site.register(Atributo)
admin.site.register(CategoriaPaleta)
admin.site.register(CategoriaCor)
admin.site.register(CategoriaComodo)
admin.site.register(Cidade)
admin.site.register(Cor)
admin.site.register(Comodo)
admin.site.register(Embalagem)
admin.site.register(Estado)