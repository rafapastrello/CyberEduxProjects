from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    dt_publicacao = models.DateTimeField(auto_now_add=True)
    resumo = models.TextField()
    slug = models.SlugField()
    img_url = models.CharField(max_length=200)

    class Meta:
        ordering = ['-dt_publicacao']
