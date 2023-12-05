import pytest
from biblioteca import Biblioteca,livro
from cliente import Cliente

from multa import MultasPorAtraso

import datetime


@pytest.fixture
def multas_por_atraso():
    return MultasPorAtraso(taxa_multa_por_dia=2.5)

@pytest.fixture
def cliente():
    return Cliente(nome="Cliente Teste", idade=30, cpf="123.456.789-01")

@pytest.fixture
def livro():
    return livro(titulo="Livro Teste", autor="Autor Teste", isbn="1234567890")

def test_aplicar_multa(multas_por_atraso, cliente, livro):
    dias_atraso = 5

    multas_por_atraso.aplicar_multa(cliente, livro, dias_atraso)

    multas_cliente = multas_por_atraso.obter_multas_cliente(cliente)
    assert len(multas_cliente) == 1

    multa_info = multas_cliente.get(livro.titulo)
    assert multa_info is not None
    assert multa_info['valor'] == 2.5 * dias_atraso

def test_calcular_total_multas_cliente(multas_por_atraso, cliente, livro):
    dias_atraso_1 = 3
    dias_atraso_2 = 7

    multas_por_atraso.aplicar_multa(cliente, livro, dias_atraso_1)
    multas_por_atraso.aplicar_multa(cliente, livro, dias_atraso_2)

    total_multas = multas_por_atraso.calcular_total_multas_cliente(cliente)
    assert total_multas == 2.5 * dias_atraso_1 + 2.5 * dias_atraso_2

