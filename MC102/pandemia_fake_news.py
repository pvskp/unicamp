# Pandemia de fake news:

# Programa que recebe uma matriz composta por numeros, 'X' e '#' e uma posição, que representa
# uma pessoa (paciente 0) infectada por 'fake news'. Cada número na matriz representa uma pessoa, 
# e este número, por sua vez, representa o alcance desta pessoa para a propagação de fake news. Ou seja, 
# representa quantas pessoas ela consegue infectar nas 4 direções. Ao ser infectada. Seu número é substituído por um
# 'X'. O '#' representa um bloqueio pelo qual as fake news não conseguem passar. 

# Assim, o programa utiliza de uma chamada recursiva para devolver ao usuário uma matriz com
# as mesmas dimensões da matriz recebida, mas que mostra o mapa após as 'infecções'.

def juntar_caracteres(rede):
    for linha in rede:
        print(''.join(linha))

def verificar(rede, inicio):
    x = inicio[0]
    y = inicio[1]

    alcance = 0

    if rede[x][y].isdigit():
        alcance = int(rede[x][y])
        rede[x][y] = 'X'  

    elif rede[x][y] == '#':
        return

    for j in range(y, y+alcance+1):
        if 0 <= j < len(rede[0]):
            if (rede[x][j]).isdigit():
                verificar(rede,[x, j])
            elif (rede[x][j]) == '#':
                break

    for j in range(y, y-alcance-1,-1):
        if 0 <= j < len(rede[0]):
            if (rede[x][j]).isdigit():
                verificar(rede,[x, j])
            elif (rede[x][j]) == '#':
                break

    for i in range(x, x+alcance+1):
        if 0 <= i < len(rede):
            if (rede[i][y]).isdigit():
                verificar(rede,[i, y])
            elif rede[i][y] == '#':
                break

    for i in range(x, x-alcance-1,-1):
        if 0 <= i < len(rede):
            if (rede[i][y]).isdigit():
                verificar(rede,[i, y])
            elif rede[i][y] == '#':
                break

def entrada():
    n = int(input()) # qtd de linhas da matriz
    matriz = []
    for _ in range(n):
        l = list(input())
        matriz.append(l)

    pos = [int(x) for x in input().split()]

    return matriz, pos

def main():
    rede, pos = entrada()
    verificar(rede, pos)
    juntar_caracteres(rede)

main()