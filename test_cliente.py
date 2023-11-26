import unittest
from biblioteca import Biblioteca  # Certifique-se de importar a classe Biblioteca ou ajustar conforme necessário
from cliente import Cliente  # Certifique-se de importar a classe Cliente ou ajustar conforme necessário

class TestCliente(unittest.TestCase):

    def setUp(self):
        # Configuração inicial para os testes
        self.biblioteca = Biblioteca("Biblioteca Central")
        self.cliente = Cliente("João", 25, "Estudante")

    def test_entrar_na_biblioteca(self):
        self.cliente.entrar_na_biblioteca(self.biblioteca)
        self.assertEqual(self.cliente.biblioteca, self.biblioteca)
        self.assertIn(self.cliente, self.biblioteca.visitantes)
        # Adicione mais verificações conforme necessário

    def test_procurar_livro_por_titulo(self):
        livro1 = self.biblioteca.adicionar_livro("Aprendendo Python", "John Smith", "123456789")
        self.cliente.entrar_na_biblioteca(self.biblioteca)

        # Verifique se o cliente encontra o livro
        with unittest.mock.patch('builtins.print') as mock_print:
            self.cliente.procurar_livro_por_titulo("Aprendendo Python")
            mock_print.assert_called_with(f"João encontrou o livro: {livro1.titulo} - {livro1.autor}")

        # Verifique se o cliente não encontra um livro inexistente
        with unittest.mock.patch('builtins.print') as mock_print:
            self.cliente.procurar_livro_por_titulo("Livro Inexistente")
            mock_print.assert_called_with("João não encontrou o livro com o título: Livro Inexistente")

    def test_pegar_livro_emprestado(self):
        livro2 = self.biblioteca.adicionar_livro("Python Avançado", "Jane Doe", "987654321")
        self.cliente.entrar_na_biblioteca(self.biblioteca)

        # Verifique se o cliente pode pegar emprestado um livro existente
        self.cliente.pegar_livro_emprestado("987654321")
        self.assertIn(livro2, self.cliente.biblioteca.livros_emprestados)
        # Adicione mais verificações conforme necessário

    def test_devolver_livro(self):
        livro3 = self.biblioteca.adicionar_livro("Data Science", "Alice Johnson", "555555555")
        self.cliente.entrar_na_biblioteca(self.biblioteca)
        self.cliente.pegar_livro_emprestado("555555555")

        # Verifique se o cliente pode devolver um livro emprestado
        self.cliente.devolver_livro("555555555")
        self.assertNotIn(livro3, self.cliente.biblioteca.livros_emprestados)
        # Adicione mais verificações conforme necessário

    def tearDown(self):
        # Limpeza após os testes, se necessário
        pass

if __name__ == '__main__':
    unittest.main()
