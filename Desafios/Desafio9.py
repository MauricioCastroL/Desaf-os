#Autor: Mauricio Castro
#Fecha: 18/09/24

import tkinter as tk
from tkinter import *
from tkinter import ttk


def convertidor():
    CLP = 931.38
    USD = 1
    EUR = 0.000965773
    if (taza_1.get() == 'CLP') and (taza_2.get() == 'USD'):
        resultado = float(dinero_str.get())/ CLP
        tk.Entry(ventana, width=12, state='readonly').place(x=120, y=120)
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
                widget.config(state='normal')  # Cambia a 'normal' para actualizar
                widget.delete(0, tk.END)
                widget.insert(0, f'${round(resultado,2):,.2f}'.replace(',','.'))  # Muestra las raíces del polinomio
                widget.config(state='readonly')

    if (taza_1.get() == 'USD') and (taza_2.get() == 'CLP'):
        resultado = CLP * float(dinero_str.get())
        tk.Entry(ventana, width=12, state='readonly').place(x=120, y=120)
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
                widget.config(state='normal')  # Cambia a 'normal' para actualizar
                widget.delete(0, tk.END)
                widget.insert(0, f'${round(resultado,2):,.2f}'.replace(',','.'))  # Muestra las raíces del polinomio
                widget.config(state='readonly') 

    if (taza_1.get() == 'CLP') and (taza_2.get() == 'EUR'):
        resultado = EUR * float(dinero_str.get())
        tk.Entry(ventana, width=12, state='readonly').place(x=120, y=120)
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
                widget.config(state='normal')  # Cambia a 'normal' para actualizar
                widget.delete(0, tk.END)
                widget.insert(0, f'${round(resultado,2):,.2f}'.replace(',','.'))  # Muestra las raíces del polinomio
                widget.config(state='readonly') 

    if (taza_1.get() == 'EUR') and (taza_2.get() == 'CLP'):
        resultado = 1035.49 * float(dinero_str.get()) 
        tk.Entry(ventana, width=12, state='readonly').place(x=120, y=120)
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
                widget.config(state='normal')  # Cambia a 'normal' para actualizar
                widget.delete(0, tk.END)
                widget.insert(0, f'${round(resultado,2):,.2f}'.replace(',','.'))  # Muestra las raíces del polinomio
                widget.config(state='readonly')

    if (taza_1.get() == 'EUR') and (taza_2.get() == 'USD'):
        resultado = 1.112 * float(dinero_str.get()) 
        tk.Entry(ventana, width=12, state='readonly').place(x=120, y=120)
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
                widget.config(state='normal')  # Cambia a 'normal' para actualizar
                widget.delete(0, tk.END)
                widget.insert(0, f'${round(resultado,2):,.2f}'.replace(',','.'))  # Muestra las raíces del polinomio
                widget.config(state='readonly')
    
    if (taza_1.get() == 'USD') and (taza_2.get() == 'EUR'):
        resultado = 0.899106 * float(dinero_str.get()) 
        tk.Entry(ventana, width=12, state='readonly').place(x=120, y=120)
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
                widget.config(state='normal')  # Cambia a 'normal' para actualizar
                widget.delete(0, tk.END)
                widget.insert(0, f'${round(resultado,2):,.2f}'.replace(',','.'))  # Muestra las raíces del polinomio
                widget.config(state='readonly')


if __name__ == '__main__':
    ventana = tk.Tk()
    try:
        icono = PhotoImage(file='dinero.png')
        ventana.iconphoto(False, icono)
    except Exception as e:
        print(f'File not found {e}')
    ventana.geometry('300x200+1000+100')
    ventana.resizable(False, False)
    ventana.configure(background='#0a1937')

    tk.Label(text='Convertidor de Divisas', fg='#ffc842', bg='#0a1937', font=('Roboto Cn', 10)).place(x=90,y=10)

    tk.Label(text='De:', fg='#ffc842', bg='#0a1937').place(x=10, y=50)
    taza_1 = StringVar()
    taza1 = ttk.Combobox(ventana, state='readonly', values=['CLP', 'USD', 'EUR'], width=5, textvariable=taza_1).place(x=40, y=50)
    tk.Label(text='A:', fg='#ffc842', bg='#0a1937').place(x=200, y=50)
    taza_2 = StringVar()
    taza2 = ttk.Combobox(ventana, state='readonly', values=['CLP', 'USD', 'EUR'], width=5, textvariable=taza_2).place(x=220, y=50)

    conversor = Button(ventana, bg='#ffc842', width=8, text='Convertir', command=convertidor).place(x=120, y=50)

    tk.Label(ventana, text='Cantidad ($)', fg='#ffc842', bg='#0a1937').place(x=45, y=90)
    dinero_str = StringVar()
    dinero = tk.Entry(ventana, width=10, textvariable=dinero_str). place(x=120, y=90)


    ventana.mainloop()