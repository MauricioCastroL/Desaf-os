#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Encuentra y muestra los elementos de la diagonal secundaria de una matriz cuadrada.

def diag_secun(A):
    i = 2
    for fila in A:
        print(fila[i])
        i = i - 1



if __name__ == '__main__':
    A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    diag_secun(A)