from django.db import models
# from django.contrib.auth.models import User
from django.shortcuts import reverse

class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('clientes_lista')

    def __str__(self):
        return self.nome