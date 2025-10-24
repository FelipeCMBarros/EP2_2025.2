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
        