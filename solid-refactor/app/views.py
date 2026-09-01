from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.forms import CategoriaForm, ProdutoForm
from app.repositories import CategoriaRepository, ProdutoRepository


# Método responsavel por listar, incluir, alterar e excluir as Categorias.
def categorias(request, acao=None, id=None):
    '''
    Método responsavel por receber todas as rotas URL do cadastro de Categorias.

    De acordo com a "acao" e o "id" informados, esse metodo irá:
      - 'categorias/': Exibir a pagina de listagem
      - 'categorias/incluir/': Exibir a pagina de inclusão
      - 'categorias/alterar/<:id>/': Exibir a pagina de alteração
      - 'categorias/excluir/<:id>/': Exibir a pagina de exclusão
      - 'categorias/salvar/': insere, altera ou exclui um registro

    Note que este método não sabe mais COMO os dados são lidos ou
    gravados: quem faz isso é o CategoriaRepository. A view só
    orquestra a requisição HTTP e decide qual template renderizar.
    '''
    repositorio = CategoriaRepository()

    try:
        # Listar registros
        # 'categorias/': Exibir a pagina de listagem
        if acao is None:
            registros = repositorio.listar()
            return render(request, 'categorias_listar.html', context={'registros': registros})

        # Salvar registro
        # 'categorias/salvar/': insere, altera ou exclui um registro
        elif acao == 'salvar':
            form_data = request.POST
            acao_form = form_data['acao']

            if acao_form == 'Inclusão':
                repositorio.inserir(form_data['descricao'])

            elif acao_form == 'Exclusão':
                repositorio.excluir(form_data['id'])

            else:
                repositorio.atualizar(form_data['id'], form_data['descricao'])

            # Sempre retornar um HttpResponseRedirect após processar dados "POST".
            # Isso evita que os dados sejam postados 2 vezes caso usuário clicar "Voltar".
            return HttpResponseRedirect(reverse("categorias"))

        # inserir registro
        # 'categorias/incluir/': Exibir a pagina de inclusão
        elif acao == 'incluir':
            return render(request, 'categorias_editar.html',
                           context={'acao': 'Inclusão', 'form': CategoriaForm()})

        # Alterar ou excluir registro
        # 'categorias/alterar/<:id>/': Exibir a pagina de alteração
        # 'categorias/excluir/<:id>/': Exibir a pagina de exclusão
        elif acao in ['alterar', 'excluir']:
            registro = repositorio.buscar_por_id(id)
            registro_dict = {'id': registro.id, 'descricao': registro.descricao}

            acao = 'Alteração' if acao == 'alterar' else 'Exclusão'

            return render(request, 'categorias_editar.html',
                           context={'acao': acao, 'form': CategoriaForm(initial=registro_dict)})

        # acao INVALIDA
        else:
            raise Exception('Ação inválida')

    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página
    except Exception as err:
        return render(request, 'home.html', context={'ERRO': err})


# Método responsavel por listar, incluir, alterar e excluir os Produtos.
def produtos(request, acao=None, id=None):
    '''
    Método responsavel por receber todas as rotas URL do cadastro de Produtos.

    De acordo com a "acao" e o "id" informados, esse metodo irá:
      - 'produtos/': Exibir a pagina de listagem
      - 'produtos/incluir/': Exibir a pagina de inclusão
      - 'produtos/alterar/<:id>/': Exibir a pagina de alteração
      - 'produtos/excluir/<:id>/': Exibir a pagina de exclusão
      - 'produtos/salvar/': insere, altera ou exclui um registro

    Assim como em categorias(), toda a lógica de acesso a dados
    fica no ProdutoRepository - a view apenas orquestra.
    '''
    repositorio = ProdutoRepository()

    try:
        # Listar registros
        # 'produtos/': Exibir a pagina de listagem
        if acao is None:
            registros = repositorio.listar()
            return render(request, 'produtos_listar.html', context={'registros': registros})

        # Salvar registro
        # 'produtos/salvar/': insere, altera ou exclui um registro
        elif acao == 'salvar':
            form_data = request.POST
            acao_form = form_data['acao']

            if acao_form == 'Inclusão':
                repositorio.inserir(form_data['descricao'], form_data['preco_unitario'],
                                     form_data['quantidade_estoque'], form_data['categoria_id'])

            elif acao_form == 'Exclusão':
                repositorio.excluir(form_data['id'])

            else:
                repositorio.atualizar(form_data['id'], form_data['descricao'], form_data['preco_unitario'],
                                       form_data['quantidade_estoque'], form_data['categoria_id'])

            # Sempre retornar um HttpResponseRedirect após processar dados "POST".
            # Isso evita que os dados sejam postados 2 vezes caso usuário clicar "Voltar".
            return HttpResponseRedirect(reverse("produtos"))

        # inserir registro
        # 'produtos/incluir/': Exibir a pagina de inclusão
        elif acao == 'incluir':
            return render(request, 'produtos_editar.html',
                           context={'acao': 'Inclusão', 'form': ProdutoForm()})

        # Alterar ou excluir registro
        # 'produtos/alterar/<:id>/': Exibir a pagina de alteração
        # 'produtos/excluir/<:id>/': Exibir a pagina de exclusão
        elif acao in ['alterar', 'excluir']:
            registro = repositorio.buscar_por_id(id)
            registro_dict = {
                'id': registro.id,
                'descricao': registro.descricao,
                'preco_unitario': registro.preco_unitario,
                'quantidade_estoque': registro.quantidade_estoque,
                'categoria_id': registro.categoria_id,
                'categoria': registro.categoria,
            }

            acao = 'Alteração' if acao == 'alterar' else 'Exclusão'

            return render(request, 'produtos_editar.html',
                           context={'acao': acao, 'form': ProdutoForm(initial=registro_dict)})

        # acao INVALIDA
        else:
            raise Exception('Ação inválida')

    # se ocorreu algunm erro, insere a mensagem para ser exibida no contexto da página
    except Exception as err:
        return render(request, 'home.html', context={'ERRO': err})


# Exibe a página inicial da aplicação
def home(request):
    '''Exibe a pagina inicial da aplicação'''
    template = 'home.html'
    return render(request, template)
