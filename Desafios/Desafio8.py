import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import numpy as np
import sympy as sp

def abrir_ecuaciones():
    ecuacion = tk.Toplevel()
    ecuacion.title("Ecuaciones")
    ecuacion.geometry('400x300+1000+100')
    ecuacion.configure(background='#0a1937')
    ecuacion.resizable(False, False)

    try:
        icono = PhotoImage(file='imagen.png')
        ecuacion.iconphoto(False, icono)
    except Exception as e:
        print(f"Error al cargar el icono: {e}")
    
    tk.Label(ecuacion, text='Aquí puedes resolver ecuaciones', bg='#0a1937', fg='white').place(x=50, y=10)

    tk.Label(ecuacion, text='Ingrese el grado de la ecuación', bg='#0a1937', fg='white').place(x=10, y=40)
    combobox = ttk.Combobox(ecuacion, values=[1, 2, 3], width=1, state='readonly')
    combobox.place(x=180, y=40)

    tk.Button(ecuacion, text='Enviar',command=lambda: crear_entry_ecuaciones(ecuacion, combobox.get())).place(x=220, y=40)

def crear_entry_ecuaciones(ecuacion, grado):
    # Limpia cualquier entrada previa
    for widget in ecuacion.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.destroy()
    
    try:
        grado = int(grado)
        if grado < 1:
            raise ValueError("El grado debe ser un número positivo.")
        
        # Crear campos de entrada según el grado
        for i in range(grado + 1):
            tk.Label(ecuacion, text=f'Coeficiente x^{i}:', bg='#0a1937', fg='white').place(x=10, y=60 + i*30)
            tk.Entry(ecuacion, width=8).place(x=100, y=60 + i*30)
    
            tk.Button(ecuacion, text='Calcular', command=lambda: calcular_ecuaciones(ecuacion, grado)).place(x=170, y=150)
            tk.Button(ecuacion, text='limpiar', command=lambda: limpiar_entry_ecuaciones(ecuacion)).place(x=240, y=150)
            
            tk.Label(ecuacion, text='Resultado', bg='#0a1937', fg='white').place(x=10, y=200)
            tk.Entry(ecuacion, width=25, state='readonly').place(x=70, y=200)

    
    except ValueError as e:
        tk.Label(ecuacion, text=f'Error: {e}', bg='#0a1937', fg='red').place(x=50, y=120)

def limpiar_entry_ecuaciones(ecuacion):
    for widget in ecuacion.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
            widget.config(state='normal')  # Cambia a 'normal' para actualizar
            widget.delete(0, tk.END)
            widget.config(state='readonly')

def calcular_ecuaciones(ecuacion, grado):
    coeficientes = [0] * (grado + 1)  # Inicializa con ceros
    
    # Extraer los coeficientes de los campos de entrada
    entries = [widget for widget in ecuacion.winfo_children() if isinstance(widget, tk.Entry) and widget.cget('state') == 'normal']
    
    # Verificar que el número de entradas coincide con el grado + 1
    if len(entries) != grado + 1:
        tk.Label(ecuacion, text='Error: Número incorrecto de coeficientes', bg='#0a1937', fg='red').place(x=50, y=60 + (grado + 1)*30 + 50)
        return
    
    for i, widget in enumerate(entries):
        valor = widget.get().strip()
        if valor:  # Si el campo no está vacío
            try:
                coeficiente = float(valor)
            except ValueError:
                coeficiente = 0  # Asume coeficiente 0 si hay un error
        else:
            coeficiente = 0  # Asume coeficiente 0 si el campo está vacío
        
        coeficientes[i] = coeficiente
    
    # Verificar si el coeficiente del término de mayor grado es 0
    if coeficientes[-1] == 0:
        tk.Label(ecuacion, text='Error: El coeficiente del término de mayor grado no puede ser 0', bg='#0a1937', fg='red').place(x=50, y=60 + (grado + 1)*30 + 50)
        return

    # Resolver el polinomio
    try:
        # `numpy.roots` encuentra las raíces de un polinomio
        raices = np.roots(coeficientes)
        resultados = ', '.join(f"{raiz:.2f}" for raiz in raices)
    except Exception as e:
        resultados = f"Error: {e}"
    
    # Actualiza el campo de resultado
    for widget in ecuacion.winfo_children():
        if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
            widget.config(state='normal')  # Cambia a 'normal' para actualizar
            widget.delete(0, tk.END)
            widget.insert(0, resultados)  # Muestra las raíces del polinomio
            widget.config(state='readonly')  # Vuelve a 'readonly'

