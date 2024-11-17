#Autor: Mauricio Castro L.
#Fecha: 4/11/24
#Objetivo: Suma numeros pares (V.2.0)

def n_termino():
    pares = int(input('Ingrese el número de sumas de los n-primeros pares: '))
    return pares

def suma_pares(n):
    i = 1
    j = 0
    while i != pares:
        if i % 2 == 0:
            j += i
            i += 1
        else:
            i += 1
    return j

def mostrar(suma, pares):
    print(f'La suma de los {pares} primeros números pares es {suma}')

if __name__ == '__main__':
    pares = n_termino()    
    suma_pares = suma_pares(pares)
    mostrar(suma_pares, pares)