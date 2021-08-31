CFFLAGS: -std=99	-Wall	-Werror

.PHONY: all clean

all: calcular_matriz_transposta

calcular_matriz_transposta: calcular_matriz_transposta.c
	gcc $(CFFLAGS) calcular_matriz_transposta.c -o calcular_matriz_transposta 

clean:
	rm -f calcular_matriz_transposta

