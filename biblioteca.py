import json

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

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

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca."""
        self.livros.append(livro)

    def listar_livros(self):
        """Lista todos os livros na biblioteca."""
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"{livro.titulo} - {livro.autor} ({status})")

    def adicionar_cliente(self, cliente):
        """Adiciona um cliente à biblioteca."""
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado na biblioteca {self.nome}.")

    def listar_clientes(self):
        """Lista todos os clientes da biblioteca."""
        for cliente in self.clientes:
            print(f"{cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf}")

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

    def buscar_livro_por_titulo(self, titulo):
        """Busca um livro pelo título na biblioteca."""
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def salvar_biblioteca(self, arquivo):
        """Salva o estado atual da biblioteca em um arquivo JSON."""
        biblioteca_json = {
            'nome': self.nome,
            'livros': [
                {'titulo': livro.titulo, 'autor': livro.autor, 'isbn': livro.isbn, 'disponivel': livro.disponivel}
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
            Livro(livro['titulo'], livro['autor'], livro['isbn']) for livro in biblioteca_json['livros']
        ]
        self.clientes = [
            Cliente(cliente['nome'], cliente['idade'], cliente['cpf']) for cliente in biblioteca_json['clientes']
        ]
        print(f"Biblioteca {self.nome} carregada de {arquivo}.")

    def contar_livros_disponiveis(self):
        """Conta o número total de livros disponíveis na biblioteca."""
        return sum(1 for livro in self.livros if livro.disponivel)