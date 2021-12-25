from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Cidades

class CidadeForms(forms.ModelForm):

    # def __init__(self, *arg, **kwargs):
    #     self.fields["cidades"].label = "Preços válidos para:"

    cidades = forms.ChoiceField(label="Preços válidos para", choices=[(esc.id, esc.cidade + " - " + esc.siglaEstado) for esc in list(Cidades.objects.all())])

    class Meta:
        model = Cidades
        fields = ("cidades", )
        # exclude = ["siglaEstado", "estado"]

        widgets = { 
            'cidades' : forms.Select(attrs={'class' : 'form-control-select'})
        }
