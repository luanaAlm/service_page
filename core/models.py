from django.db import models


class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    mensagem = models.TextField()

    def __str__(self):
        template = '{0.nome} {0.email} {0.telefone} {0.mensagem}'
        return template.format(self)
