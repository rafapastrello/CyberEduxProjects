from django.db import models


class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.TextField()
    date = models.DateField(auto_now_add=True)
    content = models.TextField()