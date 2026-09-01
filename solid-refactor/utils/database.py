import sqlite3


class Database:
    '''
    Responsabilidade única: fornecer a conexão com o banco de dados.

    Nenhuma outra classe deve saber COMO a conexão é aberta -
    se mudarmos de SQLite para outro banco no futuro, só este
    arquivo precisa ser alterado.
    '''

    _DB_PATH = 'db_solid.sqlite3'

    @staticmethod
    def get_connection():
        conexao = sqlite3.connect(Database._DB_PATH)
        # não permite DELETE CASCADE (exclusão em cascata)
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao
