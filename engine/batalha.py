from colorama import Fore, Style
import os, time

FRAQUEZAS = {
    "fogo": "agua",
    "agua": "eletrico",
    "eletrico": "veneno",
    "veneno": "agua",
    "planta": "fogo",
    "normal": None
}

def iniciar_batalha(jogador, inimigo):
    turno = 1
    while jogador.esta_vivo() and inimigo.esta_vivo():
        limpar_tela()
        print(Fore.CYAN + f"=== Turno {turno} ===" + Style.RESET_ALL)
        print(f"{Fore.BLUE}{jogador.nome} HP: {jogador.vida}{Style.RESET_ALL}")
        print(f"{Fore.RED}{inimigo.nome} HP: {inimigo.vida}{Style.RESET_ALL}")

        # ====== Ataque do jogador ======
        habilidade_jogador = jogador.escolher_ataque()
        dano, erro = habilidade_jogador.usar()
        if erro:
            print(Fore.YELLOW + f"{jogador.nome} tentou usar {habilidade_jogador.nome}, mas errou o ataque!" + Style.RESET_ALL)
        else:
            efetivo = habilidade_jogador.tipo == FRAQUEZAS.get(inimigo.tipo)
            if efetivo:
                dano = int(dano * 1.5)
            inimigo.receber_dano(dano)
            
            print(Fore.YELLOW + f"{jogador.nome} usou {habilidade_jogador.nome} e causou {dano} de dano!" + Style.RESET_ALL)
            if efetivo:
                print(Fore.LIGHTYELLOW_EX + "É super efetivo!" + Style.RESET_ALL)
        time.sleep(1)

        if not inimigo.esta_vivo():
            print(Fore.GREEN + f"{inimigo.nome} foi derrotado!" + Style.RESET_ALL)
            break
        
        # ====== Ataque do inimigo ======
        habilidade_inimigo = inimigo.escolher_ataque()
        dano, erro = habilidade_inimigo.usar()
        if erro:
            print(Fore.RED + f"{inimigo.nome} tentou usar {habilidade_inimigo.nome}, mas errou o ataque!" + Style.RESET_ALL)
        else:
            efetivo = habilidade_inimigo.tipo == FRAQUEZAS.get(jogador.tipo)
            if efetivo:
                dano = int(dano * 1.5)
            jogador.receber_dano(dano)

            print(Fore.RED + f"{inimigo.nome} usou {habilidade_inimigo.nome} e causou {dano} de dano!" + Style.RESET_ALL)
            if efetivo:
                print(Fore.LIGHTRED_EX + "É super efetivo!" + Style.RESET_ALL)

        time.sleep(1.5)

        turno += 1

    print("\n" + Fore.MAGENTA + "Fim da batalha." + Style.RESET_ALL)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
