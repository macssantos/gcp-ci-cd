# test_notificacao_email.py
from NotificacaoEmail import NotificacaoEmail

class SubscritorTeste:
    def __init__(self):
        self.notificacoes_recebidas = []

    def receber_notificacao(self, mensagem):
        self.notificacoes_recebidas.append(mensagem)

def test_notificacao_email():
    # Configurando a notificação por e-mail
    notificacao_email = NotificacaoEmail()

    # Configurando subscritores de teste
    subscritor1 = SubscritorTeste()
    subscritor2 = SubscritorTeste()

    # Adicionando subscritores
    notificacao_email.adicionar_subscritor(subscritor1)
    notificacao_email.adicionar_subscritor(subscritor2)

    # Notificando sobre nova adição
    notificacao_email.notificar_nova_adicao({"titulo": "Novo Livro", "autor": {"nome": "Autor"}})
    assert len(subscritor1.notificacoes_recebidas) == 1
    assert len(subscritor2.notificacoes_recebidas) == 1

    # Notificando sobre lembrete de devolução
    notificacao_email.notificar_lembrete_devolucao({"nome": "Cliente"}, {"titulo": "Livro", "autor": {"nome": "Autor"}})
    assert len(subscritor1.notificacoes_recebidas) == 2
    assert len(subscritor2.notificacoes_recebidas) == 2
