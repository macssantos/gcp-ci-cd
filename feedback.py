class FeedbackLivro:
    def __init__(self):
        self.feedback = {}

    def adicionar_feedback(self, isbn, cliente, avaliacao, comentario):
        """Adiciona feedback de um cliente para um livro."""
        if isbn not in self.feedback:
            self.feedback[isbn] = []

        self.feedback[isbn].append({
            'cliente': cliente,
            'avaliacao': avaliacao,
            'comentario': comentario
        })

    def obter_feedback(self, isbn):
        """Obtém todos os feedbacks de um livro."""
        return self.feedback.get(isbn, [])

    def media_avaliacao(self, isbn):
        """Calcula a média de avaliações para um livro."""
        feedbacks = self.obter_feedback(isbn)
        if not feedbacks:
            return None

        total_avaliacoes = sum(feedback['avaliacao'] for feedback in feedbacks)
        media = total_avaliacoes / len(feedbacks)
        return media
