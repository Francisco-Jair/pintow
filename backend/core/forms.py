from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Cidade

# Se adicionar novo elemento, não se atualiza sozinho -> Consertar
class CidadeForms(forms.ModelForm):

    # def __init__(self, *arg, **kwargs):
    #     self.fields["cidades"].label = "Preços válidos para:"

    cidade = forms.ChoiceField(label="Preços válidos para", choices=[(esc.id, esc.cidade + " - " + esc.siglaEstado) for esc in list(Cidade.objects.all())], initial='3', widget  =  forms.Select(attrs={'class' : 'form-select form-select-sm'}) )

    class Meta:
        model = Cidade
        fields = ["cidade"]
        # exclude = ["siglaEstado", "estado"]

        widgets = { 
            'cidades' : forms.Select(attrs={'class' : 'form-select form-select-sm'})
        }

  