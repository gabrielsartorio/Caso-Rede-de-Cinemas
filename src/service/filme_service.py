from src.repository.filme_repository import FilmeRepository

class FilmeService:
    def __init__(self):
        self.repo = FilmeRepository()

    def cadastrar_filme(self, titulo, genero, duracao, diretor, elenco):
        if not titulo or duracao <= 0:
            raise ValueError("Título ou duração inválidos.")
        filme = {
            "titulo": titulo, "genero": genero, 
            "duracao": duracao, "diretor": diretor, 
            "elenco": elenco
        }
        return self.repo.salvar(filme)

    def listar_filmes(self):
        return self.repo.obter_todos()
