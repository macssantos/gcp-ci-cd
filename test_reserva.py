

import pytest
from biblioteca import Biblioteca, Livro, Cliente, Autor,reserva


@pytest.fixture
def biblioteca():
    return Biblioteca("Minha Biblioteca")

@pytest.fixture
def cliente():
    return Cliente("Cliente Teste", 25, "123.456.789-01")

@pytest.fixture
def livro():
    autor = Autor("Autor Teste", "Localidade Teste")
    return Livro("Livro Teste", autor, "1234567890")

def test_reservar_livro(biblioteca: Biblioteca, cliente: Cliente, livro: Livro):
    reserva = reserva("Minhas Reservas")
    biblioteca.adicionar_livro(livro)
    cliente.entrar_na_biblioteca(biblioteca)
    
    reserva.reservar_livro(livro.isbn, cliente)

    assert len(reserva.reservas) == 1
    assert not livro.disponivel

def test_listar_reservas(biblioteca: Biblioteca, cliente: Cliente, livro: Livro, capsys: pytest.CaptureFixture[str]):
    reserva = reserva("Minhas Reservas")
    biblioteca.adicionar_livro(livro)
    cliente.entrar_na_biblioteca(biblioteca)
    reserva.reservar_livro(livro.isbn, cliente)

    reserva.listar_reservas()
    captured = capsys.readouterr()

    assert f"{livro.titulo} reservado para {cliente.nome}" in captured.out
