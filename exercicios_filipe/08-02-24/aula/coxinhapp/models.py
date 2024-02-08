from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    estado = models.TextField()
    cidade = models.TextField()
