from models.personagem import Personagem
import random

class Inimigo(Personagem):
    def escolher_ataque(self):
        return random.choice(self.habilidades)
