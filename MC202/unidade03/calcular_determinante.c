#include <stdio.h>
#include <math.h>
#define MAX 100

// Programa que calcula o determinante de uma matriz 3×3 (utilizando o teorema de laplace).

float calcula_determinante(int matriz[][MAX], int n)
{
    /*
    Calcula o determinante da matriz 3x3 utilizando o teorema de laplace.

    Recebe: a matriz e sua dimensão (3)
    Devolve: o valor do determinante.
    */
    int elemento, determinante = 0, cofator, d_a = 1, d_b = 1, value;
    for (int k = 0; k < n; k++)
    {
        if (k % 2 == 0)
        {
            value = 1;
        }
        else
        {
            value = -1;
        }
        elemento = matriz[k][0];
        for (int l = 0; l < n - 1; l++)
        {
            if (l != 0)
            {
                if (k == 0)
                {
                    d_a = matriz[k + 1][l] * matriz[k + (n - 1)][l + 1];
                    d_b = matriz[k + 1][l + 1] * matriz[k + (n - 1)][l];
                }
                else if (k == 1)
                {
                    d_a = matriz[k - 1][l] * matriz[k + 1][l + 1];
                    d_b = matriz[k - 1][l + 1] * matriz[k + 1][l];
                }
                else
                {
                    d_a = matriz[k - (n - 1)][l] * matriz[k - 1][l + 1];
                    d_b = matriz[k - (n - 1)][l + 1] * matriz[k - 1][l];
                }
                cofator = value * (d_a - d_b);
            }
        }
        determinante += elemento * cofator;
    }
    return determinante;
}

void preencher_matriz(int matriz[][MAX], int n)
{
    /*
    Recebe a matriz 3x3 do usuário.

    Recebe: a matriz a ser preenchida e seu tamanho (3).
    Devolve: nada.
    */
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &matriz[i][j]);
        }
    }
}

int main()
{
    int matriz[100][MAX], n = 3;
    preencher_matriz(matriz, n);
    printf("%.1f\n", calcula_determinante(matriz, n));
}
