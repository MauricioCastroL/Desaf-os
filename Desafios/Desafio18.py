#Autor: Mauricio Castro L.
#Fecha: 11/11/24

def datos():
    lista = [10, 20, 30, 50, 40, 80, 40]
    return lista

def ordenamiento(lista):
    lista = ordeno(lista)
    return lista

def ordeno(lista):
    lista_ordenada = []
    i = 0
    while len(lista) != 0:
        minimo = min(lista)
        lista.remove(minimo)
        lista_ordenada.append(minimo)
        i += 1
    return lista_ordenada


if __name__ == '__main__':
    lista = datos()
    lista = ordenamiento(lista)
    print(lista)