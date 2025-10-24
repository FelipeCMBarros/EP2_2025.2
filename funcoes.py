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

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posciona_frota(frota):
    tabuleiro = []
    i = 0
    while i<10:
        linha = []
        j = 0
        while j<10:
            linha.append(0)
            j += 1
        tabuleiro.append(linha)
        i+=1
    for tipo in frota:
        lista_navios = frota[tipo]
        k = 0
        while k < len(lista_navios):
            navio = lista_navios[k]
            m = 0
            while m < len(navio):
                posicao = navio[m]
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
                m += 1  
            k += 1
    return tabuleiro