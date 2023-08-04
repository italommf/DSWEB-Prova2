from django.contrib import admin
from .models import Aluno, Rendimento, Disciplina, Diario

admin.site.register(Aluno)
admin.site.register(Rendimento)
admin.site.register(Disciplina)
admin.site.register(Diario)