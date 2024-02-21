from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    dt_nascimento = models.DateField()
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True, upload_to='perfil/')
    
class Publicacao(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    conteudo = models.TextField()
    dt_publicacao = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='imagens/')
    titulo = models.CharField(max_length=150)

    class Meta:
        ordering = ['-dt_publicacao']
