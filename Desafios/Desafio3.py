#Autor: Mauricio Castro
#Fecha: 15/08/24

#Funcion que lea el archivo
def lectura(archivo):
    #Lista donde se almacenen las palabras
    palabras = []
    #Variable que abra los archivos
    f = open(archivo, 'r', encoding='UTF-8')
    palabras = f.read().rsplit()
    #returno la lista con las palabras
    return palabras

#Funcion que cuenta la cantidad de palabras
def contador(palabras):
    cantidad_palabras = len(palabras)
    #returno la cantidad de palabras
    return cantidad_palabras

#Funcion que cuente las freses
def frases(palabras):
    #Variable que cuente
    contador = 0 
    #Ciclo que recorra cada .
    for punto in palabras:
        if punto.endswith('.'):
            contador += 1
    #returno lacantidad de frases
    return contador 

def caracteres(palabras):
    #Creo caracteres para eliminar
    caracter = '.'
    c = '¡'
    ca = '?'
    car = '¿'
    cara = '!'
    carac = '"'
    palabras = [palabra.replace(caracter, '') for palabra in palabras]
    palabras = [palabra.replace(c, '') for palabra in palabras]
    palabras = [palabra.replace(ca, '') for palabra in palabras]
    palabras = [palabra.replace(car, '') for palabra in palabras]
    palabras = [palabra.replace(cara, '') for palabra in palabras]
    palabras = [palabra.replace(carac, '') for palabra in palabras]
    #returno la lista sin caracteres raros
    return palabras
    
#Funcion que busque la cant. de apariciones
def buscador(palabras):
    #Creo un contador 
    contador = 0
    #preguntar por la palab. por buscar
    palabra = input('¿Qué palabra desea buscar?: ')
    #Ciclo que busque cuantas veces aparece la palabra
    for busqueda in palabras:
        if busqueda.lower() == palabra.lower():
            contador += 1
    #returno el contador
    return contador

#Funcion que guarde palabras unicas
def guardar_palabras(palabras):
    #Lista que contenga las palabras unicas
    guardador = []
    #Ciclo que recorre y cuente la frec. de las palabras
    for i in palabras:
        if palabras.count(i) == 1:
            guardador.append(i)
    #reutrno la lista con las palabras unicas
    return guardador

#Funcion que resuma el texto a 100 palabras
def resumen(palabras):
    return palabras[0:101]

def mostrar(cantidad_palabras, contador, cant_palab_buscada, guardador, resumido):
    f = open('analisis_textos.txt', 'w', encoding='UTF-8')
    f.write(f'la cantidad de palabras es de: {cantidad_palabras}\n')
    f.write(f'la cantidad de frases es de: {contador}\n')
    f.write(f'la frecuencia de la palabra buscada es de: {cant_palab_buscada}\n')
    f.write('las palabras unicas son: \n')
    for cantidad in guardador:
        f.write(f'-{cantidad}\n')
    f.write(f'{resumido}')
    f.close()


if __name__ == '__main__':
    palabras = lectura('archivo2.txt')
    cantidad_palabras = contador(palabras)
    contador = frases(palabras)
    palabras_sin_carac = caracteres(palabras)
    cant_palab_buscada = buscador(palabras_sin_carac)
    guardador = guardar_palabras(palabras_sin_carac)
    resumido = resumen(palabras_sin_carac)
    mostrar(cantidad_palabras, contador, cant_palab_buscada, guardador, resumido)