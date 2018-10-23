from django.urls import path
from . import views as eventos

app_name = 'sistema_eventos'

urlpatterns = [
    path('', eventos.Home.as_view(), name='home'),
    path('novo/evento/', eventos.CadastrarEvento.as_view(), name='cadastrar-evento'),
    path('meus/eventos/', eventos.MeusEventos.as_view(), name='meus-eventos'),
    path('evento/<pk>', eventos.DetalhesEvento.as_view(), name='detalhes-evento'),
    path('evento/<pk>/adicionar/minicurso/', eventos.AdicionarMinicurso.as_view(), name='adicionar-minicurso'),
    path('evento/<pk>/adicionar/palestra/', eventos.AdicionarPalestra.as_view(), name='adicionar-palestra'),
    path('novo/palestrante/', eventos.AdicionarPalestrante.as_view(), name='adicionar-palestrante'),
    path('inscrever/minicurso/<pk>', eventos.InscreverMinicurso.as_view(), name='inscrever-minicurso'),
    path('inscrever/palestra/<pk>', eventos.InscreverPalestra.as_view(), name='inscrever-palestra'),
    path('lista/<pk>', eventos.Lista.as_view(), name='lista'),
    path('eventos/disponiveis', eventos.VisualizarEventos.as_view(), name='visualizar-eventos'),
]