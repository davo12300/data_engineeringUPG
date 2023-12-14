from tkinter import *
import tkinter as tk
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("280x300")
ventana.configure(background="black")

#creación de las etiquetas

num_one = tk.Label (ventana,text="Total :  " , background="red").place(x=65 ,y =80)
num_two = tk.Label (text="Numero 1 :  " , background="red").place(x=65 ,y =100)
num_three = tk.Label (text  ="Numero 2:  " , background="red").place(x=65 ,y =120)

#parseo de datos
Var = tk.StringVar()
Total = tk.Entry(ventana, textvariable=Var,width=6).place(x = 135, y= 80)

num1 = tk.Entry(ventana,width=10)
num1.place(x=135, y = 100)

num2= tk.Entry(ventana, width=10)
num2.place(x = 135, y = 120)

def limpiar():
    num1.delete(0, END)
    num2.delete(0, END)


def suma():
    suma= int(num1.get()) + int(num2.get())
    limpiar()    
    return Var.set(suma)

def resta():
    resta= int(num1.get()) - int(num2.get())
    limpiar()
    return Var.set(resta)

def division():
    
    suma= float(num1.get()) / float(num2.get())
    

    limpiar()
    return Var.set(suma)

def multiplicar():
    

    suma= int(num1.get()) * int(num2.get())
    limpiar()
    return Var.set(suma)


botton_aceptar = tk.Button(ventana,text='Sumar',width=9, command=suma).place(x=180, y = 150)
botton_aceptar = tk.Button(ventana,text='Restar',width=9, command=resta).place(x=100, y = 150)
botton_aceptar = tk.Button(ventana,text='Multiplicar',width=9, command=multiplicar).place(x=100, y = 190)
botton_aceptar = tk.Button(ventana,text='dividir',width=9, command=division).place(x=180, y = 190)




ventana.mainloop()