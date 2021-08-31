#include <stdio.h>
#define MAX 100

/*programa que utiliza função iterativa para decidir se uma matriz é simétrica*/

void imprimir_matriz(int matriz_original[][MAX], int mn)
{
	/*
	Imprime uma dada matriz, para fins de teste de entrada.

	Recebe: a matriz a ser impressa e suas dimensões n x n.
	Devolve: nada.
	*/
	for (int i = 0; i < mn; i++)
	{
		for (int j = 0; j < mn; j++)
		{
			printf("%d ", matriz_original[i][j]);
		}
		printf("\n");
	}
}

int conferir_simetria(int matriz_original[][MAX], int matriz_transposta[][MAX], int mn)
{
	/*
	Confere se a matriz original é simétrica, comparando esta com sua transposta.

	Recebe: a matriz original, sua transposta e sua dimensão n x n.

	Devolve: 1, caso seja simétrica e 0, caso não seja.
	*/
	for (int i = 0; i < mn; i++)
	{
		for (int j = 0; j < mn; j++)
		{
			if (matriz_original[i][j] != matriz_transposta[i][j])
			{
				return 0;
			}
		}
	}
	return 1;
}

void criar_transposta(int matriz_original[][MAX], int matriz_transposta[][MAX], int mn)
{
	/*
	Cria a matriz transposta com base na matriz previamente recebida.

	Recebe: a matriz original, a matriz transposta a ser preenchida e sua dimensão n x n.

	Devolve: nada.
	*/
	for (int i = 0; i < mn; i++)
	{
		for (int j = 0; j < mn; j++)
		{
			if (i == j)
			{
				matriz_transposta[i][j] = matriz_original[i][j];
			}
			else
			{
				matriz_transposta[j][i] = matriz_original[i][j];
			}
		}
	}
}

void receber_matriz(int matriz[][MAX], int mn)
{
	/*
	Recebe a entrada no formato de uma matriz.

	Recebe: a matriz a ser preenchida e sua quantidade de linhas		/colunas (matriz quadrada)

	Devolve: nada.
	*/
	for (int i = 0; i < mn; i++)
	{
		for (int j = 0; j < mn; j++)
		{
			scanf("%d", &matriz[i][j]);
		}
	}
}

int main()
{
	int mn, matriz[100][MAX], matriz_transposta[100][MAX];
	scanf("%d\n", &mn);
	receber_matriz(matriz, mn);
	criar_transposta(matriz, matriz_transposta, mn);
	if (conferir_simetria(matriz, matriz_transposta, mn))
	{
		printf("A matriz eh simetrica");
	}
	else
	{
		printf("A matriz NAO EH simetrica");
	}
}
