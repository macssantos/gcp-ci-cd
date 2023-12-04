class Biblioteca:
    # ... (código existente)

    def __init__(self, nome):
        # ... (código existente)
        self.reservas = []  # Adicionando uma lista para rastrear reservas

    def reservar_livro(self, isbn, cliente):
        """Reserva um livro da biblioteca para um cliente."""
        for livro in self.livros:
            if livro.isbn == isbn and livro.disponivel:
                livro.disponivel = False
                self.reservas.append({'livro': livro, 'cliente': cliente})
                print(f"{livro.titulo} reservado para {cliente.nome} com sucesso.")
                return
        print("Livro não encontrado ou indisponível para reserva.")

    def listar_reservas(self):
        """Lista todas as reservas na biblioteca."""
        for reserva in self.reservas:
            livro = reserva['livro']
            cliente = reserva['cliente']
            print(f"{livro.titulo} reservado para {cliente.nome}")

# Exemplo de uso:
# biblioteca = Biblioteca("Minha Biblioteca")
# biblioteca.reservar_livro("123456789", cliente)  # Substitua "123456789" pelo ISBN desejado
# biblioteca.listar_reservas()
