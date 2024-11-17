#Autor: Mauricio Castro L.
#Fecha: 4/11/24
#Objetivo: invertir una cadena (Version larga)

def cadena():
    frase = []
    texto = input('Ingrese una frase: ')
    for i in texto:
        if i.isalpha() == True:
            frase.append(i.strip())
    return frase

def mostrar(frase):
    print(f'{frase[::-1]}')

if __name__ == '__main__':
    frase = cadena()
    mostrar(frase)