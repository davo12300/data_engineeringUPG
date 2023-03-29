from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox

##DECLARAR VENTANAS

ventana = Tk()
ventana.title("LOGIN system")
ventana.geometry("500x500")
ventana.configure(background="#0B486B")

tk.Label(ventana, text="SISTEMA DE REGISTROS", background="#0B486B" , font='Terminal',foreground='white'). place(x=130, y=10)

## DECLARACIÓN DE TEXTO , label es solamente un texto en pantalla, ##indica los colores y Arial el tipo de letra, igual para los entry

usuario = tk.Label (ventana,text="User:  " , background="#0B486B" , font='Arial', foreground="white" ).place(x=237 ,y =60)
passwor = tk.Label (text="Password:  " , background="#0B486B" , font='Arial', foreground="white").place(x=215 ,y =140)

#ENTRADA DE DATOS .place define su ubicación en la pantalla

user = tk.Entry(ventana,width=20, background="#3B8686", font='Arial' , foreground='white', )
user.place(x=140, y = 110)

password= tk.Entry(ventana, width=20, background="#3B8686", font='Arial' , foreground='white')
password.place(x = 140, y = 190)
password.config(show="*")

##CONTADOR DE INTENTOS

count = 0

#ESTA FUNCIÓN LIMPIA LOS CAMPOS DE TEXTO

def clear_text():
   user.delete(0, END)
   password.delete(0, END)


# FUNCION DEL LOGIN
def login():
    
    #TRY SIRVE PARA EJECUTAR EL CÓDIGO Y SI ENCUENTRA UN ERROR LÓGICO NOS ENVIARÁ UN MENSAJE PANTALLA MAS ABAJO ESTA EXCEPT DONDE SE DEFINE EL MENSAJE (FUNCIONA PARACIDO A UN 'IF')
    try:
        
        ##SACAMOS VALORES DE LOS CAMPOS DE TEXTO CON GET
        user_data = str(user.get())
        pass_data = str(password.get())


        ## VALIDAMOS QUE NO ESTÉN VACIOS , si lo estan mandara un MESSAGEBOX EN pantalla
        if user_data== "" and pass_data == "":
            messagebox.showinfo(message="Rellena los campos", title="Campos vacios")
            

        ## si no , ejecutará el código
        else:  

            ##CREAMOS CONEXIÓN
            connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'davo12300', database='user_tk')
            ## CUR sirve para almacenar operaciónes en la base de datos 
            cur = connect_db.cursor()
            ## CUR. execute permite ejecutar la operación de Base de Datos
            ##Aquí se solicita la contraseña a la BD, usamos where para buscar la contraseña del usuario ingresado
            cur.execute("select password from user where usuario ='"+user_data+"'" )
            
            #data guarda el conjuto de información que arroje la base de datos, aquí almacenará la password 
            data = cur.fetchall()
            
            ##pasamos ese conjunto de información a un arreglo con list , data [0] indica el indice del conjunto
            arreglo = list(data[0])
            ## ahora teniedo el arreglo pasamos el indice del mismo a un dato str para poder compararlo 
            respuesta=str(arreglo[0])

            ##Comparamos pass_data que es el dato que ingreso el usuario en el Entry con el que sacamos de la base de datos

            if pass_data == respuesta:

                ##si es correcto nos mandara otra ventana
                print('login correcto') 
                def openNewWindow():
                    
                    
                    newWindow = Toplevel(ventana)
                    newWindow.configure(background="black")
                    newWindow.title("ACCESS TO SYSTEM")
                    newWindow.geometry("500x500")
                    
                    usuario = tk.Label (newWindow,text="Welcome to the system: Davo" +user_data+"" , background="green" , font="Aial", foreground="white").place(x=65 ,y =60)
                    Label(newWindow,
                        text ="LOGIN SYSTEM").pack()
                    
                openNewWindow()


            ##si no es correcto nos sumara un intento con la variable global y salgara el mensaje
            else:
                global count
                count  = count + 1
                
                messagebox.showinfo(message="Verifica tus datos, intentos : " +str(count)+ "" , title="Erroneo")

                ## si son 3 los errores nos cerrara el programa y saltará un último mensaje 
                ## ventana.destroy cerrara el sistema
                if count == 3:
                    messagebox.showinfo(message="Demasiados intentos >:c , cerrando programa" , title="Erroneo")

                    ventana.destroy()



            ##Cerramos conexión
            connect_db.commit()
            connect_db.close()

    ##Exception captura todos los errores , tambien pudes agregar todos los errores es posible que ocurran, aquí el error saltará si la base de datos no encuentra al usuario
    except Exception as error:
        print(error)
        messagebox.showinfo(message="Usuario no Existe", title="Login Error")
    ##finally siempre se va ejecutar, recomendacion: Buscar los nombres de los errores para poderlos
    ##manejar de mejor manera
    finally:
    
        print('se termino el script')


    


## mandamos llamar los botones y listo
botton_borrar = tk.Button(ventana,text='Limpiar',width=9, command=clear_text , font='Arial', background="#F9B900" , foreground="black").place(x=125, y = 250)
botton_aceptar = tk.Button(ventana,text='Login',width=9, command=login ,font='Arial', background="#F9B900", foreground="black").place(x=270, y = 250)



ventana.mainloop()