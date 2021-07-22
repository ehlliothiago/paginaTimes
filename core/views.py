from django.shortcuts import render, redirect, get_object_or_404
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
        try:       
            serie = request.GET['serie']
        except:
            serie = ""
        if serie == 'A':
            times = Cadastro.objects.filter(serie='A')
        elif serie == 'B':
            times = Cadastro.objects.filter(serie='B')
        else:
            times = Cadastro.objects.all()


        context = {
            'form': form,
            'times': times
        }
        return render(request, 'cadastro.html', context)

def delete_times(request, id):
    times = get_object_or_404(Cadastro, pk=id)
    if request.method == 'POST':
        times.delete()
        return redirect('cadastro')

    return render(request, 'times_confirme_delete.html', {'times': times})
