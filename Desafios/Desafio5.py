#Autor: Mauricio Castro
#Fecha: 02/09/24

import tkinter as tk
from tkinter import *

def capturar():
    i = 0
    contador = []
    rut = [rutEntry.get()]  # Obtiene el RUT de la entrada de texto
    ruti = []
    algoritmo1 = [2, 3, 4, 5, 6, 7, 2, 3]  # Algoritmo con 8 dígitos
    algoritmo = [2, 3, 4, 5, 6, 7, 2]  # Algoritmo con 7 dígitos

    # Convierte cada carácter del RUT en un entero
    for j in rut[0]:
        ruti.append(int(j))

    ruti.reverse()  # Reversa los dígitos para el cálculo

    # Asegura que el RUT tenga 8 dígitos
    if len(ruti) == 8:
        for i, j in zip(ruti, algoritmo1):
            contador.append(i * j)

        # Calcula el dígito verificador
        suma = sum(contador)
        verificador = (suma // 11) * 11
        verificador = abs(suma - verificador)
        dig_verifi = 11 - verificador

        # Ajusta el dígito verificador para casos especiales
        if dig_verifi == 11:
            dig_verifi = 0
        elif dig_verifi == 10:
            dig_verifi = 'K'

        mostrar.set(dig_verifi)
        
    elif len(ruti) == 7:
        for i, j in zip(ruti, algoritmo):
            contador.append(i * j)

        # Calcula el dígito verificador
        suma = sum(contador)
        verificador = (suma // 11) * 11
        verificador = abs(suma - verificador)
        dig_verifi = 11 - verificador

        # Ajusta el dígito verificador para casos especiales
        if dig_verifi == 11:
            dig_verifi = 0
        elif dig_verifi == 10:
            dig_verifi = 'K'

        mostrar.set(dig_verifi)
    else:
        mostrar.set("El RUT debe tener 7 u 8 dígitos.")




def limpiar():
    rutEntry.delete(0, END)
    mostrar.set('')
    
if __name__ == '__main__':
    #Creo la ventana
    ventana = Tk()
    ventana.title('Verificador de RUT')
    ventana.resizable(False, False)
    ventana.geometry('300x200')

    #Creación del Frame
    miFrame = Frame(ventana, width=500, height=500)
    miFrame.pack()

    #Creación de los Label
    rut_text = Label(miFrame, text='Ingrese su RUT')
    rut_text.grid(row=0, column=0, padx=5, pady=5)

    #Creación de los Entry
    rutEntry = StringVar()
    rutEntry = Entry(miFrame, width=20)
    rutEntry.grid(row=0, column=1, padx=5, pady=5)

    #Caja de resultado
    mostrar = StringVar()
    mostrare = Entry(miFrame, width=20, state='readonly', textvariable=mostrar)
    mostrare.grid(row=1, column=1, padx=5, pady=5)

    #Creacion de los botones
    botonenviar = StringVar()
    boton = Button(text='Enviar', width=8, height=2, bg='green', command=capturar)
    boton.place(x=160, y=100)

    botonlimpiar = StringVar()
    miboton = Button(text='Limpiar', width=8, height=2, bg='green', command=limpiar)
    miboton.place(x=75, y=100)

    ventana.mainloop()