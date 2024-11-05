#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Suma de matrices

def suma_matriz(A, B):
    C = [

    ]
    for i in range(len(A)):
        fila = []
        for j in range(len(B)):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

def mostrar(C):
    for fila in C:
        print(fila)       


if __name__ == '__main__': 
    # Matriz A
    A = [
    [1, 2, 3],
    [4, 7, 6],
    [7, 8, 4]
    ]
    B = [
    [9, 8, 7],
    [6, 5, 4],
    [7, 2, 1]
    ]
    C = suma_matriz(A, B)
    mostrar(C)
