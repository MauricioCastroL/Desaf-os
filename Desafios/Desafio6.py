#Autor: Mauricio Castro
#Fecha: 10/09/24

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
import numpy as np
import matplotlib.pyplot as plt

def calculo():
    if grados.get() == '':
        resultado.set('Ingrese el grado de la ecuación')

    if (grados.get() == '1'):
        if factor_a.get() == '':
            resultado.set('Ingrese un valor en A')
        try:
            A = int(factor_a.get())
            B = int(factor_b.get())
            intersecta_x = -int(B)/int(A)
            resultado.set(f'Intersecta EJE X: {intersecta_x,0}')

            x = np.arange(-100, 100, 0.01)
            plt.plot(x, A*x + B, 'red')
            plt.xlabel('$x$')
            plt.ylabel('$f(x)$')
            plt.title('Gráfico ecuación primer grado')
            plt.show()

        except ZeroDivisionError:
            resultado.set('Ingrese un valor distinto de 0 en A')
        except ValueError:
            resultado.set('Ingrese valores validos')

    if (grados.get() == '2'):
        if (factor_a.get() == ''):
            resultado.set('Ingrese un valor en A')
        try:
            A = int(factor_a.get())
            B = int(factor_b.get())
            C = int(factor_c.get())
            discriminante = B**2 - 4 * A * C

            if discriminante == 0:
                try:
                    intersecta_x = (-B + math.sqrt(B**2 - 4 * A * C)) / 2 * A
                    resultado.set(f'Intersecta en EJE X: {round(intersecta_x, 2), 0}')

                    x = np.arange(-100, 100, 0.01)
                    plt.plot(x, A*x**2 + B*x + C, 'red')
                    plt.xlabel('$x$')
                    plt.ylabel('$f(x)$')
                    plt.title('Gráfico ecuación primer grado')
                    plt.show()

                except ZeroDivisionError:
                    resultado.set('A debe ser distinto de 0')
                except ValueError:
                    resultado.set('Ingrese valores validos')

            if discriminante > 0:
                try:
                    intersecta_x = (-B + math.sqrt(B**2 - 4 * A * C)) / 2 * A
                    intersecta_x1 = (-B - math.sqrt(B**2 - 4 * A * C)) / 2 * A
                    resultado.set(f'Intersecta en EJE X: {round(intersecta_x, 2), 0}, {round(intersecta_x1, 2), 0}')

                    x = np.arange(-100, 100, 0.01)
                    plt.plot(x, A*x**2 + B*x + C, 'red')
                    plt.xlabel('$x$')
                    plt.ylabel('$f(x)$')
                    plt.title('Gráfico ecuación primer grado')
                    plt.show()

                except ZeroDivisionError:
                    resultado.set('A debe ser un valor distinto de 0')
                except ValueError:
                    resultado.set('Ingrese valores validos')
            
            if discriminante < 0:
                try:
                    real_x = -B / (2 * A)
                    imaginario_x = math.sqrt(-int(discriminante))
                    resultado.set(f'Intersecta en EJE X: {real_x:.2f} ± {imaginario_x:.2f}i')

                    x = np.arange(-100, 100, 0.01)
                    plt.plot(x, A*x**2 + B*x + C, 'red')
                    plt.xlabel('$x$')
                    plt.ylabel('$f(x)$')
                    plt.title('Gráfico ecuación primer grado')
                    plt.show()

                except ZeroDivisionError:
                    resultado.set('A debe ser un valor distinto de 0')
        except ValueError:
            resultado.set('Ingrese valores validos')


if __name__ == '__main__':
    ventana = Tk()
    ventana.title('Calculadora de ecuaciones')
    ventana.geometry('300x300+1000+100')
    ventana.resizable(False, False)
    miFrame = Frame(ventana, height=500, width=500)
    miFrame.pack()
    frame = Frame(ventana, width=500, height=500).place(x=50, y=100)

    #Cuadro del grado de la ecuación
    gradotext = Label(miFrame, text='Ingrese el grado de la ecuación').grid(column=0, row=0, padx=5, pady=5)
    grados = StringVar()
    grado = ttk.Combobox(miFrame, values=[1, 2], width=4, height=1, state='readonly', textvariable=grados).grid(row=0, column=1, padx=5, pady=5)

    factor_a_text = Label(ventana, text='Factor A').place(x=10, y=30)
    factor_a = StringVar()
    factor_A = Entry(ventana, width=2, textvariable=factor_a).place(x=70, y=30)

    factor_b_text = Label(ventana, text='Factor B').place(x=110, y=30)
    factor_b = StringVar()
    factor_B = Entry(ventana, width=2, textvariable=factor_b).place(x=170, y=30)

    factor_c_text = Label(ventana, text='Factor C').place(x=210, y=30)
    factor_c = StringVar()
    factor_C = Entry(ventana, width=2, textvariable=factor_c).place(x=270, y=30)

    resultadotext = Label(ventana, text='Resultado').place(x=10, y=60)
    resultado = StringVar()
    cuadro_resul = Entry(ventana, width=20, state='readonly', textvariable=resultado).place(x=80, y=60)

    graficotext = Label(ventana, text='Gráfico').place(x=10, y=90)
    
    boton = Button(ventana, text='Enviar', bg='grey', command=calculo).place(x=210, y=60)
    
    ventana.mainloop()