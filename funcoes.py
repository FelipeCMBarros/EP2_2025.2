def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes = []
    if orientacao == 'vertical':
        i = 0
        while i < tamanho:
            posicoes.append([linha + i, coluna])
            i += 1
    else:
        i = 0
        while i < tamanho:
            posicoes.append([linha, coluna + i])
            i += 1
    return posicoes
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
    return frota

        