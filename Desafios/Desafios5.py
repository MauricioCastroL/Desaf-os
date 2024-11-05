#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Sumar los elementos de cada fila

def suma(A):
    for fila in A:
        suma = sum(fila)
        print(suma)

if __name__ == '__main__':
    A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    suma(A)