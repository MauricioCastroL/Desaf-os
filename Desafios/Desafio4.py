#Autor: Mauricio Castro
#Fecha: 16/08/24

#Funcion que lea el archivo
def lectura(archivo):
    # lista que almacene los datos
    datos = []
    palabras = []
    f = open(archivo, 'r', encoding='UTF-8')
    #Ciclo que almacene los datos
    for i in f:
        datos.append(i.rstrip().split(','))
    #Elimino encabezado
    del datos[0]
    #Ciclo que aplane  la lista
    for lista in datos:
        for palabra in lista:
            palabras.append(palabra)
    #returno la lista aplanada
    return palabras, datos

#Funcion que cuente el total de registros
def registros(datos):
    #returno la cantidad de registros
    return len(datos)

#Funcion que calcule la edad promedio
def edad_prom(denominador, datos):
    #Creo una variable que cuente
    contador = 0 
    #Ciclo que recorra buscando numeros
    for numero in datos:
        if numero.isdigit() == True:
            contador = contador + int(numero)
    #Variable que calcule el promedio de edad
    promedio = round(contador/denominador, 2)
    #returno el promedio
    return promedio

#Funcio que extraila la profesion más frecuente
def profesion(datos):
    #Lista que almacenara las profesiones
    profesiones = []
    #Ciclo que recorra las listas buscando las profesiones
    for i in datos:
        profesiones.append(i[-1])
    #returno la lista con las profesiones
    return profesiones

#Funcion que genere el archivo a mostrar los datos
def mostrar(num_registros, promedio, profesiones):
    f = open('informe.txt', 'w', encoding='UTF-8')
    f.write(f'El número total de registros son: {num_registros}\n')
    f.write(f'La edad promedio dentro de las profesiones es de: {promedio}\n')
    for i in profesiones:
        f.write(f'las profesiones son: {i}\n')
    f.close()


if __name__ == '__main__':
    datos, lista = lectura('datos.txt')
    num_registros = registros(lista)
    promedio = edad_prom(num_registros, datos)
    profesiones = profesion(lista)
    mostrar(num_registros, promedio, profesiones)
