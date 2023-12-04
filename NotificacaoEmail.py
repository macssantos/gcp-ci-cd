# notificacao_email.py
class NotificacaoEmail:
    def __init__(self):
        self.subscritores = []

    def adicionar_subscritor(self, subscritor):
        """Adiciona um subscritor para receber notificações."""
        self.subscritores.append(subscritor)

    def remover_subscritor(self, subscritor):
        """Remove um subscritor da lista."""
        self.subscritores.remove(subscritor)

    def notificar_nova_adicao(self, livro):
        """Notifica subscritores sobre uma nova adição à biblioteca."""
        mensagem = f"Novo livro adicionado: {livro.titulo} de {livro.autor.nome}."
        self._enviar_notificacao(mensagem)

    def notificar_lembrete_devolucao(self, cliente, livro):
        """Notifica subscritores sobre um lembrete de devolução."""
        mensagem = f"Lembrete de devolução para {cliente.nome}: Por favor, devolva o livro '{livro.titulo}'."
        self._enviar_notificacao(mensagem)

    def _enviar_notificacao(self, mensagem):
        """Simula o envio de notificação por e-mail."""
        for subscritor in self.subscritores:
            subscritor.receber_notificacao(mensagem)
