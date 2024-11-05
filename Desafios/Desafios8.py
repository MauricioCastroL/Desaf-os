#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Serie de fibonacci

def crear_serie():
    a, b = 0, 1
    for i in range(10):
        print( a + b)
        a, b = b, a + b

if __name__ == '__main__':
    crear_serie()