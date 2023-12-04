from datetime import datetime

class Emprestimo:
    def __init__(self, livro, cliente):
        self.livro = livro
        self.cliente = cliente
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def devolver(self):
        """Registra a devolução do livro."""
        self.data_devolucao = datetime.now()
        self.livro.disponivel = True
        print(f"Livro {self.livro.titulo} devolvido por {self.cliente.nome}.")
