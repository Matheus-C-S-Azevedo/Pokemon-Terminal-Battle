import random

class Habilidade:
    def __init__(self, nome, tipo, dano_base):
        self.nome = nome
        self.tipo = tipo
        self.dano_base = dano_base

    def usar(self):
        if random.random() < 0.1:  # 10% de chance de errar
            return 0, True
        variacao = random.randint(-5, 5)
        return self.dano_base + variacao, False
