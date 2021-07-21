from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify


class Cadastro(models.Model):
    sigla = models.CharField('Sigla', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    escudo = models.CharField('Escudo', max_length=100)
    serie = models.CharField('Serie', max_length=1)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.sigla

def Cadastro_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.sigla)

    class Meta:
        model = Cadastro

signals.pre_save.connect(Cadastro_pre_save, sender = Cadastro)

