#Autor: Mauricio Castro L.
#Fecha: 4/11/24
#Objetivo: invertir una cadena (Version corta)

def cadena():
    frase = input('Ingrese una frase: ')
    return frase

def mostrar(frase):
    print(f'{frase[::-1]}')

if __name__ == '__main__':
    frase = cadena()
    mostrar(frase)