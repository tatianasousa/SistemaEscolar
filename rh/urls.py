from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('rh/', views.rhHomePage, name='rh'),
    path('rh/cadastro_professor/', views.cadastrarProfessor, name='cadastro_professor'),
    path('rh/cadastro_aluno/', views.cadastrarAluno, name='cadastro_aluno'),
]