def abrir_limites():
    limites = tk.Toplevel()
    limites.title("Límites")
    limites.geometry('400x300')
    limites.configure(background='#0a1937')
    limites.resizable(False, False)

    tk.Label(limites, text='Aquí puedes calcular límites', bg='#0a1937', fg='white').place(x=100, y=10)
    try:
        icono = PhotoImage(file='imagen.png')
        limites.iconphoto(False, icono)
    except Exception as e:
        print(f"Error al cargar el icono: {e}")
    
    tk.Label(limites, text='Aquí puedes calcular límites', bg='#0a1937', fg='white').place(x=100, y=10)

    tk.Label(limites, text='Ingrese la función', bg='#0a1937', fg='white').place(x=10, y=40)
    tk.Label(limites, text='Por ejemplo: sin(x)/x, log(x), x**2 + 2*x + 1', bg='#0a1937', fg='white').place(x=10, y=60)
    funcion_entry = tk.Entry(limites, width=30)
    funcion_entry.place(x=150, y=40)
    
    tk.Label(limites, text='Variable', bg='#0a1937', fg='white').place(x=10, y=100)
    var_entry = tk.Entry(limites, width=10)
    var_entry.place(x=150, y=100)
    
    tk.Label(limites, text='Límite al que tiende', bg='#0a1937', fg='white').place(x=10, y=140)
    limite_entry = tk.Entry(limites, width=10)
    limite_entry.place(x=150, y=140)

    tk.Button(limites, text='Calcular', command=lambda: calcular_limites(limites, funcion_entry.get(), var_entry.get(), limite_entry.get())).place(x=100, y=200)
    tk.Button(limites, text='Limpiar', command=lambda: limpiar_entry_limites(limites)).place(x=200, y=200)

    # Campo para mostrar el resultado
    tk.Label(limites, text='Resultado:', bg='#0a1937', fg='white').place(x=10, y=240)
    resultado_entry = tk.Entry(limites, width=50, state='readonly')
    resultado_entry.place(x=70, y=240)

def limpiar_entry_limites(limites):
    for widget in limites.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
            widget.config(state='normal')  # Cambia a 'normal' para actualizar
            widget.delete(0, tk.END)
            widget.config(state='readonly')

