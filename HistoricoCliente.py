# historico_cliente.py
import cliente 
import pytest
from datetime import datetime
from HistoricoCliente import HistoricoCliente, Livro

@pytest.fixture
def historico_cliente():
    return HistoricoCliente()

@pytest.fixture
def livro():
    return Livro("Livro Teste", "Autor Teste", "1234567890")

def test_adicionar_emprestimo(historico_cliente, livro):
    data_emprestimo = datetime.now()
    historico_cliente.adicionar_emprestimo(livro, data_emprestimo)
    assert len(historico_cliente.historico_emprestimos) == 1
    emprestimo = historico_cliente.historico_emprestimos[0]
    assert emprestimo['livro'] == livro
    assert emprestimo['data_emprestimo'] == data_emprestimo

def test_adicionar_devolucao(historico_cliente, livro):
    data_devolucao = datetime.now()
    historico_cliente.adicionar_devolucao(livro, data_devolucao)
    assert len(historico_cliente.historico_emprestimos) == 1
    devolucao = historico_cliente.historico_emprestimos[0]
    assert devolucao['livro'] == livro
    assert devolucao['data_devolucao'] == data_devolucao

def test_registrar_emprestimo(historico_cliente, livro):
    historico_cliente.registrar_emprestimo(livro)
    assert len(historico_cliente.emprestimos) == 1
    assert historico_cliente.emprestimos[0] == livro

def test_listar_emprestimos(capsys, historico_cliente, livro):
    historico_cliente.registrar_emprestimo(livro)
    historico_cliente.listar_emprestimos()
    captured = capsys.readouterr()
    assert f"{livro.titulo} - Em andamento" in captured.out
