# exportacao_dados.py

import csv
import json

class ExportacaoDeDados:
    """Classe responsável pela exportação de dados da biblioteca."""

    @staticmethod
    def exportar_para_csv(biblioteca, arquivo_csv):
        """Exporta dados da biblioteca para um arquivo CSV."""
        with open(arquivo_csv, 'w', newline='') as csvfile:
            fieldnames = ['Titulo', 'Autor', 'ISBN', 'Disponivel']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for livro in biblioteca.livros:
                writer.writerow({
                    'Titulo': livro.titulo,
                    'Autor': livro.autor.nome,
                    'ISBN': livro.isbn,
                    'Disponivel': 'Sim' if livro.disponivel else 'Não'
                })

        print(f'Dados exportados para {arquivo_csv}.')

# Teste em pytest
def test_exportacao(tmp_path):
    # Criando uma instância da biblioteca para teste
    biblioteca_teste = Biblioteca("Biblioteca Teste")
    autor_teste = Autor("Autor Teste", "Localidade Teste")
    livro_teste = Livro("Livro Teste", autor_teste, "1234567890")
    biblioteca_teste.adicionar_livro(livro_teste)

    # Criando uma instância da classe ExportacaoDeDados
    exportador = ExportacaoDeDados()

    # Exportando para CSV
    arquivo_csv = tmp_path / "exportacao_teste.csv"
    exportador.exportar_para_csv(biblioteca_teste, arquivo_csv)

    # Verificando se o arquivo CSV foi criado
    assert arquivo_csv.is_file()
