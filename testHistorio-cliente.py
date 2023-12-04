# test_historico_cliente.py
from datetime import datetime
import pytest
from HistoricoCliente import HistoricoCliente

@pytest.fixture
def historico_cliente():
    return HistoricoCliente()

def test_adicionar_emprestimo(historico_cliente):
    livro_emprestado = {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien'}
    data_emprestimo = datetime.now()
    
    historico_cliente.adicionar_emprestimo(livro_emprestado, data_emprestimo)

    assert len(historico_cliente.historico_emprestimos) == 1
    assert historico_cliente.historico_emprestimos[0]['livro'] == livro_emprestado
    assert historico_cliente.historico_emprestimos[0]['data_emprestimo'] == data_emprestimo

def test_adicionar_devolucao(historico_cliente):
    livro_devolvido = {'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes'}
    data_devolucao = datetime.now()
    
    historico_cliente.adicionar_devolucao(livro_devolvido, data_devolucao)

    assert len(historico_cliente.historico_emprestimos) == 1
    assert historico_cliente.historico_emprestimos[0]['livro'] == livro_devolvido
    assert historico_cliente.historico_emprestimos[0]['data_devolucao'] == data_devolucao