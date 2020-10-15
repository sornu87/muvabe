from django.db import models
from datetime import datetime  
from django.utils import timezone


# Create your models here.
class Empresa(models.Model):
    nome_empresa = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome_empresa
    



class Eoi(models.Model):
      
    STATUS = (
       ('draft', 'Draft'),
       ('submetido','Submetido'),
       ('publicado','Publicado'),
       )

    assunto = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100)
    data_pulicacao = models.DateField(default=timezone.now)
    data_limite = models.DateField(default=timezone.now)
    data_sessao_QA = models.DateField(default=timezone.now)
    is_new = models.BooleanField(default=True)
    empresa_pulicadora = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estado_eoi = models.CharField(
       max_length=32,
       choices=STATUS,
       default='available',
   )

    def __str__(self):
        return self.assunto
    