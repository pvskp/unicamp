# Caça ao tesouro:

# Programa que recebe um campo no formato de uma matriz
# 8x8 composta por '.', 'x' e 'o'. Além da quantidade de sensores disponíveis para procurar o tesouro, suas posiçoes e seu alcance.

# 'x' representa o tesouro buscado, 'o' representa um bloqueio, por onde o alcance dos sensores não consegue passar e '.' é apenas uma parte comum do campo.

# O programa devolve a quantidade de baús que puderam ser encontrados no campo.


dimensao_da_matriz = 8 #8x8

matriz = []

for _ in range(dimensao_da_matriz):
    matriz.append(list(map(str, input().split())))

numero_de_sensores = int(input())

alcance_dos_sensores = int(input())

posicoes_dos_sensores = []

for _ in range(numero_de_sensores):
    posicoes_dos_sensores.append(list(map(int, input().split())))

m, n  = 8, 8 #coluna, linha

return_code = 0
contador_de_baus = 0

for sensor in posicoes_dos_sensores:
    # sensor[0]+alcance e sensor[0]-alcance -> alcance no eixo x
    # sensor[1]+alcance e sensor[1]-alcance -> alcance no eixo y
    x_positivo, x_negativo = (sensor[0]+alcance_dos_sensores), (sensor[0]-alcance_dos_sensores)
    y_positivo, y_negativo = (sensor[1]+alcance_dos_sensores), (sensor[1]-alcance_dos_sensores)
    #Posso acessar a matriz com matriz[sensor[0]][sensor[1]]

    for y_p in range(sensor[1], y_positivo+1):
        if 0 <= y_p < 8:
            if matriz[sensor[0]][y_p] == "x":
                contador_de_baus += 1
                matriz[sensor[0]][y_p] = "."
            elif matriz[sensor[0]][y_p] == "o":
                break
    for y_n in range(sensor[1], y_negativo-1, -1):
        if 0 <= y_n < 8:
            if matriz[sensor[0]][y_n] == "x":
                contador_de_baus += 1
                matriz[sensor[0]][y_n] = "."
            elif matriz[sensor[0]][y_n] == "o":
                break
    for x_p in range(sensor[0], x_positivo+1):
        if 0 <= x_p < 8:
            if matriz[x_p][sensor[1]] == "x":
                contador_de_baus += 1
                matriz[x_p][sensor[1]] = "."
            elif matriz[x_p][sensor[1]] == "o":
                break
    for x_n in range(sensor[0], x_negativo-1, -1):
        if 0 <= x_n < 8:
            if matriz[x_n][sensor[1]] == "x":
                contador_de_baus += 1
                matriz[x_n][sensor[1]] = "."
            elif matriz[x_n][sensor[1]] == "o":
                break

if contador_de_baus > 0:
    print(f'{contador_de_baus} bau(s) encontrado(s).')
else:
    print('Nenhum bau encontrado.')
