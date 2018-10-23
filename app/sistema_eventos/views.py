from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, View
from .models import Evento, Atividade, Palestrante
from django.urls import reverse_lazy

class Home(View):
    def get(self, request):
        return render(request, 'base.html')

class CadastrarEvento(CreateView):
    model = Evento
    fields = ['criador', 'nome']
    success_url = reverse_lazy('sistema_eventos:home')
    template_name = 'sistema_eventos/add-evento.html'

class MeusEventos(ListView):
    model = Evento
    template_name = 'sistema_eventos/meus-eventos.html'

    def get_context_data(self, **kwargs):
        kwargs['eventos'] = Evento.objects.filter(criador = self.request.user)
        return super(MeusEventos, self).get_context_data(**kwargs)

class DetalhesEvento(DetailView):
    model = Evento
    template_name = 'sistema_eventos/detalhes-evento.html'

class AdicionarMinicurso(View):
    def get(self, request, pk):
        palestrantes = Palestrante.objects.all()
        return render(request, 'sistema_eventos/add-minicurso.html', {'palestrantes': palestrantes})

    def post(self, request, pk):
        evento = Evento.objects.filter(id = pk).first()
        palestrante = Palestrante.objects.filter(id = request.POST.get('palestrante')).first()
        atividade = Atividade(palestrante=palestrante, nome=request.POST.get('nome'), data=request.POST.get('data'), hora=request.POST.get('hora'))
        atividade.save()
        evento.lista_minicursos.add(atividade)
        evento.save()
        return redirect('sistema_eventos:detalhes-evento', pk = pk)

class AdicionarPalestra(View):
    def get(self, request, pk):
        palestrantes = Palestrante.objects.all()
        return render(request, 'sistema_eventos/add-palestra.html', {'palestrantes': palestrantes})

    def post(self, request, pk):
        evento = Evento.objects.filter(id = pk).first()
        palestrante = Palestrante.objects.filter(id = request.POST.get('palestrante')).first()
        atividade = Atividade(palestrante=palestrante, nome=request.POST.get('nome'), data=request.POST.get('data'), hora=request.POST.get('hora'))
        atividade.save()
        evento.lista_palestras.add(atividade)
        evento.save()
        return redirect('sistema_eventos:detalhes-evento', pk = pk)

class AdicionarPalestrante(CreateView):
    model = Palestrante
    success_url = reverse_lazy('sistema_eventos:meus-eventos')
    template_name = 'sistema_eventos/add-palestrante.html'
    fields = ['nome']

class InscreverMinicurso(View):
    def get(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        eventos = Evento.objects.all()
        aux = None
        for evento in eventos:
            if atividade in evento.lista_minicursos.all():
                aux = evento
                break
        aux2 = 0
        for minicurso in evento.lista_minicursos.all():
            if self.request.user in minicurso.inscricoes.all():
                aux2 += 1
        if aux2 == 2:
            return render(request, 'sistema_eventos/error.html', {'mensagem': 'Não foi possível realizar sua inscrição, pois você está excedendo o limite de inscrições em minicursos.'})
        atividade.inscricoes.add(self.request.user)
        atividade.save()
        return redirect('sistema_eventos:home')


class InscreverPalestra(View):
    def get(self, request, pk):
        atividade = Atividade.objects.filter(id = pk).first()
        atividade.inscricoes.add(self.request.user)
        atividade.save()
        return redirect('sistema_eventos:home')

class Lista(DetailView):
    model = Atividade
    template_name = 'sistema_eventos/lista.html'

class VisualizarEventos(ListView):
    model = Evento
    template_name = 'sistema_eventos/visualizar-eventos.html'
