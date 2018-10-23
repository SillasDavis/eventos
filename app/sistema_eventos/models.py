from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Atividade(CreateUpdateModel):
    palestrante = models.ForeignKey('Palestrante', on_delete=models.CASCADE, related_name='eventos', verbose_name='evento')
    nome = models.CharField(max_length=255, verbose_name='nome da atividade')
    data = models.DateField()
    hora = models.TimeField()
    inscricoes = models.ManyToManyField(UUIDUser, related_name='inscritos', verbose_name='inscrições', blank=True)

    def __str__(self):
        return self.nome

class Palestrante(CreateUpdateModel):
    nome = models.CharField(max_length=255, verbose_name='nome do palestrante')

    def __str__(self):
        return self.nome

class Evento(CreateUpdateModel):
    criador = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='creator', verbose_name='criador')
    nome = models.CharField(max_length=255, verbose_name='nome do evento')
    lista_minicursos = models.ManyToManyField(Atividade, related_name='minicursos', blank=True)
    lista_palestras = models.ManyToManyField(Atividade, related_name='palestras', blank=True)

    def __str__(self):
        return self.nome
