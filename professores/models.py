from django.db import models
from ninja.models import Ninja

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    idade = models.IntegerField()
    ninjas = models.ManyToManyField(Ninja)

    def __str__(self):
        return self.nome
        