def calcular_limites(limites, funcion_str, variable_str, limite_str):
    # Limpiar resultados anteriores
    resultado_widget = [widget for widget in limites.winfo_children() if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly']
    if resultado_widget:
        resultado_widget[0].config(state='normal')  # Cambia a 'normal' para actualizar
        resultado_widget[0].delete(0, tk.END)
    
    # Definir símbolo para la variable
    try:
        variable = sp.Symbol(variable_str)
    except Exception as e:
        tk.Label(limites, text=f'Error en variable: {e}', bg='#0a1937', fg='red').place(x=10, y=280)
        return
    
    # Definir función
    try:
        funcion = sp.sympify(funcion_str)
    except Exception as e:
        tk.Label(limites, text=f'Error en función: {e}', bg='#0a1937', fg='red').place(x=10, y=280)
        return

    # Definir límite
    limite_str = limite_str.strip().lower()
    if limite_str == 'inf' or limite_str == 'oo':
        limite = sp.oo
    elif limite_str == '-inf' or limite_str == '-oo':
        limite = -sp.oo
    else:
        try:
            limite = float(limite_str)
        except ValueError:
            tk.Label(limites, text='Error en límite: Debe ser un número, ∞ o -∞', bg='#0a1937', fg='red').place(x=10, y=280)
            return

    # Calcular límite
    try:
        limite_resultado = sp.limit(funcion, variable, limite)
        
        # Convertir el resultado a una forma legible
        if limite_resultado == sp.oo:
            resultados = f"Limite de la función cuando {variable_str} tiende a {limite}: +∞"
        elif limite_resultado == -sp.oo:
            resultados = f"Limite de la función cuando {variable_str} tiende a {limite}: -∞"
        elif limite_resultado.is_real:
            resultados = f"Limite de la función cuando {variable_str} tiende a {limite}: {limite_resultado}"
        else:
            resultados = f"Limite de la función cuando {variable_str} tiende a {limite}: No definido"
    except Exception as e:
        resultados = f"Error: {e}"
    
    # Mostrar resultados
    resultado_widget[0].insert(0, resultados)  # Muestra los resultados
    resultado_widget[0].config(state='readonly')  # Vuelve a 'readonly'

    

def abrir_integrales():
    integrales = tk.Toplevel()
    integrales.title("Integrales")
    integrales.geometry('500x400')
    integrales.configure(background='#0a1937')
    integrales.resizable(False, False)

    try:
        icono = PhotoImage(file='imagen.png')
        integrales.iconphoto(False, icono)
    except Exception as e:
        print(f"Error al cargar el icono: {e}")
    
    tk.Label(integrales, text='Aquí puedes calcular integrales', bg='#0a1937', fg='white').place(x=150, y=10)

    tk.Label(integrales, text='Ingrese la función', bg='#0a1937', fg='white').place(x=10, y=40)
    tk.Label(integrales, text='Por ejemplo: sin(x)/x, log(x), x**2 + 2*x + 1', bg='#0a1937', fg='white').place(x=10, y=60)
    funcion_entry = tk.Entry(integrales, width=40)
    funcion_entry.place(x=150, y=40)
    
    tk.Label(integrales, text='Variable', bg='#0a1937', fg='white').place(x=10, y=100)
    var_entry = tk.Entry(integrales, width=10)
    var_entry.place(x=150, y=100)
    
    tk.Label(integrales, text='Límites de integración (opcional)', bg='#0a1937', fg='white').place(x=10, y=140)
    tk.Label(integrales, text='Inferior', bg='#0a1937', fg='white').place(x=10, y=170)
    limite_inf_entry = tk.Entry(integrales, width=10)
    limite_inf_entry.place(x=150, y=170)
    
    tk.Label(integrales, text='Superior', bg='#0a1937', fg='white').place(x=10, y=210)
    limite_sup_entry = tk.Entry(integrales, width=10)
    limite_sup_entry.place(x=150, y=210)

    tk.Button(integrales, text='Calcular Integral Definida', command=lambda: calcular_integral_definida(integrales, funcion_entry.get(), var_entry.get(), limite_inf_entry.get(), limite_sup_entry.get())).place(x=50, y=250)
    tk.Button(integrales, text='Calcular Integral Indefinida', command=lambda: calcular_integral_indefinida(integrales, funcion_entry.get(), var_entry.get())).place(x=200, y=250)
    tk.Button(integrales, text='Limpiar', command=lambda: limpiar_entry_integrales(integrales)).place(x=360, y=250)

    # Campo para mostrar el resultado
    tk.Label(integrales, text='Resultado:', bg='#0a1937', fg='white').place(x=10, y=290)
    resultado_entry = tk.Entry(integrales, width=60, state='readonly')
    resultado_entry.place(x=70, y=290)

def limpiar_entry_integrales(integrales):
    for widget in integrales.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly':
            widget.config(state='normal')  # Cambia a 'normal' para actualizar
            widget.delete(0, tk.END)
            widget.config(state='readonly')

def calcular_integral_definida(integrales, funcion_str, variable_str, limite_inf_str, limite_sup_str):
    # Limpiar resultados anteriores
    resultado_widget = [widget for widget in integrales.winfo_children() if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly']
    if resultado_widget:
        resultado_widget[0].config(state='normal')  # Cambia a 'normal' para actualizar
        resultado_widget[0].delete(0, tk.END)
    
    # Definir símbolo para la variable
    try:
        variable = sp.Symbol(variable_str)
    except Exception as e:
        tk.Label(integrales, text=f'Error en variable: {e}', bg='#0a1937', fg='red').place(x=10, y=330)
        return
    
    # Definir función
    try:
        funcion = sp.sympify(funcion_str)
    except Exception as e:
        tk.Label(integrales, text=f'Error en función: {e}', bg='#0a1937', fg='red').place(x=10, y=330)
        return

    # Definir límites
    try:
        limite_inf = float(limite_inf_str) if limite_inf_str.strip() else None
        limite_sup = float(limite_sup_str) if limite_sup_str.strip() else None
    except ValueError:
        tk.Label(integrales, text='Error en límites: Deben ser números válidos', bg='#0a1937', fg='red').place(x=10, y=330)
        return

    # Calcular integral definida
    try:
        if limite_inf is not None and limite_sup is not None:
            integral_resultado = sp.integrate(funcion, (variable, limite_inf, limite_sup))
            resultados = f"Integral definida de {funcion_str} de {limite_inf} a {limite_sup}: {integral_resultado}"
        else:
            tk.Label(integrales, text='Error: Debe proporcionar ambos límites para integral definida', bg='#0a1937', fg='red').place(x=10, y=330)
            return
    except Exception as e:
        resultados = f"Error: {e}"
    
    # Mostrar resultados
    resultado_widget[0].insert(0, resultados)  # Muestra los resultados
    resultado_widget[0].config(state='readonly')  # Vuelve a 'readonly'

def calcular_integral_indefinida(integrales, funcion_str, variable_str):
    # Limpiar resultados anteriores
    resultado_widget = [widget for widget in integrales.winfo_children() if isinstance(widget, tk.Entry) and widget.cget('state') == 'readonly']
    if resultado_widget:
        resultado_widget[0].config(state='normal')  # Cambia a 'normal' para actualizar
        resultado_widget[0].delete(0, tk.END)
    
    # Definir símbolo para la variable
    try:
        variable = sp.Symbol(variable_str)
    except Exception as e:
        tk.Label(integrales, text=f'Error en variable: {e}', bg='#0a1937', fg='red').place(x=10, y=330)
        return
    
    # Definir función
    try:
        funcion = sp.sympify(funcion_str)
    except Exception as e:
        tk.Label(integrales, text=f'Error en función: {e}', bg='#0a1937', fg='red').place(x=10, y=330)
        return

    # Calcular integral indefinida
    try:
        integral_resultado = sp.integrate(funcion, variable)
        integral_resultado = sp.simplify(integral_resultado)  # Simplificar el resultado
        resultados = f"Integral indefinida de {funcion_str}: {integral_resultado} + C"
    except Exception as e:
        resultados = f"Error: {e}"
    
    # Mostrar resultados
    resultado_widget[0].insert(0, resultados)  # Muestra los resultados
    resultado_widget[0].config(state='readonly')  # Vuelve a 'readonly'

if __name__ == '__main__':
    calculadora = tk.Tk()
    calculadora.geometry('300x200+1000+100')
    calculadora.title('Matheasy')
    calculadora.resizable(False, False)

    try:
        icono = PhotoImage(file='imagen.png')
        calculadora.iconphoto(False, icono)
    except Exception as e:
        print(f"Error al cargar el icono: {e}")

    calculadora.configure(background='#0a1937')

    tk.Label(calculadora, text='Bienvenido', bg='#0a1937', fg='white').place(x=120, y=10)
    tk.Label(calculadora, text='Elije una opción!', bg='#0a1937', fg='white').place(x=105, y=30)

    tk.Button(calculadora, width=8, height=1, text='Ecuaciones', command=abrir_ecuaciones).place(x=10, y=60)
    tk.Button(calculadora, width=8, height=1, text='Límites', command=abrir_limites).place(x=80, y=60)
    tk.Button(calculadora, width=8, height=1, text='Integrales', command=abrir_integrales).place(x=150, y=60)

    calculadora.mainloop()