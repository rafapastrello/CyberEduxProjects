from django.db import models

# Create your models here.

'''
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=200)
    autor = models.CharField(max_length=201)
    dt_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dt_publicacao']
'''

class Publicacao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=200)
    autor = models.CharField(max_length=201)
    dt_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dt_publicacao']