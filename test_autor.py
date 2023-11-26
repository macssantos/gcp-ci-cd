import unittest
from autor import Autor  # Certifique-se de ajustar o import conforme necessário

class TestAutor(unittest.TestCase):

    def test_init(self):
        autor = Autor("John Doe", "Escritor renomado", "Nova York")
        self.assertEqual(autor.nome, "John Doe")
        self.assertEqual(autor.biografia, "Escritor renomado")
        self.assertEqual(autor.localidade, "Nova York")

    def test_str(self):
        autor = Autor("Jane Smith", "Autora best-seller", "Los Angeles")
        expected_str = "Jane Smith - Autora best-seller - Los Angeles"
        self.assertEqual(str(autor), expected_str)

if __name__ == '__main__':
    unittest.main()
