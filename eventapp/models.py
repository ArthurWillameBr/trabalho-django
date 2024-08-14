from django.db import models

class Event(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    local = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=50)
    horario = models.TimeField()
    preco = models.FloatField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    imagem = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} - {self.tipo} em {self.local}'
