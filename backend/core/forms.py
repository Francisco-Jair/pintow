from email.policy import default
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Cidades

# Se adicionar novo elemento, não se atualiza sozinho -> Consertar
class CidadeForms(forms.ModelForm):

    # def __init__(self, *arg, **kwargs):
    #     self.fields["cidades"].label = "Preços válidos para:"

    cidades = forms.ChoiceField(label="Preços válidos para", choices=[(esc.id, esc.cidade + " - " + esc.siglaEstado) for esc in list(Cidades.objects.all())], initial='3', widget  =  forms.Select(attrs={'class' : 'form-select form-select-sm'}) )

    class Meta:
        model = Cidades
        fields = ["cidades"]
        # exclude = ["siglaEstado", "estado"]

        widgets = { 
            'cidades' : forms.Select(attrs={'class' : 'form-select form-select-sm'})
        }

  