from django.db import models

# Create your models here.

class Figura(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')