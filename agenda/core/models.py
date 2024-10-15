from django.db import models

# Create your models here.

#classe que representa a tabela Evento no banco de dados
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)


    #forçar o nome da tabela ser evento
    class Meta:
        db_table = "evento"