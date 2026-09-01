from django import forms

from app.repositories import CategoriaRepository


class CategoriaForm(forms.Form):
    '''
    Responsabilidade única: definir os campos e as regras de
    validação do formulário de Categoria.
    '''
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)


class ProdutoForm(forms.Form):
    '''
    Responsabilidade única: definir os campos e as regras de
    validação do formulário de Produto.

    Não acessa o banco diretamente: pede as Categorias para o
    CategoriaRepository, que é quem sabe como buscar esses dados.
    '''
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)
    preco_unitario = forms.DecimalField(label='Preço Unitário', max_digits=10, decimal_places=2, required=True)
    quantidade_estoque = forms.IntegerField(label='Qtd. Estoque', required=True)
    categoria_id = forms.ChoiceField(label='Categoria', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categorias = CategoriaRepository().listar()
        self.fields['categoria_id'].choices = [(c.id, c.descricao) for c in categorias]
