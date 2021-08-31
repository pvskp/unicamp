#include <stdio.h>
#define MAX 100

// Programa que utiliza uma função iterativa que, dada uma matriz real, calcula a matriz transposta

void imprime_transposta(float matriz_transposta[][MAX], int m, int n)
{
    /*
    Imprime a dada matriz transposta real.

    Recebe: a matriz transposta, a quantidade de linhas e a quantidade de colunas.
    Devolve: nada.
    */
    printf("\nMatriz transposta: \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%.1f ", matriz_transposta[i][j]);
        }
        printf("\n");
    }
}

void calcular_transposta(float matriz_original[][MAX], float matriz_transposta[][MAX], int m, int n)
{
    /*
    Calcula a transposta de uma dada matriz real.

    Recebe: A matriz original, a matriz transposta a ser preenchida e sua quantidade de linhas e colunas, respectivamente
    Devolve: nada.
    */
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
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

void preencher_matriz(float matriz[][MAX], int m, int n)
{
    /*
    Recebe a matriz principal, no formato de ponto flutuante.

    Recebe: A matriz a ser preenchida, a quantidade de linhas e a quantidade de colunas.
    Devolve: nada.
    */
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%f", &matriz[i][j]);
        }
    }
}

int main()
{
    float matriz_original[100][MAX], matriz_transposta[100][MAX];
    int m, n;
    printf("Entre com a quantidade de linhas: ");
    scanf("%d", &m);
    printf("Entre com a quantidade de colunas: ");
    scanf("%d", &n);
    preencher_matriz(matriz_original, m, n);
    calcular_transposta(matriz_original, matriz_transposta, m, n);
    imprime_transposta(matriz_transposta, m, n);
}