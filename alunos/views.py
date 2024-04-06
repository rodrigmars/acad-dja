from django.shortcuts import render
from .models import Aluno


def home(request):
    return render(request, "alunos/home.html")


def aluno_lista(request):
    alunos = Aluno.objects.all()

    return render(request, "alunos/aluno_lista.html", {"alunos": alunos})
