#Autor: Mauricio Castro L.
#Fecha: 28/10/24

'''Desafío 2: Calculadora de Edad en Días
Crea un programa que calcule la edad de una persona en días.
Requisitos:

* Pide al usuario su fecha de nacimiento.
* Calcula la edad en días desde la fecha de nacimiento hasta hoy.
* Muestra la edad en días.'''

from datetime import date

def fechas():
    dia_nacimiento = int(input('Ingrese su día de nacimiento: '))
    mes_nacimiento = int(input('Ingrese su mes de nacimiento: '))
    ano_nacimiento = int(input('Ingrese su año de nacimiento: '))
    fecha_actual = date.today()
    dia_sys = int(fecha_actual.day)
    mes_sys = int(fecha_actual.month)
    ano_sys = int(fecha_actual.year)
    nacimiento = [dia_nacimiento, mes_nacimiento, ano_nacimiento]
    fecha_sistema = [dia_sys, mes_sys, ano_sys]
    return nacimiento, fecha_sistema

def calculo(nacimiento, fecha_sistema):
    if (nacimiento[-1] == fecha_sistema[-1]): #Mismo año y distinto mes 
        dias = (fecha_sistema[0] - nacimiento[0]) + ((fecha_sistema[1] - nacimiento[1]) * 30 ) 

    elif (nacimiento[-1] == fecha_sistema[-1]) and (nacimiento[1] == fecha_sistema[1]): #Mismo año y mismo mes
        dias = (fecha_sistema[0] - nacimiento[0])

    elif (nacimiento[-1] == fecha_sistema[-1]) and (nacimiento[1] == fecha_sistema[1]) and (nacimiento[0] == fecha_sistema[0]): #Todo igual
        dias = 0

    else: #Nada igual
        dias = (fecha_sistema[0] - nacimiento[0]) + ((fecha_sistema[1] - nacimiento[1]) * 30 ) + ((fecha_sistema[-1] - nacimiento[-1]) * 365 )

    return dias

def mostrar(dias):
    print(f'Tienes {dias} días de nacido.')

if __name__ == '__main__':
    nacimiento, fecha_sistema = fechas()
    resultado = calculo(nacimiento, fecha_sistema)
    mostrar(resultado)