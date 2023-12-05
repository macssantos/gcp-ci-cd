

from biblioteca import Biblioteca, Livro, Cliente
from reserva import reserva
import pytest

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca de Teste")

@pytest.fixture
def cliente():
    return Cliente("Cliente Teste", 25, "Estudante")

def test_reservar_livro(biblioteca, cliente, capsys):
    livro_disponivel = Livro("Python 101", "John Doe", "123456789")
    livro_indisponivel = Livro("Python Avançado", "Jane Doe", "987654321", disponivel=False)

    biblioteca.adicionar_livro(livro_disponivel)
    biblioteca.adicionar_livro(livro_indisponivel)

    cliente.entrar_na_biblioteca(biblioteca)

    # Testando a reserva de um livro disponível
    reserva = reserva(biblioteca)
    reserva.reservar_livro("123456789", cliente)
    captured = capsys.readouterr()
    assert f"{livro_disponivel.titulo} reservado para {cliente.nome} com sucesso." in captured.out

    # Testando a reserva de um livro indisponível
    reserva.reservar_livro("987654321", cliente)
    captured = capsys.readouterr()
    assert "Livro não encontrado ou indisponível para reserva." in captured.out

def test_listar_reservas(biblioteca, cliente, capsys):
    livro_disponivel = Livro("Python 101", "John Doe", "123456789")
    livro_indisponivel = Livro("Python Avançado", "Jane Doe", "987654321", disponivel=False)

    biblioteca.adicionar_livro(livro_disponivel)
    biblioteca.adicionar_livro(livro_indisponivel)

    cliente.entrar_na_biblioteca(biblioteca)

    # Reservando um livro disponível
    reserva = reserva(biblioteca)
    reserva.reservar_livro("123456789", cliente)

    # Reservando um livro indisponível
    reserva.reservar_livro("987654321", cliente)

    # Listando as reservas
    reserva.listar_reservas()
    captured = capsys.readouterr()
    assert f"{livro_disponivel.titulo} reservado para {cliente.nome}" in captured.out
    assert "Livro Avançado reservado para Cliente Teste" not in captured.out



