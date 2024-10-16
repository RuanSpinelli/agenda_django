from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#classe que representa a tabela Evento no banco de dados
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name="Data do evento")
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data que você anotou")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    #forçar o nome da tabela no db ser o mesmo nome da classe
    class Meta:
        db_table = "evento"

    #faz com que o nome do objeto criado seja o mesmo do titulo
    def __str__(self):
        return self.titulo
    

    def get_data_evento(self):
        return self.data_evento.strftime("%d/%m/%y %H:%M")