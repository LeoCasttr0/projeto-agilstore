from django.forms import ModelForm
from agilstoreapp.models import Produtos

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nomeProduto','categoria','quantidadeDoEstoque','preco']