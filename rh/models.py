from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    telefone = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    telefone = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return self.nome