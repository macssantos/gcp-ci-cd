import pytest

import json
# test_biblioteca.py
from biblioteca import Biblioteca, Livro, Cliente,Autor  # Certifique-se de que a classe Livro está definida em biblioteca

# Restante do seu código de teste...
  

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca de Teste")

@pytest.fixture
def livro():
    return Livro("Livro Teste", Autor("Autor Teste", "Localidade Teste"), "1234567890")


@pytest.fixture
def cliente():
    return Cliente("Cliente Teste", 25, "123.456.789-01")

def test_adicionar_livro(biblioteca):
    titulo = "Python 101"
    autor = Autor("John Doe", "Local")
    isbn = "123456789"
    
    novo_livro = biblioteca.adicionar_livro(titulo, autor, isbn)
    
    assert len(biblioteca.livros) == 1
    assert novo_livro.titulo == titulo
    assert novo_livro.autor == autor
    assert novo_livro.isbn == isbn   

    
def test_listar_livros(biblioteca, capsys):
    # Supondo que o método de listar_livros esteja implementado corretamente
    biblioteca.listar_livros()
    captured = capsys.readouterr()
    
    # Adapte conforme a saída real esperada
    assert "Lista de Livros" in captured.out
    assert "Python 101 - John Doe" in captured.out


# Adicione mais testes para outros métodos conforme necessário

def test_salvar_carregar_biblioteca(biblioteca, tmp_path):
    arquivo = tmp_path / "test_biblioteca.json"
    
    # Adiciona um livro à biblioteca
    biblioteca.adicionar_livro("Python 101", Autor("John Doe", "Local"), "123456789")
    
    # Salva a biblioteca em um arquivo JSON
    biblioteca.salvar_biblioteca(arquivo)
    
    # Cria uma nova instância de biblioteca e carrega a partir do arquivo
    nova_biblioteca = Biblioteca("Nova Biblioteca")
    nova_biblioteca.carregar_biblioteca(arquivo)
    
    # Verifica se o livro foi carregado corretamente
    assert len(nova_biblioteca.livros) == 1
    assert nova_biblioteca.livros[0].titulo == "Python 101"