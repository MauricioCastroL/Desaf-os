#Autor: Mauricio Castro
#Fecha: 11/09/24

import tkinter as tk
from tkinter import *
from tkinter import ttk

def uno():
    if unoa.get() == '1':
        visior.set(visior.get() + unoa.get())
        
def dos():
    if dosa.get() == '2':
        visior.set(visior.get() + dosa.get())

def tres():
    if tresa.get() == '3':
        visior.set(visior.get() + tresa.get())

def cuatro():
    if cuatroa.get() == '4':
        visior.set(visior.get() + cuatroa.get())
        
def cinco():
    if cincoa.get() == '5':
        visior.set(visior.get() + cincoa.get())

def seis():
    if seisa.get() == '6':
        visior.set(visior.get() + seisa.get())

def siete():
    if sietea.get() == '7':
        visior.set(visior.get() + sietea.get())
        
def ocho():
    if ochoa.get() == '8':
        visior.set(visior.get() + ochoa.get())

def nueve():
    if nuevea.get() == '9':
        visior.set(visior.get() + nuevea.get())

def cero():
    if ceroa.get() == '0':
        visior.set(visior.get() + ceroa.get())
        
def porcentaje():
    if porcentajea.get() == '%':
        visior.set(visior.get() + porcentajea.get())

def punto_decimal():
    if punto_decimala.get() == '.':
        visior.set(visior.get() + punto_decimala.get())

def suma():
    if sumaa.get() == '+':
        visior.set(visior.get() + sumaa.get())
        
def resta():
    if restaa.get() == '-':
        visior.set(visior.get() + restaa.get())

def multiplicacion():
    if multiplicaciona.get() == '*':
        visior.set(visior.get() + multiplicaciona.get())

def division():
    if divisiona.get() == '/':
        visior.set(visior.get() + divisiona.get())

def eliminar():
    if borrara.get() == '⌫':
        visior.set(visior.get() + borrara.get())

def igual():
    if iguala.get() == '=':
        resultado = eval(visior.get())
        visior.set(resultado)

def borrar_C():
    visior.set('')

if __name__ == '__main__':
    #Creacion de la calculadora 
    calculadora = Tk()
    calculadora.title('Calculadora')
    calculadora.geometry('320x400+1000+100')
    calculadora.resizable(False, False)
    icono = PhotoImage(file='icono.png')
    calculadora.iconphoto(False, icono)
    calculadora.configure(background='#504848')

    #Creación de los botones y visor
    unoa = StringVar(value='1')
    uno = Button(calculadora, width=8, height=3, background='#d65200', text='1', command=uno, textvariable=unoa).place(x=20, y=150)
    dosa = StringVar(value='2')
    dos = Button(calculadora, width=8, height=3, background='#d65200', text='2', command=dos).place(x=90, y=150)
    tresa = StringVar(value='3')
    tres = Button(calculadora, width=8, height=3, background='#d65200', text='3', command=tres).place(x=160, y=150)
    multiplicaciona = StringVar(value='*')
    multiplicacion = Button(calculadora, width=8, height=3, background='#d65200', text='X', command=multiplicacion).place(x=230, y=150)
    cuatroa = StringVar(value='4')
    cuatro = Button(calculadora, width=8, height=3, background='#d65200', text='4', command=cuatro).place(x=20, y=210)
    cincoa = StringVar(value='5')
    cinco = Button(calculadora, width=8, height=3, background='#d65200', text='5', command=cinco).place(x=90, y=210)
    seisa = StringVar(value='6')
    seis = Button(calculadora, width=8, height=3, background='#d65200', text='6', command=seis).place(x=160, y=210)
    restaa = StringVar(value='-')
    resta = Button(calculadora, width=8, height=3, background='#d65200', text='-', command=resta).place(x=230, y=210)
    sietea = StringVar(value='7')
    siete = Button(calculadora, width=8, height=3, background='#d65200', text='7', command=siete).place(x=20, y=270)
    ochoa = StringVar(value='8')
    ocho = Button(calculadora, width=8, height=3, background='#d65200', text='8', command=ocho).place(x=90, y=270)
    nuevea = StringVar(value='9')
    nueve = Button(calculadora, width=8, height=3, background='#d65200', text='9', command=nueve).place(x=160, y=270)
    sumaa = StringVar(value='+')
    suma = Button(calculadora, width=8, height=3, background='#d65200', text='+', command=suma).place(x=230, y=270)
    ceroa = StringVar(value='0')
    cero = Button(calculadora, width=8, height=3, background='#d65200', text='0', command=cero).place(x=90, y=330)
    iguala = StringVar(value='=')
    igual = Button(calculadora, width=8, height=3, background='#d65200', text='=', command=igual).place(x=230, y=330)
    punto_decimala = StringVar(value='.')
    punto_decimal = Button(calculadora, width=8, height=3, background='#d65200', text='.', command=punto_decimal).place(x=160, y=330)
    porcentajea = StringVar(value='%')
    porcentaje = Button(calculadora, width=8, height=3, background='#d65200', text='%', command=porcentaje).place(x=20, y=330)
    divisiona = StringVar(value='/')
    division = Button(calculadora, width=8, height=3, background='#d65200', text='/', command=division).place(x=230, y=90)
    eliminara = StringVar(value='C')
    eliminar = Button(calculadora, width=8, height=3, background='#d65200', text='C', command=borrar_C).place(x=160, y=90)
    borrara = StringVar(value='⌫')
    borrar = Button(calculadora, width=8, height=3, background='#d65200', text='⌫', command=eliminar).place(x=90, y=90)

    visior = StringVar()
    visior_resultado = Entry(calculadora, width=45, state='readonly', textvariable=visior).place(x=20, y=50)

    calculadora.mainloop()