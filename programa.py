# Importando todas as funções
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida
from funcoes import monta_tabuleiros


frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
    }

# os valores são fixos
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tipos_navios = [
        ("porta-aviões", 4, 1),
        ("navio-tanque", 3, 2),
        ("contratorpedeiro", 2, 3),
        ("submarino", 1, 4)
    ]

for nome_navio, tamanho, quantidade in tipos_navios:
    i = 0
    while i < quantidade:
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if nome_navio != "submarino":
            orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
            orientacao = "vertical" if orientacao_input == 1 else "horizontal"
        else:
            orientacao = "horizontal"  #padrão dos submarinos

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            i += 1
        else:
            print("Esta posição não está válida!")

frota_jogador = frota

# Montagem dos tabuleiros
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota_jogador)  # frota_jogador foi criada nas etapas anteriores

# Controle de jogadas
posicoes_jogadas = []

# Loop principal do jogo
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # Solicita linha válida
    while True:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        if 0 <= linha <= 9:
            break
        else:
            print("Linha inválida!")

    # Solicita coluna válida
    while True:
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        if 0 <= coluna <= 9:
            break
        else:
            print("Coluna inválida!")

    # Verifica se a jogada já foi feita
    if [linha, coluna] in posicoes_jogadas:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue
    else:
        posicoes_jogadas.append([linha, coluna])

    # Atualiza o tabuleiro do oponente
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    # Verifica se afundou todos os navios do oponente
    total_afundados = afundados(frota_oponente, tabuleiro_oponente)
    if total_afundados == 10:  # total de embarcações (1+2+3+4 = 10)
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False