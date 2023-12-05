import pytest
from biblioteca import Biblioteca,Livro
from cliente import Cliente
from HistoricoCliente import HistoricoCliente
from Emprestimo import Emprestimo
import datetime

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca Teste")

@pytest.fixture
def cliente():
    return Cliente("Fulano", 25, "Estudante")

@pytest.fixture
def livro():
    return livro("Aventuras na Biblioteca", "Autor Teste", "123456789")

def test_emprestimo_devolucao(biblioteca: Biblioteca, cliente: Cliente, Livro: livro):
    biblioteca.adicionar_cliente(cliente)
    biblioteca.adicionar_livro(livro)

    cliente.entrar_na_biblioteca(biblioteca)

    emprestimo = cliente.biblioteca.emprestar_livro(livro.isbn)
    assert emprestimo is not None
    assert not livro.disponivel

    emprestimo.devolver()
    assert livro.disponivel

def test_historico_cliente(biblioteca: Biblioteca, cliente: Cliente, livro: livro):
    biblioteca.adicionar_cliente(cliente)
    biblioteca.adicionar_livro(livro)

    cliente.entrar_na_biblioteca(biblioteca)

    emprestimo = cliente.biblioteca.emprestar_livro(livro.isbn)
    cliente.biblioteca.devolver_livro(livro.isbn)

    historico = HistoricoCliente(cliente)
    historico.registrar_emprestimo(emprestimo)

    assert len(historico.emprestimos) == 1
    assert historico.emprestimos[0].livro == livro
