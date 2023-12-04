import datetime

class MultasPorAtraso:
    def __init__(self, taxa_multa_por_dia):
        self.taxa_multa_por_dia = taxa_multa_por_dia
        self.multas = {}

    def aplicar_multa(self, cliente, livro, dias_atraso):
        """Aplica uma multa por atraso ao cliente."""
        if cliente.nome not in self.multas:
            self.multas[cliente.nome] = {}

        valor_multa = self.taxa_multa_por_dia * dias_atraso
        self.multas[cliente.nome][livro.titulo] = {
            'valor': valor_multa,
            'data_aplicacao': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        print(f"Multada aplicada para {cliente.nome} pelo livro {livro.titulo} "
              f"no valor de R${valor_multa:.2f} por atraso de {dias_atraso} dias.")

    def obter_multas_cliente(self, cliente):
        """Obtém as multas aplicadas a um cliente."""
        return self.multas.get(cliente.nome, {})

    def calcular_total_multas_cliente(self, cliente):
        """Calcula o total das multas aplicadas a um cliente."""
        multas_cliente = self.obter_multas_cliente(cliente)
        return sum(multa['valor'] for multa in multas_cliente.values())
