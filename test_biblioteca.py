import pytest
import autor
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
   # Teste para verificar se a biblioteca é filtrada corretamente 

def test_buscar_livros_por_localidade(biblioteca_teste):

    biblioteca = Biblioteca("Biblioteca Municipal")

    livro_1 = Livro("O Pequeno Príncipe", autor("Antoine de Saint-Exupéry", "Biografia", "França"),False,100,True)
    livro_2 = Livro("Dom Quixote", autor("Miguel de Cervantes", "Biografia", "Espanha"),False,150,True)
    livro_3 = Livro("Harry Potter e a Pedra Filosofal", autor("J.K. Rowling", "Biografia", "Reino Unido"),False,200,True)

    biblioteca.adicionar_livro(livro_1)
    biblioteca.adicionar_livro(livro_2)
    biblioteca.adicionar_livro(livro_3)

    livros_franceses = biblioteca.buscar_livros_por_localidade("França")
    biblioteca_teste.assertEqual(len(livros_franceses), 1)
    biblioteca_teste.assertEqual(livros_franceses[0].titulo, "Dom Quixote")

    livros_espanhóis = biblioteca.buscar_livros_por_localidade("Espanha")
    biblioteca_teste.assertEqual(len(livros_espanhóis), 1)
    biblioteca_teste.assertEqual(livros_espanhóis[0].titulo, "Dom Quixote")

    livros_britânicos = biblioteca.buscar_livros_por_localidade("Reino Unido")
    biblioteca_teste.assertEqual(len(livros_britânicos), 1)
    biblioteca_teste.assertEqual(livros_britânicos[0].titulo, "Harry Potter e a Pedra Filosofal")