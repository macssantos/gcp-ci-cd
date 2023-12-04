# historico_cliente.py
import cliente 
class HistoricoCliente:
    def __init__(self):
        self.historico_emprestimos = []
        self.cliente = cliente
        self.emprestimos = []

    def adicionar_emprestimo(self, livro, data_emprestimo):
        """Adiciona um registro de empréstimo ao histórico."""
        emprestimo = {'livro': livro, 'data_emprestimo': data_emprestimo}
        self.historico_emprestimos.append(emprestimo)

    def adicionar_devolucao(self, livro, data_devolucao):
        """Adiciona um registro de devolução ao histórico."""
        devolucao = {'livro': livro, 'data_devolucao': data_devolucao}
        self.historico_emprestimos.append(devolucao)
    def registrar_emprestimo(self, emprestimo):
        """Registra um empréstimo no histórico do cliente."""
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        """Lista todos os empréstimos do cliente."""
        for emprestimo in self.emprestimos:
            status = "Devolvido" if emprestimo.data_devolucao else "Em andamento"
            print(f"{emprestimo.livro.titulo} - {status}")       