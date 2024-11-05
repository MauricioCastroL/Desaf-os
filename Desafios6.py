#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Encontrar el máx. de cada col.

def max_columna(A):
    filas = list(zip(* A))
    for fila in filas:
        print(max(fila))


if __name__ == '__main__':
    A = [
    [1, 2, 305],
    [40, 50, 6],
    [7, 8, 9]
    ]
    max_columna(A)