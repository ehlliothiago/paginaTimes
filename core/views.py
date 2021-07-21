from django import forms
from django.shortcuts import render
from django.contrib import messages
from .forms import  CadastroModelForm
from .models import Cadastro
def index(request):
    serieA = Cadastro.objects.filter(serie='A')
    serieB = Cadastro.objects.filter(serie='B')

    context = {
        'serieA':serieA,
        'serieB':serieB
    }
    return render(request, 'index.html', context)
def cadastro(request):
        form = CadastroModelForm(request.POST or None)
        if str(request.method) == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Time salvo com sucesso.') 
                form = CadastroModelForm()
            else:
                messages.error(request, 'Erro ao cadastrar time.') 
        
        context = {
            'form': form,
            #'times': Cadastro.objects.all()
        }
        return render(request, 'cadastro.html', context)