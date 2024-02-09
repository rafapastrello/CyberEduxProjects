from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    conteudo = models.TextField()
    autor = models.TextField()
    dt_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dt_publicacao']
