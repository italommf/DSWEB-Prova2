from urllib import request
from django.shortcuts import get_object_or_404, render
from .models import Aluno, Rendimento, Diario

def aprovado(request, matricula):
    aluno = get_object_or_404(Aluno, matricula = matricula)
    rendimento_aluno = get_object_or_404(Rendimento) 
    context = {
        'aluno': aluno,
        'rendimento': rendimento_aluno,
    }
    return render(request, 'prova/aprovado.html', context)

def info_disciplinas(request, id):
    #diario = get_object_or_404(Diario, id = id)
    diario = Diario.objects.filter(id=id)
    context = {
        'diario': diario
    }
    return render(request, 'prova/disciplina.html', context)