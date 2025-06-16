# 🔥 Pokémon Battle Terminal Game (Python OOP)

Um projeto educacional de jogo de batalha por turnos inspirado em Pokémon, implementado em Python com foco em **Programação Orientada a Objetos (POO)**. Feito para rodar diretamente no terminal com saída colorida e dinâmica!

---

## 🎯 Objetivo

Demonstrar o uso prático dos principais conceitos de POO:
- Herança
- Polimorfismo
- Encapsulamento
- Composição
- Modularização de código

---

## 📁 Estrutura do Projeto

```
trabalho_OOP/
├── engine/
│   └── batalha.py         # Lógica da batalha entre os personagens
├── models/
│   ├── habilidade.py      # Define as habilidades (ataques)
│   ├── personagem.py      # Classe base para jogadores e inimigos
│   ├── jogador.py         # Herda de Personagem, com escolha de ataque interativa
│   ├── inimigo.py         # Herda de Personagem, escolhe ataques aleatoriamente
│   └── __init__.py        # Importações organizadas
├── main.py                # Inicializa os personagens e executa a batalha
```

---

## 🧩 Classes e Componentes

### `Habilidade`
```python
Habilidade(nome: str, tipo: str, dano_base: int)
```
Representa uma habilidade de ataque. Possui:
- `usar()`: retorna um dano aleatório com 10% de chance de erro.

---

### `Personagem` (Classe Base)
```python
Personagem(nome, tipo, vida, habilidades)
```
Abstração comum para jogadores e inimigos. Possui métodos:
- `receber_dano(dano)`
- `esta_vivo()`

---

### `Jogador` (Herda de Personagem)
Permite ao usuário **escolher a habilidade** no terminal.

Método:
- `escolher_ataque()`: exibe habilidades disponíveis e lê a escolha do usuário.

---

### `Inimigo` (Herda de Personagem)
Ataca de forma aleatória.

Método:
- `escolher_ataque()`: retorna uma habilidade aleatória.

---

### `batalha.py`
Contém a função:
```python
iniciar_batalha(jogador, inimigo)
```
Simula o turno de cada personagem, mostrando:
- HP atual
- Ações (ataques, erros, dano causado)
- Mensagens como “É super efetivo!”

Usa uma **tabela de fraquezas** para aplicar bônus de dano (x1.5) se o tipo do ataque for eficaz contra o tipo do oponente.

---

## 💡 Exemplo de Execução

```
python3 main.py
```

Saída:

```
=== Turno 1 ===
Pikachu HP: 100
Charmander HP: 90

1 - Choque do Trovão (20 de dano)
2 - Investida (10 de dano)
Número da habilidade: 1

Pikachu usou Choque do Trovão e causou 26 de dano!
É super efetivo!

Charmander tentou usar Brasa, mas errou o ataque!
```

---

## 🧪 Tipos e Fraquezas

```python
FRAQUEZAS = {
    "fogo": "agua",
    "agua": "eletrico",
    "eletrico": "terra",
    "terra": "agua",
    "planta": "fogo",
    "normal": None
}
```

Se o tipo do ataque for eficaz contra o tipo do inimigo, o dano é multiplicado por 1.5.

---

## 📌 Tecnologias Usadas

- Python 3.10+
- [colorama](https://pypi.org/project/colorama/) para terminal colorido
- Orientação a Objetos aplicada na prática

---

## 📚 Possíveis Expansões

- Interface gráfica (Tkinter, PyGame)
- Tipos mais complexos (gelo, veneno, psíquico)
- Efeitos de status (paralisia, veneno, etc.)
- Vários rounds ou torneios
- Leitura de personagens e habilidades a partir de arquivos `.json`

---

## 👨‍🏫 Autoria

Projeto desenvolvido para avaliação de conceitos de Programação Orientada a Objetos.

> Equipe: [Nomes dos integrantes]  
> Disciplina: Programação Orientada a Objetos  
> Professor: [Nome do professor]  
> Instituição: [Nome da instituição]