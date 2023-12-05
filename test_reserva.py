# test_biblioteca.py
from biblioteca import Biblioteca, Livro, Cliente

def test_reservar_livro():
    # Configurando a biblioteca e adicionando um livro
    biblioteca = Biblioteca("Minha Biblioteca")
    
    # Corrigindo a criação da variável livro
    livro = Livro("Python para Iniciantes", "John Doe", "123456789")
    
    # Corrigindo a chamada da função adicionar_livro
    biblioteca.adicionar_livro(livro)

    # Configurando um cliente
    cliente = Cliente("Alice", 25, "123.456.789-01")
    biblioteca.adicionar_cliente(cliente)

    # Testando a reserva
    biblioteca.reservar_livro("123456789", cliente)
    
    # Verificando se o livro foi reservado corretamente
    assert biblioteca.livros[0].disponivel == False
    assert len(biblioteca.reservas) == 1

