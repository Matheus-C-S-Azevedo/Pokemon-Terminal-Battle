from models.habilidade import Habilidade

class Personagem:
    def __init__(self, nome, tipo, vida, habilidades):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.habilidades = habilidades

    def atacar(self):
        return self.habilidades[0]  # padrão simples

    def receber_dano(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0
