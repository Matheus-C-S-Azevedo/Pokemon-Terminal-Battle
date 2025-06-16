from models import Habilidade
from models import Jogador
from models import Inimigo
from engine.batalha import iniciar_batalha

def main():
    # region: Habilidades
    # Habilidades do pikachu
    choque_do_trovao = Habilidade("Choque do Trovão", "eletrico", 20)
    investida = Habilidade("Investida", "normal", 10)
    # Habilidades do Charmander
    arranhao = Habilidade("Arranhão", "normal", 20)
    brasa = Habilidade("Brasa", "fogo", 10)
    # Habilidades do Bulba
    chicote_de_vinha = Habilidade("Chicote de Vinha", "planta", 14)
    po_venenoso = Habilidade("Pó Venenoso", "veneno", 12)
    # Habilidades do Squirtle
    pistola_agua = Habilidade("Pistola d’Água", "agua", 16)
    giro_rapido = Habilidade("Giro Rápido", "normal", 14)
    # endregion

    # region: Pokemons
    bulbasaur = Inimigo("Bulbasaur", "planta", 95, [chicote_de_vinha, po_venenoso])
    squirtle = Inimigo("Squirtle", "agua", 100, [pistola_agua, giro_rapido])
    pikachu = Jogador("Pikachu", "eletrico", 100, [choque_do_trovao, investida])
    charmander = Inimigo("Charmander", "fogo", 100, [arranhao, brasa])
    # endregion

    iniciar_batalha(pikachu, bulbasaur)

if __name__ == "__main__":
    main()
