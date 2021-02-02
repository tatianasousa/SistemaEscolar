from django.shortcuts import render, redirect
from .forms import ProfessorForm, AlunoForm
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html', {})

def rhHomePage(request):
    return render(request, 'rh.html', {})

def cadastrarProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_professor')
    else:
        form = ProfessorForm()
    return render(request, 'cadastroProfessor.html', {'form':form})

def cadastrarAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_aluno')
    else:
        form = ProfessorForm()
    return render(request, 'cadastro_aluno.html', {'form':form})