#Autor: Mauricio Castro L.
#Fecha: 28/10/24

import random

def eleccion():
    juego = input('Elija (Piedra, Papel o Tijera): ')
    return juego

def ganador(juego):
    lista = ['Piedra', 'Papel', 'Tijera']
    eleccion_maquina = random.choice(lista)
    if (eleccion_maquina == juego):
        print(f'{eleccion_maquina}')
        print(f'Es un empate')

    elif (eleccion_maquina == 'Piedra') and (juego == 'Papel'):
        print(f'{eleccion_maquina}')
        print(f'Ganaste!')
    elif (eleccion_maquina == 'Piedra') and (juego == 'Tijera'):
        print(f'{eleccion_maquina}')
        print(f'Perdiste!')

    elif (eleccion_maquina == 'Papel') and (juego == 'Tijera'):
        print(f'{eleccion_maquina}')
        print(f'Ganaste!')
    elif (eleccion_maquina == 'Papel') and (juego == 'Piedra'):
        print(f'{eleccion_maquina}')
        print(f'Perdiste!')

    elif (eleccion_maquina == 'Tijera') and (juego == 'Piedra'):
        print(f'{eleccion_maquina}')
        print(f'Ganaste!')
    elif (eleccion_maquina == 'Tijera') and (juego == 'Papel'):
        print(f'{eleccion_maquina}')
        print(f'Perdiste!')


if __name__ == '__main__':
    juego = eleccion()
    resultado = ganador(juego)