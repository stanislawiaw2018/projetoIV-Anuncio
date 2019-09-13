from django.db import models

# Create your models here.
class Anuncio(models.Model):
    cliente = models.CharField(max_length=50)
    Titulo = models.CharField(max_length=80)
    preco = models.DecimalField(decimal_places=2,max_digits=2)
    Anuncio = models.TextField()
    nome_contato = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    secao = models.CharField(max_length=10)
    tipo_anuncio = models.CharField(max_length=100)

    def __str__(self):
        return self.Titulo
