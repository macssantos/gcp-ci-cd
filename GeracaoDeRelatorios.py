import json
import datetime

class GeracaoDeRelatorios:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_livros_disponiveis(self):
        """Gera um relatório com os livros disponíveis na biblioteca."""
        relatorio = f"Relatório de Livros Disponíveis na Biblioteca {self.biblioteca.nome}\n"
        relatorio += "-" * 50 + "\n"

        for livro in self.biblioteca.livros:
            if livro.disponivel:
                relatorio += f"{livro.titulo} - {livro.autor}\n"

        return relatorio

    def gerar_relatorio_clientes(self):
        """Gera um relatório com todos os clientes da biblioteca."""
        relatorio = f"Relatório de Clientes na Biblioteca {self.biblioteca.nome}\n"
        relatorio += "-" * 50 + "\n"

        for cliente in self.biblioteca.clientes:
            relatorio += f"{cliente.nome} - Idade: {cliente.idade} - CPF: {cliente.cpf}\n"

        return relatorio

    def gerar_relatorio_emprestimos_atrasados(self, dias_atraso_limite=0):
        """Gera um relatório com os empréstimos atrasados na biblioteca."""
        relatorio = f"Relatório de Empréstimos Atrasados na Biblioteca {self.biblioteca.nome}\n"
        relatorio += "-" * 50 + "\n"

        data_atual = datetime.datetime.now()

        for livro in self.biblioteca.livros:
            if not livro.disponivel and livro.data_devolucao < data_atual:
                dias_atraso = (data_atual - livro.data_devolucao).days
                if dias_atraso > dias_atraso_limite:
                    relatorio += f"{livro.titulo} - {livro.autor} - Dias de Atraso: {dias_atraso}\n"

        return relatorio
