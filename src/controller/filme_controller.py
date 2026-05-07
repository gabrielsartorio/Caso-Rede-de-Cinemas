from src.service.filme_service import FilmeService

class FilmeController:
    def __init__(self):
        self.service = FilmeService()

    def adicionar_filme(self, titulo, genero, duracao, diretor, elenco):
        try:
            fid = self.service.cadastrar_filme(titulo, genero, duracao, diretor, elenco)
            return f"Sucesso! Filme salvo com ID {fid}"
        except Exception as e:
            return f"Erro: {e}"

    def listar(self):
        return self.service.listar_filmes()
