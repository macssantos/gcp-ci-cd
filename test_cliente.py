import unittest
import pytest
from cliente import Cliente
from biblioteca import Biblioteca, Livro, Autor

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca de Teste")

@pytest.fixture
def cliente():
    return Cliente("Cliente Teste", 25, "123.456.789-01")

def test_entrar_na_biblioteca(cliente, biblioteca, capsys):
    cliente.entrar_na_biblioteca(biblioteca)
    captured = capsys.readouterr()
    assert f"{cliente.nome} entrou na biblioteca {biblioteca.nome}." in captured.out

def test_procurar_livro_por_titulo_com_biblioteca(cliente, biblioteca, capsys):
    # Adiciona um livro à biblioteca
    livro = Livro("Python 101", Autor("John Doe", ""), "123456789")
    biblioteca.adicionar_livro(livro)

    # Testando a busca por um livro existente
    cliente.procurar_livro_por_titulo("Python 101")
    captured = capsys.readouterr()
    assert f"{cliente.nome} encontrou o livro: Python 101 - John Doe" in captured.out

    # Testando a busca por um livro inexistente
    cliente.procurar_livro_por_titulo("Python Avançado")
    captured = capsys.readouterr()
    assert f"{cliente.nome} não encontrou o livro com o título: Python Avançado" in captured.out

def test_pegar_livro_emprestado_com_biblioteca(cliente, biblioteca, capsys):
    # Adiciona um livro disponível à biblioteca
    livro_disponivel = Livro("Python 101", Autor("John Doe", ""), "123456789")
    biblioteca.adicionar_livro(livro_disponivel)

    # Adiciona um livro indisponível à biblioteca
    livro_indisponivel = Livro("Python Avançado", Autor("Jane Doe", ""), "987654321", disponivel=False)
    biblioteca.adicionar_livro(livro_indisponivel)

    # Testando o empréstimo de um livro disponível
    cliente.pegar_livro_emprestado("123456789")
    captured = capsys.readouterr()
    assert f"{cliente.nome} pegou emprestado o livro com o ISBN: 123456789" in captured.out

    # Testando o empréstimo de um livro indisponível
    cliente.pegar_livro_emprestado("987654321")
    captured = capsys.readouterr()
    assert f"{cliente.nome} não conseguiu pegar emprestado o livro com o ISBN: 987654321" in captured.out

def test_devolver_livro_com_biblioteca(cliente, biblioteca, capsys):
    # Adiciona um livro emprestado à biblioteca
    livro_emprestado = Livro("Python 101", Autor("John Doe", ""), "123456789")
    biblioteca.adicionar_livro(livro_emprestado)
    biblioteca.emprestar_livro("123456789")

    # Adiciona um livro não emprestado à biblioteca
    livro_nao_emprestado = Livro("Python Avançado", Autor("Jane Doe", ""), "987654321")
    biblioteca.adicionar_livro(livro_nao_emprestado)

    # Testando a devolução de um livro emprestado
    cliente.devolver_livro("123456789")
    captured = capsys.readouterr()
    assert f"{cliente.nome} devolveu o livro com o ISBN: 123456789" in captured.out

    # Testando a devolução de um livro não emprestado
    cliente.devolver_livro("987654321")
    captured = capsys.readouterr()
    assert f"{cliente.nome} tentou devolver um livro não emprestado com o ISBN: 987654321" in captured.out


