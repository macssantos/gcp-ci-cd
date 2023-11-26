import json

class Autor:
    def __init__(self, nome, biografia):
        self.nome = nome
        self.biografia = biografia

    def __str__(self):
        return f"{self.nome} - {self.biografia}"