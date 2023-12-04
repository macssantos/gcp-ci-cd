import json

class Autor:
    def __init__(self, nome, localidade):
        self.nome = nome
        self.localidade = localidade

class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True, categoria=None):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel
        self.categoria = categoria

class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.clientes = []

    # Métodos existentes...

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca."""
        self.livros.append(livro)

    def listar_livros(self):
        """Lista todos os livros na biblioteca."""
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"{livro.titulo} - {livro.autor.nome} - Categoria: {livro.categoria} ({status})")

    # Outros métodos existentes...

    def salvar_biblioteca(self, arquivo):
        """Salva o estado atual da biblioteca em um arquivo JSON."""
        biblioteca_json = {
            'nome': self.nome,
            'livros': [
                {'titulo': livro.titulo, 'autor': livro.autor.nome, 'isbn': livro.isbn,
                 'disponivel': livro.disponivel, 'categoria': livro.categoria}
                for livro in self.livros
            ],
            'clientes': [
                {'nome': cliente.nome, 'idade': cliente.idade, 'cpf': cliente.cpf}
                for cliente in self.clientes
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
            Livro(livro['titulo'], Autor(livro['autor'], ''), livro['isbn'],
                 livro['disponivel'], livro['categoria']) for livro in biblioteca_json['livros']
        ]
        self.clientes = [
            Cliente(cliente['nome'], cliente['idade'], cliente['cpf']) for cliente in biblioteca_json['clientes']
        ]
        print(f"Biblioteca {self.nome} carregada de {arquivo}.")

    def listar_livros_por_categoria(self, categoria):
        """Lista os livros de uma determinada categoria na biblioteca."""
        livros_categoria = [livro for livro in self.livros if livro.categoria == categoria]
        if livros_categoria:
            for livro in livros_categoria:
                status = "Disponível" if livro.disponivel else "Indisponível"
                print(f"{livro.titulo} - {livro.autor.nome} ({status})")
        else:
            print(f"Nenhum livro encontrado na categoria {categoria}.")

    def filtrar_autores_por_localidade(self, localidade):
        """Filtra autores por localidade na biblioteca."""
        autores_localidade = set([livro.autor.nome for livro in self.livros if livro.autor.localidade == localidade])
        if autores_localidade:
            print(f"Autores na localidade {localidade}:")
            for autor_nome in autores_localidade:
                print(autor_nome)
        else:
            print(f"Nenhum autor encontrado na localidade {localidade}.")

    def localizar_livro(self, titulo=None, autor=None, isbn=None):
        """Localiza um livro na biblioteca com base em critérios específicos."""
        for livro in self.livros:
            if (
                (titulo is None or livro.titulo.lower() == titulo.lower()) and
                (autor is None or livro.autor.nome.lower() == autor.lower()) and
                (isbn is None or livro.isbn == isbn)
            ):
                return livro

        return None