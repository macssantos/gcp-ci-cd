import pytest
from biblioteca import Biblioteca
from cliente import Cliente
from feedback import FeedbackLivro

@pytest.fixture
def feedback_livro():
    return FeedbackLivro()

def test_adicionar_feedback(feedback_livro):
    livro = Livro("Título do Livro", "Autor do Livro", "123456789")
    cliente = Cliente("Nome do Cliente", 25, "Estudante")

    feedback_livro.adicionar_feedback(livro.isbn, cliente.nome, 4, "Ótimo livro!")

    feedbacks = feedback_livro.obter_feedback(livro.isbn)
    assert len(feedbacks) == 1
    assert feedbacks[0]['cliente'] == cliente.nome
    assert feedbacks[0]['avaliacao'] == 4
    assert feedbacks[0]['comentario'] == "Ótimo livro!"

def test_media_avaliacao(feedback_livro):
    livro = Livro("Título do Livro", "Autor do Livro", "123456789")
    cliente1 = Cliente("Cliente 1", 30, "Professor")
    cliente2 = Cliente("Cliente 2", 22, "Estudante")

    feedback_livro.adicionar_feedback(livro.isbn, cliente1.nome, 5, "Maravilhoso!")
    feedback_livro.adicionar_feedback(livro.isbn, cliente2.nome, 3, "Bom livro.")

    assert feedback_livro.media_avaliacao(livro.isbn) == 4.0
