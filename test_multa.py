import datetime
import pytest

# Suponha que as classes estejam em um módulo chamado multas.py
from multa import MultasPorAtraso

@pytest.fixture
def multas():
    return MultasPorAtraso(taxa_multa_por_dia=2.0)

class ClienteMock:
    def __init__(self, nome):
        self.nome = nome

class LivroMock:
    def __init__(self, titulo):
        self.titulo = titulo

def test_aplicar_multa(multas):
    cliente = ClienteMock("Alice")
    livro = LivroMock("Python Avançado")
    dias_atraso = 5

    multas.aplicar_multa(cliente, livro, dias_atraso)

    # Verifica se a multa foi aplicada corretamente
    multas_cliente = multas.obter_multas_cliente(cliente)
    assert len(multas_cliente) == 1
    assert multas_cliente[livro.titulo]['valor'] == 2.0 * dias_atraso

def test_calcular_total_multas_cliente(multas):
    cliente = ClienteMock("Bob")
    livro1 = LivroMock("Data Science")
    livro2 = LivroMock("Machine Learning")

    # Aplica multas para diferentes livros
    multas.aplicar_multa(cliente, livro1, dias_atraso=3)
    multas.aplicar_multa(cliente, livro2, dias_atraso=7)

    # Calcula o total de multas para o cliente
    total_multas = multas.calcular_total_multas_cliente(cliente)

    # Verifica se o total de multas foi calculado corretamente
    assert total_multas == (2.0 * 3) + (2.0 * 7)
