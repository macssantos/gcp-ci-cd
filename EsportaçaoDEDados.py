# exportacao_dados.py
import csv

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