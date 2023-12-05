import pytest
from biblioteca import Biblioteca,livro
from cliente import Cliente

from multa import MultasPorAtraso

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca Teste")

@pytest.fixture
def cliente():
    return Cliente("João", 25, "Estudante")

@pytest.fixture
def livro():
    return livro("Aventuras na Biblioteca", "Autor Teste", "123456789")

@pytest.fixture
def multas():
    return MultasPorAtraso(taxa_multa_por_dia=5.0)

def test_aplicar_multa(biblioteca, cliente, livro, multas):
    biblioteca.adicionar_cliente(cliente)
    biblioteca.adicionar_livro(livro)
    cliente.entrar_na_biblioteca(biblioteca)

    biblioteca.emprestar_livro(livro.isbn)
    livro.disponivel = False

    # Simulando atraso de 3 dias
    multas.aplicar_multa(cliente, livro, dias_atraso=3)

    # Verifica se a multa foi aplicada corretamente
    multas_cliente = multas.obter_multas_cliente(cliente)
    assert livro.titulo in multas_cliente
    assert multas_cliente[livro.titulo]['valor'] == 15.0
    assert 'data_aplicacao' in multas_cliente[livro.titulo]
