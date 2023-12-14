from tkinter import *
import tkinter as tk
import mysql.connector


##DECLARAR VENTANAS

ventana = Tk()
ventana.title("USER REGISTER")
ventana.geometry("280x300")
ventana.configure(background="black")

usuario = tk.Label (ventana,text="USER:  " , background="blue").place(x=65 ,y =60)
passwor = tk.Label (text="PASS:  " , background="blue").place(x=65 ,y =80)

#ENTRADA DE DATOS

user = tk.Entry(ventana,width=10)
user.place(x=135, y = 60)

password= tk.Entry(ventana, width=10)
password.place(x = 135, y = 80)

def registro():
    user_data = str(user.get())
    pass_data = str(password.get())

    connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'davo12300', database='user_tk')
    cur = connect_db.cursor()
    cur.execute("insert into user (usuario,pass)" "values('"+user_data+"','"+pass_data+"')" )
    connect_db.commit()
    print("Ejecutado con exito")
    connect_db.close()

botton_aceptar = tk.Button(ventana,text='Registrar',width=9, command=registro).place(x=145, y = 150)

def clear_text():
   user.delete(0, END)
   password.delete(0, END)
   
botton_borrar = tk.Button(ventana,text='Limpiar',width=9, command=clear_text).place(x=60, y = 150)


ventana.mainloop()