from models.personagem import Personagem

class Jogador(Personagem):
    def escolher_ataque(self):
        print("Escolha sua habilidade:")
        for i, hab in enumerate(self.habilidades):
            print(f"{i+1} - {hab.nome} ({hab.dano_base} de dano)")
        escolha = int(input("Número da habilidade: ")) - 1
        return self.habilidades[escolha]


