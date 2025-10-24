# Importando todas as funções
from funcoes import define_posicoes
from funcoes import preenche_frota
from funcoes import faz_jogada
from funcoes import posiciona_frota
from funcoes import afundados
from funcoes import posicao_valida


frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
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

print(frota)
