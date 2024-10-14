#Autor: Mauricio Castro L
#Fecha: 13/08/2024

#Funcion que lea el archivo
def abrir(archivo):
    ent = open(archivo, "r")
    datos = []
    for i in ent:
        datos.append(i.strip().split(","))
    del datos[0]
    ent.close()
    return datos

#funcion que calcule el total de ventas por producto
def productos(datos):
    productos = {}
    for i in datos:
        if i[1] in productos:
            productos[i[1]] += int(i[2])
        else:
            productos[i[1]] = int(i[2])
    return productos

def venta_por_tienda(datos):
    tiendas = {}
    for i in datos:
        if i[0] in tiendas:
            tiendas[i[0]] += int(i[2])
        else:
            tiendas[i[0]] = int(i[2])
    return tiendas

def archivo_salida(venta_productos, venta_por_tienda):
    salida = open("venta_por_producto.txt", "w")
    sal = open("venta_por_tienda.txt", "w")

    for i in venta_productos:
        salida.write(f"{i}: {venta_productos[i]}\n")
    salida.close()

    for i in venta_por_tienda:
        sal.write(f"{i}: {venta_por_tienda[i]}\n")
    sal.close()
    print("Archivo salida generado correctamente.")
    




if __name__ == '__main__':
    datos = abrir("ventas.txt")
    venta_productos = productos(datos)
    venta_por_tienda = venta_por_tienda(datos)
    archivo_salida(venta_productos, venta_por_tienda)