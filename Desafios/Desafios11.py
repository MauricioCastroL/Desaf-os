#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Analisis de textos

def lectura(archivo):  
    datos = []
    palabras = []
    file = open(archivo, 'r', encoding='UTF-8')

    for linea in file:
        linea = linea.rstrip().split(' ')
        datos.append(linea)

    for listas in datos:
        for elemento in listas:
            palabras.append(elemento.rstrip('.,').lower())
    return datos, palabras

def contador(datos):
    numero = 0
    for lista in datos:
        numero += len(lista)
    return numero


def long_promedio(datos, cant_palabras):
    numero = 0
    for lista in datos:
        for elemento in lista:
            if elemento[-1] == '.' or elemento[-1] == ',':
                numero += (len(elemento) - 1)
            else:
                numero += len(elemento)
    lon_prom = round(numero / cant_palabras, 2)
    return lon_prom

def palabra_comun(palabras):
    cantidad = []
    for palabra in palabras:
        numero = palabras.count(palabra)
        cantidad.append((palabra, numero))
    cantidad = set(cantidad)
    cantidad_ordenada = []
    for x, y in cantidad:
        cantidad_ordenada.append((x, y))
    for x, y in cantidad:
        print(f'Palabra: {x}, Frecuencia: {y}')

if __name__ == '__main__':
    datos, palabras = lectura('ejemplo.txt')
    cant_palabras = contador(datos)
    lon_prom = long_promedio(datos, cant_palabras)
    palabra_comun(palabras)