# Import necessary classes and modules
from biblioteca import Biblioteca,Livro
from autor import Autor
import datetime

# Rest of your test code...

from EsportaçaoDEDados import ExportacaoDeDados
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