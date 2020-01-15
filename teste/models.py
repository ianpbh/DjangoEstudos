from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField('data de publicacao')


class ImagemArtigo(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)
    ativo = models.IntegerField(default=0)
