from django.db import models

# Create your models here.
class Produtos(models.Model):
    nomeProduto = models.CharField(max_length=50)  # Nome do produto, limitado a 50 caracteres
    categoria = models.CharField(max_length=50)  # Categoria como texto simples
    quantidadeDoEstoque = models.IntegerField()  # Quantidade em número
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço com casas decimais