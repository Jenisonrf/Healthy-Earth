import sqlite3

class GerenciadorBancoDados:
    def __init__(self, db_file):
        # Inicializa a conexão com o banco de dados SQLite e cria um cursor.
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        # Chama o método para criar a tabela de usuários se ela não existir.
        self.criar_tabela_usuarios()

    def criar_tabela_usuarios(self):
        # Cria a tabela de usuários no banco de dados se ela não existir.
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        # Confirma as alterações no banco de dados.
        self.conn.commit()

    def adicionar_usuario(self, login, senha):
        try:
            # Tenta inserir um novo usuário na tabela.
            self.cursor.execute('INSERT INTO usuarios (login, senha) VALUES (?, ?)', (login, senha))
            # Confirma as alterações no banco de dados.
            self.conn.commit()
            return True  # Retorna True se a inserção for bem-sucedida.
        except sqlite3.IntegrityError:
            # Se o login já existir retorna False.
            return False

    def verificar_credenciais(self, login, senha):
        self.cursor.execute('SELECT senha FROM usuarios WHERE login = ?', (login,))
        resultado = self.cursor.fetchone()
        if resultado:
            hash_senha_armazenada = resultado[0]  # Obtém a senha armazenada no banco de dados.
            if senha == hash_senha_armazenada:
                return True
        return False  # Retorna False se as credenciais não forem válidas.

    def fechar_conexao(self):
        # Fecha a conexão com o banco de dados quando não é mais necessário.
        self.conn.close()
