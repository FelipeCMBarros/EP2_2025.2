# Enunciados como comentarios pra ficar mais facil de lembrar o que cada função faz

# Função chamada define_posicoes que recebe como argumentos uma linha, coluna, orientacao e um tamanho. A função retorna uma lista com as posições que o navio irá ocupar no grid.

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

# Função chamada preenche_frota que recebe como argumentos o dicionário com as informações da frota, uma string com o nome do navio, a linha e a coluna para posicionar o navio, a orientacao que o navio será posicionado e o 'tamanho' do navio, retornando o dicionário de frota atualizado com as informações do novo navio

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = [posicoes]
    else:
        frota[nome_navio].append(posicoes)
    return frota

# Função chamada faz_jogada que recebe o tabuleiro, linha e coluna e retorna o tabuleiro com os valores atualizadosfunção chamada faz_jogada que recebe o tabuleiro, linha e coluna e retorna o tabuleiro com os valores atualizados

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

# Função deve se chamar posiciona_frota e recebe como argumento um dicionário com as informações dos navios e retorna uma lista de listas representando o tabuleiro com os navios posicionados

def posiciona_frota(frota):
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

# Função afundados que recebe como argumentos um dicionário com as informações das embarcações e o tabuleiro com o estado atual da partida. A função retorna um número representando a quantidade de navios já afundados

def afundados(frota, tabuleiro):
    afundados = 0
    for tipo in frota:
        lista_navios = frota[tipo]
        i = 0
        while i < len(lista_navios):
            navio = lista_navios[i]
            j = 0
            afundado = True
            while j < len(navio):
                posicao = navio[j]
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                j += 1
            if afundado:
                afundados += 1
            i += 1
    return afundados

# Função chamada posicao_valida que recebe como argumentos um dicionário com as informações dos navios, a linha e a coluna em que o jogador deseja posicionar um navio, a orientacao e o tamanho do navio. A função retorna True se as posições do navio a ser posicionado ocuparem somente posições vazias ou posições válidas. Caso contrário, a função deve retornar False.

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for posicao in posicoes_novo_navio:
        l, c = posicao
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False  
    
    ocupadas = []
    for tipo in frota:
        for navio in frota[tipo]:
            for posicao in navio:
                ocupadas.append(posicao)
    
    for posicao in posicoes_novo_navio:
        if posicao in ocupadas:
            return False  
    
    return True