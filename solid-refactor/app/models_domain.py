from dataclasses import dataclass


@dataclass
class Categoria:
    '''
    Responsabilidade única: representar os dados de uma Categoria.
    Não sabe nada sobre banco de dados, HTTP ou formulários.
    '''
    id: int
    descricao: str


@dataclass
class Produto:
    '''
    Responsabilidade única: representar os dados de um Produto.
    Não sabe nada sobre banco de dados, HTTP ou formulários.
    '''
    id: int
    descricao: str
    preco_unitario: float
    quantidade_estoque: int
    categoria_id: int
    categoria: str = None
