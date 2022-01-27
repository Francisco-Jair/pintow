from django.shortcuts import render, redirect
from backend.core.forms import CidadeForms

def home(request):
    """Função que comanda a página inicial"""

    if request.method == "POST":
        form = CidadeForms(request.POST)
        
        if form.is_valid():
            pass
            # print(form.cleaned_data['cidades'])
            # return redirect('https://www.google.com/')

        formulario = CidadeForms()
    else:
        formulario = CidadeForms()
    
    context = {
        "title" : "Pitow - Home",
        "cidadeForms" : formulario
    }

    return render(request, 'core/home.html', context)


def escolher_cidade(request):
    """Função que muda a cidade e com isso os itens"""
    pass