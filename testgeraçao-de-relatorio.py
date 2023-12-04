import pytest
from biblioteca import Biblioteca
from cliente import Cliente
from GeracaoDeRelatorios import GeracaoDeRelatorios

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca Teste")

@pytest.fixture
def cliente():
    return Cliente("João", 25, "Estudante")

@pytest.fixture
def livro():
    return Livro("Aventuras na Biblioteca", "Autor Teste", "123456789")

@pytest.fixture
def gerador_relatorios(biblioteca):
    return GeracaoDeRelatorios(biblioteca)

def test_gerar_relatorio_livros_disponiveis(biblioteca, livro, gerador_relatorios):
    biblioteca.adicionar_livro(livro)
    relatorio = gerador_relatorios.gerar_relatorio_livros_disponiveis()
    assert livro.titulo in relatorio
    assert livro.autor in relatorio

def test_gerar_relatorio_clientes(biblioteca, cliente, gerador_relatorios):
    biblioteca.adicionar_cliente(cliente)
    relatorio = gerador_relatorios.gerar_relatorio_clientes()
    assert cliente.nome in relatorio
    assert str(cliente.idade) in relatorio
    assert cliente.cpf in relatorio

def test_gerar_relatorio_emprestimos_atrasados(biblioteca, livro, gerador_relatorios):
    biblioteca.adicionar_livro(livro)
    biblioteca.emprestar_livro(livro.isbn)
    livro.disponivel = False
    livro.data_devolucao = datetime.datetime.now() - datetime.timedelta(days=2)
    
    relatorio = gerador_relatorios.gerar_relatorio_emprestimos_atrasados(dias_atraso_limite=1)
    assert livro.titulo in relatorio
    assert livro.autor in relatorio
