from django.db import models


class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    phone = models.CharField('Telefone', max_length=11)
    endereco = models.CharField('Endereço', max_length=200)

    def __str__(self):
        return self.nome
