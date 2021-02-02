from django import forms
from .models import Professor, Aluno

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'endereco', 'telefone', 'data_nascimento', 'matricula']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'endereco', 'telefone', 'data_nascimento', 'matricula']