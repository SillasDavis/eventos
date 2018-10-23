from django.contrib import admin
from .models import Atividade, Palestrante, Evento

admin.site.register(Atividade)
admin.site.register(Palestrante)
admin.site.register(Evento)