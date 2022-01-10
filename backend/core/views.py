from django.shortcuts import render, redirect
from backend.core.models import Cidades
from backend.core.forms import CidadeForms

# Create your views here.
def home(request):

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
        "title" : "Pintow - Home",
        # "cidades" : Cidades.objects.all(),
        "cidadeForms" : formulario
    }

    return render(request, 'core/home.html', context)