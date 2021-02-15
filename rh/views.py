from django.shortcuts import render, redirect
from .forms import ProfessorForm, AlunoForm
from django.contrib import messages
from .models import *

from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html', {})

def rhHomePage(request):
    return render(request, 'rh.html', {})

def cadastrarProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            nome_p = form.cleaned_data['nome']
            endereco_p = form.cleaned_data['endereco']
            telefone_p = form.cleaned_data['telefone']
            data_nascimento_p = form.cleaned_data['data_nascimento']
            matricula_p = form.cleaned_data['matricula']
            professor = Professor(nome=nome_p, endereco=endereco_p, telefone=telefone_p, data_nascimento=data_nascimento_p, matricula=matricula_p)
            professor.save()
            return redirect('rh')
    else:
        form = ProfessorForm()
    return render(request, 'cadastroProfessor.html', {'form':form})

def cadastrarAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rh')
    else:
        form = AlunoForm()
    return render(request, 'cadastro_aluno.html', {'form':form})