#Autor: Mauricio Castro L.
#Fecha 10/12/2024
#Objetivo: Calculadora de Descuentos

def productos():
    articulos = []
    # Función que pida los productos y descuentos
    bandera = True
    while bandera == True:
        # Ingreso del producto y su descuento(%)
        producto = input('Ingrese el producto: ')
        if verificacion_producto(producto, alimentos):
            descuento = int(input('Ingrese su descuento(%): '))
            # Ingreso de los articulos y sus descuentos
            articulos.append([producto, descuento])
        
            bandera = input('Quiere ingresar más productos? (si/no): ')
            bandera = verificacion_bandera(bandera)
        else:
            print('Ingresa un producto válido')
            productos()

    return articulos


def verificacion_bandera(bandera):
    # Verifica si se quieren ingresar más productos 
    if bandera == 'si':
        bandera = True
    else:
        bandera = False
    
    return bandera


def verificacion_producto(producto, alimentos):
    # Función que verifica los alimentos ingresados
    n = len(alimentos)
    for i in range(n):
        if producto in alimentos[i][0]:
            return producto
    return False  


def calculadora_descuentos(articulos, alimentos):
    # Función que busque los productos
    articulos_precios = []
    n = len(alimentos)
    m = len(articulos)
    for i in range(n):
        for j in range(m):
            if articulos[j][0] == alimentos[i][0]:
                descuento = calculo(articulos[j], alimentos[i])
                articulos_precios.append(descuento)
    
    return articulos_precios


def calculo(articulo, alimento):
    # Función que calcule el descuento de los productos
    descuento = [articulo[0], int((alimento[1] * ((100 - articulo[1])/ 100)))]
    return descuento


def mostrar_precios(producto_precio):
    # Función que muestre el producto y su nuevo precio
    n = len(producto_precio)
    for i in range(n):
        print(f'EL nuevo precio de {producto_precio[i][0]} es de ${producto_precio[i][1]}')
    

if __name__ == '__main__':
    alimentos = [['Lentejas', 15000], ['Porotos', 10000], ['Huevos', 5000]]
    articulos = productos()
    producto_precio = calculadora_descuentos(articulos, alimentos)
    mostrar_precios(producto_precio)