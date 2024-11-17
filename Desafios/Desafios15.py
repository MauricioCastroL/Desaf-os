#Autor: Mauricio Castro L.
#Fecha: 4/11/24
#Objetivo: Factorial

def numero():
    numero = int(input('Ingrese un numero: '))
    return numero

def calculo_factorial(num):
    if num == 0 or num == 1:
        factorial = 1
        return factorial
    elif num < 0:
        print(f'No existen factoriales para números negativos')
    else:
        for i in range(num - 1, 1, -1):
            num *= i
        return num
    
def mostrar(factorial, num):
    print(f'El factorial de {num} es {factorial}')

if __name__ == '__main__':
    num = numero()
    factorial = calculo_factorial(num)
    mostrar(factorial, num)