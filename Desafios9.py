#Autor: Mauricio Castro L.
#Fecha: 30/10/24
#Objetivo: Ordenamiento de burbuja

def ordenamiento(a):
    if len(a) == 1:
        print('ya esta listo')
    if len(a) == 2:
        if a[0] < a[1]:
            print('ya esta')
        else:
            a = [a[1], a[0]]
            print(a)
    if len(a) > 3:
        n = len(a)
        for i in range(n-1):  
            for j in range(n-1-i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    
    print(a)

if __name__ == '__main__':
    a = [8, 23, 12, 81, 43, 55, 70, 88, 99, 1300]
    ordenamiento(a)