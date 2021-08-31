# Similaridade máxima:

# Programa que recebe duas matrizes: uma grande e uma pequena.

# O propósito do programa é avaliar a similaridade máxima que a matriz pequena pode ter com alguma parte grande e retornar a posição do canto superior esquerdo deste trecho, além da similaridade em %.

def ler_entrada():
    """
    Lê a entrada do usuário (o tamanho da primeira matriz e a matriz em si, o tamanho da segunda matriz e a matriz em si)
    
    Recebe: nada.
    Devolve: as duas matrizes e seus respectivos tamanhos.
    """
    matriz_maior = []
    matriz_menor = []
    n = int(input())

    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz_maior.append(linha)

    m = int(input())

    for _ in range(m):
        linha = list(map(int, input().split()))
        matriz_menor.append(linha)

    return matriz_maior, matriz_menor, n, m

def conferir_similaridade(matriz_maior, matriz_menor, tamanho_matriz_maior, tamanho_matriz_menor):
    """
    Confere a similiaridade maxima possível entre a matriz maior e a matriz menor. 
    
    Recebe: a matriz maior, a matriz menor, o tamanho da matriz maior e o tamanho da matriz menor.
    Devolve: a posição de maior similaridade e a porcentagem dessa similaridade.
    """
    similaridade_maxima = 0
    pos_x, pos_y = 0, 0
    for x in range(tamanho_matriz_maior-tamanho_matriz_menor+1):
        for y in range(tamanho_matriz_maior-tamanho_matriz_menor+1):
            soma = 0
            for i in range(tamanho_matriz_menor):
                for j in range(tamanho_matriz_menor):
                    if matriz_maior[i+x][j+y] == matriz_menor[i][j]:
                        soma += 1

            similaridade = (soma/tamanho_matriz_menor**2)*100
            if similaridade > similaridade_maxima:
                similaridade_maxima = similaridade
                pos_x, pos_y = x, y
                
    lista_posicoes = [pos_x, pos_y]

    return lista_posicoes, similaridade_maxima

def main():
    quadrado_maior, quadrado_menor, n, m = ler_entrada()

    posicao, similaridade_maxima = conferir_similaridade(quadrado_maior, quadrado_menor, n, m)

    x, y = posicao[0], posicao[1]

    print(f'Posição: ({x},{y})')
    print(f'Similaridade máxima: {similaridade_maxima:.2f}%')

main()
