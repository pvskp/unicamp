"""
Magic:

Programa que recebe uma série de cartas, atributos e uma ordem de prioridade de atributos
e devolve as cartas ordenadas com base nessa ordem de prioridade utilizando o algoritmo de 
insertion sort.
"""

def imprimir_insercoes(lista_ordenada, n_insercoes):
  for atributo in lista_ordenada:
    print('{:15s}'.format(atributo[0]), ''.join('{:>10}'.format(item) for item in atributo[1:]))
  print('Insercoes realizadas:', n_insercoes)

def criar_matriz_ordenada(entrada):
  return [list(_.values()) for _ in entrada]

def insertion_sort(lista, ordem):
  insercoes = 0
  for b in reversed(ordem):
    for i in range(1, len(lista)):
      chave = lista[i]
      t = i
      eh_insercao = False
      while (t > 0) and (chave[b] > lista[t-1][b]):  
        eh_insercao = True
        lista[t] = lista[t - 1]
        t -= 1
      lista[t] = chave
      if eh_insercao:
        insercoes += 1
  
  return insercoes

def pedir_entrada():
    quantidade_de_cartas = int(input())
    atributos = input().split()
    lista_entradas = []
    for _ in range(quantidade_de_cartas):
        lista_entradas.append(dict(zip(atributos, input().split()))) # lista de dicionários
    
    ordem_de_prioridade = input().split()

    for i in (ordem_de_prioridade):
      for j in range(len(lista_entradas)):
        lista_entradas[j][i] = int(lista_entradas[j][i])

    return lista_entradas, ordem_de_prioridade

def main():
    entrada, ordem_de_prioridade = pedir_entrada()
    insercoes = insertion_sort(entrada, ordem_de_prioridade) # algoritmo pronto
    lista_ordenada = criar_matriz_ordenada(entrada) # cria uma matriz onde cada linha representa um animal
    imprimir_insercoes(lista_ordenada, insercoes)

main()