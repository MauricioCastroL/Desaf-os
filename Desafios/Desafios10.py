#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Juego de palabras

import random

def inicio_juego():
    print('Este juego consiste en que adivines la palabra generada')
    print('aleatoriamente de un listado de palabras.')
    listado_random = ['makako']
    palabra = random.choice(listado_random)
    return palabra

def juego(palabra):
    n = len(palabra)
    print('_ ' * n)
    intento = input('Ingrese una palabra: ')
    lista_resultado = []
    numero_intento = 1
    resultado = False
    while resultado != True:
        if len(intento) > len(palabra):
            print(f'Ingrese una palabra o una letra, pero con el mismo largo que le indican los caracteres')
            numero_intento += 1
            intento = input('Ingrese una palabra o una letra: ')

        elif intento == palabra:
            print(f'Felicidades has ganado!, cant. intentos: {numero_intento}')
            resultado = True

        elif len(intento) == 1:
            for i in range(n):
                if intento == palabra[i]:
                    lista_resultado.append(intento)
                else:
                    lista_resultado.append('_')
            for i in lista_resultado:
                print(i, end=' ')
            print()
            lista_resultado = []
            numero_intento += 1
            intento = input('Ingrese una palabra o una letra: ')
        else:
            for i in range(n):
                if palabra[i] == intento[i]:
                    lista_resultado.append(intento[i])
                else:
                    lista_resultado.append('_')
            numero_intento += 1
            for i in lista_resultado:
                print(i, end=' ')
            print()
            lista_resultado = []
            intento = input('Ingrese una palabra o una letra: ')


if __name__ == '__main__':
    palabra = inicio_juego()
    juego(palabra)