#Autor: Mauricio Castro L.
#Fecha: 29/10/24

def menu():
    print(f'Elija una opción, Agregar, Eliminar o Buscar un contacto.')
    opcion = input('ELija su opción: ')
    return opcion

def opcion(eleccion, contactos):
    if eleccion == 'Agregar':
        contactos = agregar(contactos)
        return contactos
    if eleccion == 'Eliminar':
        contactos = eliminar(contactos)
        return contactos
    if eleccion == 'Mostrar':
        contactos = mostrar(contactos)
        return contactos

def agregar(contactos):
    contacto = input('Ingrese el nombre del contacto: ')
    telefono = input('Agrege un número telefonico: ')
    correo = input('Agregue un correo: ')
    contactos[contacto] = ['telefono: ' + telefono, 'correo: ' + correo]
    return contactos

def eliminar(contactos):
    print(contactos)
    opcion = input('Ingrese el nombre de a quien quiere eliminar\nde sus contactos: ')
    del(contactos[opcion])
    return contactos

def mostrar(contactos):
    nombre = input('Ingrese el nombre de la persona a la que busca: ')
    if nombre in contactos:
        print(contactos[nombre])

if __name__ == '__main__':
    contactos = {
        'Mauricio': ['telefono: 56975991039', 'correo: mauriciocastro@gmail.com']
    }
    eleccion = menu()
    opcion(eleccion, contactos)