from utils.database import Database
from app.models_domain import Categoria, Produto


class CategoriaRepository:
    '''
    Responsabilidade única: acesso a dados (CRUD) da tabela Categoria.

    Não sabe nada sobre HTTP, templates ou formulários - só sabe
    ler e gravar Categorias no banco de dados.
    '''

    def listar(self):
        sql = '''
            SELECT  id,
                    descricao
            FROM Categoria
            ORDER BY descricao
        '''
        conexao = Database.get_connection()
        registros = conexao.cursor().execute(sql).fetchall()
        return [Categoria(id=r[0], descricao=r[1]) for r in registros]

    def buscar_por_id(self, id):
        sql = '''
            SELECT  id,
                    descricao
            FROM Categoria
            WHERE id = ?
        '''
        conexao = Database.get_connection()
        registro = conexao.cursor().execute(sql, (id,)).fetchone()
        return Categoria(id=registro[0], descricao=registro[1])

    def inserir(self, descricao):
        sql = "INSERT INTO Categoria(descricao) VALUES(?)"
        conexao = Database.get_connection()
        conexao.cursor().execute(sql, (descricao,))
        conexao.commit()

    def atualizar(self, id, descricao):
        sql = "UPDATE Categoria SET descricao = ? WHERE id = ?"
        conexao = Database.get_connection()
        conexao.cursor().execute(sql, (descricao, id))
        conexao.commit()

    def excluir(self, id):
        sql = "DELETE FROM Categoria WHERE id = ?"
        conexao = Database.get_connection()
        conexao.cursor().execute(sql, (id,))
        conexao.commit()


class ProdutoRepository:
    '''
    Responsabilidade única: acesso a dados (CRUD) da tabela Produto.

    Não sabe nada sobre HTTP, templates ou formulários - só sabe
    ler e gravar Produtos no banco de dados.
    '''

    def listar(self):
        sql = '''
            SELECT  pro.id,
                    pro.descricao,
                    pro.preco_unitario,
                    pro.quantidade_estoque,
                    pro.categoria_id,
                    cat.descricao as categoria
            FROM Produto pro
            INNER JOIN Categoria cat ON cat.id = pro.categoria_id
            ORDER BY pro.descricao
        '''
        conexao = Database.get_connection()
        registros = conexao.cursor().execute(sql).fetchall()
        return [Produto(id=r[0], descricao=r[1], preco_unitario=r[2],
                         quantidade_estoque=r[3], categoria_id=r[4],
                         categoria=r[5]) for r in registros]

    def buscar_por_id(self, id):
        sql = '''
            SELECT  pro.id,
                    pro.descricao,
                    pro.preco_unitario,
                    pro.quantidade_estoque,
                    pro.categoria_id,
                    cat.descricao as categoria
            FROM Produto pro
            INNER JOIN Categoria cat ON cat.id = pro.categoria_id
            WHERE pro.id = ?
        '''
        conexao = Database.get_connection()
        registro = conexao.cursor().execute(sql, (id,)).fetchone()
        return Produto(id=registro[0], descricao=registro[1], preco_unitario=registro[2],
                        quantidade_estoque=registro[3], categoria_id=registro[4],
                        categoria=registro[5])

    def inserir(self, descricao, preco_unitario, quantidade_estoque, categoria_id):
        sql = '''
            INSERT INTO Produto (descricao, preco_unitario, quantidade_estoque, categoria_id)
            VALUES (?, ?, ?, ?)
        '''
        conexao = Database.get_connection()
        conexao.cursor().execute(sql, (descricao, preco_unitario, quantidade_estoque, categoria_id))
        conexao.commit()

    def atualizar(self, id, descricao, preco_unitario, quantidade_estoque, categoria_id):
        sql = '''
            UPDATE Produto
            SET descricao = ?, preco_unitario = ?, quantidade_estoque = ?, categoria_id = ?
            WHERE id = ?
        '''
        conexao = Database.get_connection()
        conexao.cursor().execute(sql, (descricao, preco_unitario, quantidade_estoque, categoria_id, id))
        conexao.commit()

    def excluir(self, id):
        sql = "DELETE FROM Produto WHERE id = ?"
        conexao = Database.get_connection()
        conexao.cursor().execute(sql, (id,))
        conexao.commit()
