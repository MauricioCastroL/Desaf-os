#Autor: Mauricio Castro
#Fecha: 14/08/24

#Funcion que abra el archivo
def lectura(archivo):
    #Leo el archivo
    palabras = []
    abrir = open(archivo , 'r', encoding='UTF-8')
    for palabra in abrir:
        palabras.append(palabra.rstrip().split(' '))
    #returno listado con las palabras
    return palabras

#Funcion que cuente la frec. por palabra
def contador_palabras(palabras):
    contador = []
    frecuencia = {}
    frecuencia_copy = {}
    #Accedo a las listas de las lineas
    for linea in palabras:
        #Accedo a las palabras de las listas
        for palabra in linea:
                #Creo una lista que almacene las palabras
                contador.append(palabra)
                #Agrego a un dic. las palabras y su frec.
                frecuencia[palabra] = contador.count(palabra)
    #Creo una copia del diccioanrio
    frecuencia_copy = frecuencia.copy()
    #Creo un ciclo para que los valores sean listas
    for clave in frecuencia_copy:
        valor = frecuencia_copy[clave]
        frecuencia_copy[clave] = [valor]
    #returno el diccionario y su copia con modificaciones
    return frecuencia, contador, frecuencia_copy

#Función que saque el % de la frecuencia
def porcentaje_frecuencia(diccionario, contador, diccionario_copy):
    porcentajes = []
    #ciclo que recorra las frecuencias
    for valores in diccionario.values():
        #calculo de los prorcentajes
        porcentaje = (valores / len(contador)) * 100
        porcentaje = round(porcentaje, 2)
        #agrego los porcentajes a la lista
        porcentajes.append(porcentaje)
    return porcentajes

#Función que agrege los porcentajes al diccionario
def diccionario(porcentajes, diccionario):
    claves = list(diccionario.keys())
    for clave, valor in zip(claves, porcentajes):
        diccionario[clave] = diccionario.get(clave, []) + [str(valor) + '%']
    return diccionario

#Función que muestre los datos
def mostar(diccionario):
    archivo = open('palabras_frecuencia.txt', 'w', encoding='UTF-8')
    archivo.write('palabra,frecuencia,porcentaje \n')
    for clave, valores in diccionario.items():
        archivo.write(f'{clave}: {valores} \n')
    archivo.close()


if __name__ == "__main__":
    palabras = lectura('palabras.txt')
    frecuencia, contador, frecuencia_copy = contador_palabras(palabras)
    porcentajes = porcentaje_frecuencia(frecuencia, contador, frecuencia_copy)
    dic = diccionario(porcentajes, frecuencia_copy)
    mostar(dic)