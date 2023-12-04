# historico_cliente.py
class HistoricoCliente:
    def __init__(self):
        self.historico_emprestimos = []

    def adicionar_emprestimo(self, livro, data_emprestimo):
        """Adiciona um registro de empréstimo ao histórico."""
        emprestimo = {'livro': livro, 'data_emprestimo': data_emprestimo}
        self.historico_emprestimos.append(emprestimo)

    def adicionar_devolucao(self, livro, data_devolucao):
        """Adiciona um registro de devolução ao histórico."""
        devolucao = {'livro': livro, 'data_devolucao': data_devolucao}
        self.historico_emprestimos.append(devolucao)