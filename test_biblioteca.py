import pytest

import json
# test_biblioteca.py
from biblioteca import Biblioteca, Livro, Cliente,Autor  # Certifique-se de que a classe Livro está definida em biblioteca

# Restante do seu código de teste...
  

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca de Teste")

# @pytest.fixture
# def livro():
#     return Livro("Livro Teste", Autor("Autor Teste", "Localidade Teste"), "1234567890")

@pytest.fixture
def cliente():
    return Cliente("Cliente Teste", 25, "123.456.789-01")

def test_adicionar_livro(biblioteca, livro):
    # Dados do livro
    titulo = "Título do Livro"
    autor = "Autor do Livro"
    isbn = "123456789"

    # Adiciona o livro à biblioteca
    novo_livro = biblioteca.adicionar_livro(titulo, autor, isbn)

    # Verificações
    assert len(biblioteca.livros) == 1
    assert novo_livro.titulo == titulo
    assert novo_livro.autor == autor
    assert novo_livro.isbn == isbn
    assert novo_livro.disponivel is True  # Considerando que o padrão seja disponível
    assert novo_livro.categoria is None  # Considerando que o padrão seja None

def test_listar_livros(biblioteca, livro, capsys):
    biblioteca.adicionar_livro(livro)
    biblioteca.listar_livros()
    captured = capsys.readouterr()
    assert f"{livro.titulo} - {livro.autor.nome}" in captured.out

# Adicione mais testes para outros métodos conforme necessário

def test_salvar_carregar_biblioteca(biblioteca, livro, cliente, tmp_path):
    arquivo = tmp_path / "test_biblioteca.json"

    biblioteca.adicionar_livro(livro)
    biblioteca.adicionar_cliente(cliente)
    biblioteca.salvar_biblioteca(arquivo)

    nova_biblioteca = Biblioteca("Nova Biblioteca")
    nova_biblioteca.carregar_biblioteca(arquivo)

    assert nova_biblioteca.nome == biblioteca.nome
    assert len(nova_biblioteca.livros) == 1
    assert nova_biblioteca.livros[0].titulo == livro.titulo
    assert len(nova_biblioteca.clientes) == 1
    assert nova_biblioteca.clientes[0].nome == cliente.nome