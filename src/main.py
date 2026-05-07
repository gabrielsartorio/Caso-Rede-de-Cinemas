from src.controller.filme_controller import FilmeController

if __name__ == "__main__":
    controller = FilmeController()
    
    # Teste de inclusão
    resultado = controller.adicionar_filme(
        titulo="Duna: Parte 2",
        genero="Ficção Científica",
        duracao=165,
        diretor="Denis Villeneuve",
        elenco="Timothée Chalamet, Zendaya"
    )
    print(resultado)
    
    # Listagem
    print("\nLista de filmes no banco de dados:")
    for f in controller.listar():
        print(f"- {f['titulo']}")