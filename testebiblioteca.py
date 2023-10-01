import pytest
import json
from biblioteca import Livro, Biblioteca

# Função de fixture para criar uma instância de Biblioteca para testes
@pytest.fixture
def biblioteca_teste():
    biblioteca = Biblioteca("Biblioteca de Teste")
    livro1 = Livro("Aventuras de Python", "Guido van Rossum", "123456")
    livro2 = Livro("Introdução ao Machine Learning", "Andrew Ng", "789012")
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    return biblioteca

# Teste para garantir que a biblioteca seja inicializada corretamente
def test_inicializacao_biblioteca(biblioteca_teste):
    assert biblioteca_teste.nome == "Biblioteca de Teste"
    assert len(biblioteca_teste.livros) == 2

# Teste para verificar se um livro é emprestado corretamente
def test_emprestar_livro(biblioteca_teste):
    biblioteca_teste.emprestar_livro("123456")
    assert not biblioteca_teste.livros[0].disponivel

# Teste para verificar se um livro é devolvido corretamente
def test_devolver_livro(biblioteca_teste):
    biblioteca_teste.emprestar_livro("123456")
    biblioteca_teste.devolver_livro("123456")
    assert biblioteca_teste.livros[0].disponivel

# Teste para verificar se a biblioteca é salva e carregada corretamente
def test_salvar_carregar_biblioteca(biblioteca_teste):
    arquivo = "test_biblioteca.json"
    biblioteca_teste.salvar_biblioteca(arquivo)

    # Cria uma nova instância de Biblioteca
    nova_biblioteca = Biblioteca("Nova Biblioteca")
    nova_biblioteca.carregar_biblioteca(arquivo)

    # Verifica se os dados foram carregados corretamente
    assert nova_biblioteca.nome == "Biblioteca de Teste"
    assert len(nova_biblioteca.livros) == 2
    assert nova_biblioteca.livros[0].titulo == "Aventuras de Python"

    # Limpa o arquivo de teste após os testes
    import os
    os.remove(arquivo)

if __name__ == "__main__":
    pytest.main()
