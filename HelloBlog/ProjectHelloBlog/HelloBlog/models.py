from django.db import models

# Create your models here.

class Publicacao(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    conteudo = models.TextField()
    dt_publicacao = models.DateTimeField(auto_now_add=True)
    thumnail = models.ImageField(upload_to='imagens/')
    titulo = models.CharField(max_length=150)

    class Meta:
        ordering = ['-dt_publicacao']
