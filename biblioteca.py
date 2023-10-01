import json

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca."""
        self.livros.append(livro)

    def listar_livros(self):
        """Lista todos os livros na biblioteca."""
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"{livro.titulo} - {livro.autor} ({status})")

    def emprestar_livro(self, isbn):
        """Empresta um livro da biblioteca."""
        for livro in self.livros:
            if livro.isbn == isbn and livro.disponivel:
                livro.disponivel = False
                print(f"{livro.titulo} emprestado com sucesso.")
                return
        print("Livro não encontrado ou indisponível.")

    def devolver_livro(self, isbn):
        """Devolução de um livro à biblioteca."""
        for livro in self.livros:
            if livro.isbn == isbn and not livro.disponivel:
                livro.disponivel = True
                print(f"{livro.titulo} devolvido com sucesso.")
                return
        print("Livro não encontrado ou já devolvido.")

    def salvar_biblioteca(self, arquivo):
        """Salva o estado atual da biblioteca em um arquivo JSON."""
        biblioteca_json = {
            'nome': self.nome,
            'livros': [
                {'titulo': livro.titulo, 'autor': livro.autor, 'isbn': livro.isbn, 'disponivel': livro.disponivel}
                for livro in self.livros
            ]
        }
        with open(arquivo, 'w') as f:
            json.dump(biblioteca_json, f)
        print(f"Biblioteca {self.nome} salva em {arquivo}.")

    def carregar_biblioteca(self, arquivo):
        """Carrega o estado anterior da biblioteca a partir de um arquivo JSON."""
        with open(arquivo, 'r') as f:
            biblioteca_json = json.load(f)

        self.nome = biblioteca_json['nome']
        self.livros = [
            Livro(livro['titulo'], livro['autor'], livro['isbn']) for livro in biblioteca_json['livros']
        ]
        print(f"Biblioteca {self.nome} carregada de {arquivo}.")

    def contar_livros_disponiveis(self):
        """Conta o número total de livros disponíveis na biblioteca."""
        return sum(1 for livro in self.livros if livro.disponivel)
    
    def test_buscar_livro_por_titulo(biblioteca_teste):
    # Busca um livro existente pelo título
    livro_encontrado = biblioteca_teste.buscar_livro_por_titulo("Aventuras de Python")
    assert livro_encontrado is not None
    assert livro_encontrado.titulo == "Aventuras de Python"

    # Busca um livro inexistente pelo título
    livro_nao_encontrado = biblioteca_teste.buscar_livro_por_titulo("Livro Inexistente")
    assert livro_nao_encontrado is None


# Exemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca Central")

    livro1 = Livro("Aventuras de Python", "Guido van Rossum", "123456")
    livro2 = Livro("Introdução ao Machine Learning", "Andrew Ng", "789012")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    biblioteca.listar_livros()

    biblioteca.emprestar_livro("123456")
    biblioteca.listar_livros()

    biblioteca.devolver_livro("123456")
    biblioteca.listar_livros()

    biblioteca.salvar_biblioteca("biblioteca.json")
    biblioteca.carregar_biblioteca("biblioteca.json")
