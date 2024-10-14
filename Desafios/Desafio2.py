#Autor: Mauricio Castro
#Fecha: 15/08/24

def lectura(archivo1, archivo2):
    #Listas que almacenen los textos
    primero = []
    segundo = []
    #variables de apertura
    abrir = open(archivo1, 'r', encoding='UTF-8')
    apertura = open(archivo2, 'r', encoding='UTF-8')
    #Ciclod de apertura
    primero = abrir.read().rsplit()
    segundo = apertura.read().rsplit()
    #returno las listas con las palabras
    return primero, segundo

def linea_arch1(primero, segundo):
    #lista que almacene lo distinto
    diferente = []
    #Ciclo que recorra y compare
    for palabra, letras in zip(primero, segundo):
        if palabra != letras:
            diferente.append(letras)
    #returno los palabras diferentes del primer texto
    return diferente

def linea_arch2(primero, segundo):
    #Liste que almacene lo distinto
    diferente = []
    #Ciclo que reccorra y compare
    for palabra, letras in zip(primero, segundo):
        if palabra != letras:
            diferente.append(palabra)
    #returno las palabras diferentes del segundo texto
    return diferente

def mostrar(texto1, texto2):
    #varible que crea el archivo
    f = open('diferencias.txt', 'w', encoding='UTF-8')
    f.write('linea en archivo1.txt, pero no en archivo2.txt \n')
    #Ciclos que escriban los datos
    for i in texto2:
        f.write(f'- {i} \n')
    f.write('linea en archivo2.txt, pero no en archivo1.txt \n')
    for i in texto1:
        f.write(f'- {i} \n')
    #Cierre del archivo
    f.close()


if __name__ == '__main__':
    primero, segundo = lectura('archivo1.txt', 'archivo2.txt')
    diferente1 = linea_arch1(primero, segundo)
    diferente2 = linea_arch2(primero, segundo)
    mostrar(diferente1, diferente2)