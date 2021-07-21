from django import forms
from django.db.models import fields
from .models import Cadastro

class CadastroForm(forms.Form):
    sigla = forms.CharField(label='Sigla ')
    nome = forms.CharField(label='Nome ')
    cidade = forms.CharField(label='Cidade ')
    escudo = forms.CharField(label='Escudo ')
    serie = forms.CharField(label='Serie')

    def send(self):
        sigla = self.cleaned_data['sigla']
        nome = self.cleaned_data['nome']
        cidade = self.cleaned_data['cidade']
        escudo = self.cleaned_data['escudo']
        serie = self.cleaned_data['serie']


class CadastroModelForm(forms.ModelForm):
   
    class Meta:
        model = Cadastro
        fields = ['sigla', 'nome', 'cidade', 'escudo', 'serie']
