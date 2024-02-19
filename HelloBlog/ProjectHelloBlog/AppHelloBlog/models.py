from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    slug = models.SlugField()
    nome_img = models.CharField(max_length=200)
    dt_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dt_publicacao']
