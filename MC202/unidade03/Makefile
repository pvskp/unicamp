CFFLAGS: -std=99	-Wall	-Werror

# LDFLAGS: -lm

.PHONY: all clean

all: calcular_determinante

calcular_determinante: calcular_determinante.c
	gcc $(CFFLAGS) calcular_determinante.c -o calcular_determinante

clean:
	rm -f calcular_determinante

