#Autor: Mauricio Castro
#Fecha: 20/09/24

def contador(listado):
    vocales = 0
    consonantes = 0 
    for palabra in listado:
        if (palabra.lower() == 'a') or (palabra.lower() == 'e') or (palabra.lower() == 'i') or (palabra.lower() == 'o') or (palabra.lower() =='u'):
            vocales += 1
        elif palabra == ' ':
            continue
        elif palabra == '.':
            continue
        else:
            consonantes += 1
    return [vocales, consonantes]

def salida(voca_conso):
    print(f'"vocales": {voca_conso[0]}')
    print(f'"consonantes": {voca_conso[1]}')

if __name__ == '__main__':
    listado_palabras = contador(input('Listado de palabras: '))
    salida(listado_palabras)