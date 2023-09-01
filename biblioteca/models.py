from django.db import models

# Create your models here.

class livraria(models.Model):
    
    nomeLivraria = models.CharField(max_length=250)
    
    def __str__(self):
        return f'A livraria escolhida foi: {self.nomeLivraria}'

class biblioteca(models.Model):
    
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    preco = models.FloatField()
    livraria =  models.ForeignKey(
        livraria,
        on_delete=models.CASCADE
    )
    
