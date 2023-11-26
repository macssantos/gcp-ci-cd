class Cliente:
    def __init__(self, nome, idade, ocupacao):
        self.nome = nome
        self.idade = idade
        self.ocupacao = ocupacao
        self.biblioteca = None

    def entrar_na_biblioteca(self, biblioteca):
        """Usuário entra em uma biblioteca."""
        self.biblioteca = biblioteca
        print(f"{self.nome} entrou na biblioteca {self.biblioteca.nome}.")

    def procurar_livro_por_titulo(self, titulo):
        """Usuário procura por um livro na biblioteca."""
        if self.biblioteca:
            livro_encontrado = self.biblioteca.buscar_livro_por_titulo(titulo)
            if livro_encontrado:
                print(f"{self.nome} encontrou o livro: {livro_encontrado.titulo} - {livro_encontrado.autor}")
            else:
                print(f"{self.nome} não encontrou o livro com o título: {titulo}")
        else:
            print(f"{self.nome} não está em nenhuma biblioteca.")

    def pegar_livro_emprestado(self, isbn):
        """Usuário pede emprestado um livro da biblioteca."""
        if self.biblioteca:
            self.biblioteca.emprestar_livro(isbn)
        else:
            print(f"{self.nome} não está em nenhuma biblioteca.")

    def devolver_livro(self, isbn):
        """Usuário devolve um livro à biblioteca."""
        if self.biblioteca:
            self.biblioteca.devolver_livro(isbn)
        else:
            print(f"{self.nome} não está em nenhuma biblioteca.")


