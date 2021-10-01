lista_de_texto, lista_de_palavras, lista_de_posicoes_palavra, lista_posicoes_letras = [], [], [], []
palavra_formada = ""
pos_inicial = 0

qtd_linhas = int(input())

for linha in range(qtd_linhas): # Pede o texto ao usuário
    lista_de_texto.append(input().split())

for frase in lista_de_texto:  # Converte todos os items da lista_de_texto para uma lista de palavras
    for palavra in frase:
        palavra = palavra.lower()
        lista_de_palavras.append(palavra)

palavra_buscada = input()

def conferir(letra_buscada, posicao_ultima_palavra, lista): 
    """
    Confere se a palavra pode ser encontrada no texto
    de forma que satisfaça o jogo

    Parâmetros: a letra que está sendo procurada neste momento (deve-se utilizar um
    for para percorrer a palavra buscada)

    Retorna: caso haja um 'match' válido, retorna a letra encontrada e as posições, respectivamente
    da palavra e da letra na lista. Do contrário, retorna uma string vazia uma posição, a posição da palavra
    inserida no parâmetro e 0.
    """
    for i in range(posicao_ultima_palavra, len(lista)): # Procura a letra no range da última lista                                                              
            for j in range(len(lista[i])):              # onde foi encontrada uma letra até a ultima lista da lista maior
                if (letra_buscada == lista[i][j]):
                    return lista[i][j], i, j 
    
    return '', posicao_ultima_palavra, 0

for letra_buscada in palavra_buscada: # Ciclo para percorrer as letras da palavra buscada

    letra_encontrada, pos_palavra, pos_letra = conferir(letra_buscada, pos_inicial, lista_de_palavras)
    pos_inicial = pos_palavra+1 # Acrescenta +1 à posição da palavra para que a lista anterior
                                # não seja mais percorrida
    lista_de_posicoes_palavra.append(pos_palavra+1)
    lista_posicoes_letras.append(pos_letra+1)

    palavra_formada += letra_encontrada # Soma-se a letra encontrada à uma string vazia para
                                        # ser comparada futuramente

if palavra_formada == palavra_buscada: # Confirma se a palavra encontrada acima condiz com a palavra buscada
    print('Palavra encontrada')
    for i in range(len(palavra_formada)):
        print(f'{palavra_formada[i]}: palavra {lista_de_posicoes_palavra[i]}, letra {lista_posicoes_letras[i]}')
else:
    print('Palavra nao encontrada')