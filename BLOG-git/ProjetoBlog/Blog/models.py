from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    resumo = models.TextField()
    slug = models.SlugField()
    img_url = models.CharField(max_length=200)

    class Meta:
        ordering = ['-publicado_em']
