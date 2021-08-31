
# Tratamento de imagem:

# Programa que recebe uma matriz que representa uma imagem no formato PBM e, em seguida,
# pergunta qual a operação desejada para manipulação desta imagem.

# Neste programa, foram implementadas 6 formas de tratamento:

# flip horizontal: inverte a imagem no eixo horizontal.

# flip vertial: inverte a imagem no eixo vertical.

# shift horizontal: locomove os pixels da imagem (em x pixels, a ser determinado pelo usuário)
#     no eixo horizontal.

# shift vertical: locomove os pixels da imagem (em x pixels, a ser determinado pelo usuário)
#     no eixo vertical.

# crop: recorta a imagem com base em duas coordenadas (canto superior esquerdo e canto inferior direito).

# shrink: diminui a quantidade de pixels da imagem, divindo-a em pequenas matrizes 2x2 e formando uma nova matriz
#     apenas com o maximo dessas matrizes menores


def flip_horizontal(imagem_original): #OK!
    imagem_flipada = []

    for i in imagem_original:
        linha_flipada = []
        for j in reversed(i):
            linha_flipada.append(j)
        imagem_flipada.append(linha_flipada)
    
    return imagem_flipada

def flip_vertical(imagem_original): #OK!
    imagem_flipada = []

    for linha in reversed(imagem_original):
        imagem_flipada.append(linha)
    
    return imagem_flipada

def shift_vertical(imagem_original, x): #OK!
    imagem_shift = []
    for i in range(len(imagem_original)):
        imagem_shift.append(imagem_original[i-x])

    return imagem_shift

def shift_horizontal(imagem_original, x): #OK!
    imagem_shift = []
    for i in range(len(imagem_original)):
        linha_shift = []
        for j in range(len(imagem_original[0])):
            linha_shift.append(imagem_original[i][j-x])
        imagem_shift.append(linha_shift)

    return imagem_shift

def crop(imagem_original, x1, y1, x2, y2): #OK!
    imagem_crop = []
    for i in range(len(imagem_original)):
        if x1-1 <= i <= x2-1:
            linha_cropada = []
            for j in range(len(imagem_original[0])):
                if y1-1 <= j <= y2-1:
                    linha_cropada.append(imagem_original[i][j])
            imagem_crop.append(linha_cropada)

    return imagem_crop

def shrink(imagem_original): #OK!
    imagem_shrink = []
    for x in range(0, len(imagem_original), 2):
        linha_shrink = []
        for y in range(0, len(imagem_original[0]), 2):
            linha_menor = []
            for i in range(2):
                for j in range(2):
                    linha_menor.append(imagem_original[x+i][y+j])
            linha_shrink.append(max(linha_menor))
        imagem_shrink.append(linha_shrink)

    return imagem_shrink

def imprimir_imagem(matriz):
    print('P2')
    print(len(matriz[0]), len(matriz))
    print(255)
    for _ in matriz:
        print(*_)

def realizar_operacao_desejada(matriz, operacao):
    if operacao == 'flip':
        modo = input()
        if modo == 'horizontal':
            matriz_modificada = flip_horizontal(matriz)
        elif modo == 'vertical':
            matriz_modificada = flip_vertical(matriz)
    elif operacao == 'shift':
        modo = input()
        parametro = int(input())
        if modo == 'horizontal':
            matriz_modificada = shift_horizontal(matriz, parametro)
        elif modo == 'vertical':
            matriz_modificada = shift_vertical(matriz, parametro)
    elif operacao == 'crop':
        x1, y1 = input().split()
        x2, y2 = input().split()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        matriz_modificada = crop(matriz, x1, y1, x2, y2)
    elif operacao == 'shrink':
        matriz_modificada = shrink(matriz)

    return matriz_modificada

def perguntar_operacao():
    return input()

def pedir_imagem():
    tipo_do_arquivo = input()
    m, n = (input().split())
    m, n = int(m), int(n)
    valor_max = int(input())
    matriz = []

    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    return matriz

def main():
    imagem  = pedir_imagem()
    operacao = perguntar_operacao()
    nova_imagem = realizar_operacao_desejada(imagem, operacao)
    imprimir_imagem(nova_imagem)

main()