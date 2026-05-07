from src.repository.conexao import DatabaseConnection

class FilmeRepository:
    def __init__(self):
        self.conn = DatabaseConnection.get_connection()

    def salvar(self, filme):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO filmes (titulo, genero, duracao, diretor, elenco)
        VALUES (?, ?, ?, ?, ?)
        """, (filme['titulo'], filme['genero'], filme['duracao'], filme['diretor'], filme['elenco']))
        self.conn.commit()
        return cursor.lastrowid
        
    def obter_todos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM filmes")
        return [dict(row) for row in cursor.fetchall()]
