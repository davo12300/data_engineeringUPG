## LIBRERIAS

import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font


##------ VENTANA INICIAL

## DEFINICION DE VENTANA, geometry define el tamaño de la ventana
## CONFIGURE puede definir algunos visuales / funcionales, background cambia el color fondo 


ventana = Tk()
ventana.title("FINAL PROYECT")
ventana.geometry("500x500")
ventana.configure(background="#0B486B")

tk.Label(ventana, text="SISTEMA DE REGISTROS", background="#0B486B" , font='Terminal',foreground='white'). place(x=130, y=10)

## DECLARACIÓN DE TEXTO , label es solamente un texto en pantalla, ##indica los colores y Arial el tipo de letra, igual para los entry
count = 0


## Funcion login page crea una nueva ventana para poder se llamada en los botones
def login_page():
    ##Destruimos la ventana inicial 
    ventana.destroy()
    ## Creamos y parametrizamos la nueva ventana
    ventana2 = Tk()
    ventana2.title("LOGIN system")
    ventana2.geometry("500x500")
    ventana2.configure(background="#0B486B")

    tk.Label(ventana2, text="SISTEMA DE REGISTROS", background="#0B486B" , font='Terminal',foreground='white'). place(x=130, y=10)

    ## DECLARACIÓN DE TEXTO , label es solamente un texto en pantalla, ##indica los colores y Arial el tipo de letra, igual para los entry

    usuario = tk.Label (ventana2,text="User:  " , background="#0B486B" , font='Arial', foreground="white" ).place(x=237 ,y =60)
    passwor = tk.Label (text="Password:  " , background="#0B486B" , font='Arial', foreground="white").place(x=215 ,y =140)

    #ENTRADA DE DATOS .place define su ubicación en la pantalla

    user = tk.Entry(ventana2,width=20, background="#3B8686", font='Arial' , foreground='white')
    user.place(x=140, y = 110)

    password= tk.Entry(ventana2, width=20, background="#3B8686", font='Arial' , foreground='white')
    password.place(x = 140, y = 190)
    password.config(show="*")

    

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
                connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'mypass10', database='user_tk')
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

                        
                    ventana2.destroy()
                    ##si es correcto nos mandara otra root
                    
                    # Creación de la ventana de Registros
                    
                    root = tk.Tk()
                    root.title("Sistema de registros de MySQL")
                    root.geometry("1000x350")
                    root.configure(background="#0B486B")
                    standard_font = font.Font(family="Arial", size=12)

                    ##Texto de pantalla de registros, Label únicamente texto en pantalla

                    identi = tk.Label (root,text="ID  " , background="#0B486B", foreground='white', font=standard_font).place(x=65 ,y =30)

                    nombre = tk.Label (root,text="NOMBRE:  " , background="#0B486B", foreground='white', font=standard_font).place(x=65 ,y =60)
                    apellido1 = tk.Label (root, text="APELLIDO PATERNO  " , background="#0B486B", foreground='white', font=standard_font).place(x=65 ,y =90)
                    apellido2 = tk.Label (root,text="APELLIDO MATERNO  " , background="#0B486B", foreground='white', font=standard_font).place(x=65 ,y =120)
                    edad1 = tk.Label (root,text="EDAD  " , background="#0B486B", foreground='white', font=standard_font).place(x=65 ,y =150)
                    
                    ## StringVar sirve para cuando tengamos que hacer busqueda poder mandar los resultados a nuestras entradas de texto
                    
                    id_var = tk.StringVar()
                    name_var = tk.StringVar()
                    ape_var = tk.StringVar()
                    apem_var = tk.StringVar()
                    edad_var = tk.StringVar()

                    ##Declaramos todas nuestras entradas de texto y configuramos el fondo , el color del texto, y el lugar donde van

                    ide = tk.Entry(root,width=20, background="#3B8686", font='Arial' , foreground='white', textvariable=id_var)
                    ide.place(x=230, y = 30)
                    ide.config(state='normal')


                    name = tk.Entry(root,width=20, background="#3B8686", font='Arial' , foreground='white',  textvariable=name_var)
                    name.place(x=230, y = 60)

                    ap= tk.Entry(root,width=20, background="#3B8686", font='Arial' , foreground='white',  textvariable=ape_var)
                    ap.place(x = 230, y = 90)

                    am = tk.Entry(root,width=20, background="#3B8686", font='Arial' , foreground='white',  textvariable=apem_var)
                    am.place(x=230, y = 120)

                    age= tk.Entry(root,width=20, background="#3B8686", font='Arial' , foreground='white',  textvariable=edad_var)
                    age.place(x =230, y = 150)


                    ## creamos una función llamada clear_text, nos ayuda a limpiar nuestras entradas de texto 

                    def clear_text():
                        age.delete(0, END)
                        name.delete(0, END)
                        am.delete(0, END)
                        ap.delete(0, END)
                        ide.delete(0, END)
                    

                    ## Función registro, esta función sirve para crear nuevo registro

                    def registro():

                        ##Recogemos la información de las entradas de texto y las guardamos en una variable 
                        user_name = str(name.get())
                        user_ap = str(ap.get())
                        user_amta = str(am.get())
                        user_age = str(age.get())


                        ##Verificamos que no esten vacias , si es así , messagebox te mandará un mensaje en pantalla
                        if user_name== "" or user_ap == "" or user_amta == "" or user_ap == "" or   user_age == "":
                                messagebox.showinfo(message="Rellena los campos", title="Campos vacios")

                        else:

                            ##si esta correcto todo procede a hacer la inserseción 

                            ##Creamos conexión
                            connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'mypass10', database='user_tk')

                            ##definimos cursor, en esta nos ayudará a insertar la información.
                            cur = connect_db.cursor()
                            ## Ejecutamos el cursor donde creamos la query
                            ##concatenamos la query con las variables donde recogimos el sistema
                            cur.execute("INSERT into cliente (nombre,apellido_p,apellido_m,edad)" "values('"+user_name+"','"+user_ap+"','"+user_amta+"','"+user_age+"')" )
                            
                            
                            ##Al finalizar pondrá ejecutado con exito


                            messagebox.showinfo(message="EJECUTADO CON EXITO", title="EXITO")
                            
                            ##Cerramos conexión y el commit
                            connect_db.commit()
                            connect_db.close()

                            ##Mandamos llamar display para que actulize el treeview 
                            display()
                            ##limpiamos las entradas de texto
                            clear_text()

                    ##Funcion Actulizar, actuliza el registro que hayamos buscado, todo es igual que registro solo cambia la query

                    def actualizar():
                        ## se obtienen datos
                        id_c = str(ide.get())
                        user_name = str(name.get())
                        user_ap = str(ap.get())
                        user_amta = str(am.get())
                        user_age = str(age.get())

                        if user_name== "" or user_ap == "" or user_amta == "" or user_ap == "" or user_age == "":
                                messagebox.showinfo(message="Rellena los campos", title="Campos vacios")

                        else:
                            connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'mypass10', database='user_tk')
                            cur = connect_db.cursor()
                            ## Se usa query para UPDATE
                            sql = "UPDATE cliente SET nombre = '"+user_name+"', apellido_p = '"+user_ap+"', apellido_m = '"+user_amta+"', edad = '"+user_age+"' WHERE id_cliente = '"+id_c+"'"
                            


                            cur.execute(sql)
                            
                            
                            messagebox.showinfo(message="EJECUTADO CON EXITO", title="EXITO")
                            
                                    
                            connect_db.commit()
                            connect_db.close()
                            display()
                            clear_text()
                            busqueda()
                        
                        ide.config(state= "normal")
                        ide.delete(0,END)

                    
                    ##Funcion buscar, esta busca el id en la base de datos y lo acomoda en nuestras entradas de texto
                    def buscar():

                        ##Try se usa para atrapar errores de ejecución(Es opcional)
                        try:

                            ##Aquí solo requerimos recoger el ID de la caja de texto
                            user_id = str(ide.get())

                            ##chacamos que no este vacio

                            if user_id == "":
                                messagebox.showinfo(message="Campos Vacios", title="ERROR")
                            else:
                                
                                ##.config nos ayuda a desabilitar la caja de texto disabled para inhabilidar y normal para regresarla a como es
                                ide.config(state= "disable")
                                
                                display()
                                
                                
                                ##Creamos conexión


                                connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'mypass10', database='user_tk')
                                cur = connect_db.cursor()
                                ##Aquí requerimos SELECT para que nos arroje la información que queremos con el ID
                                cur.execute( "SELECT * FROM cliente where id_cliente="+user_id+"")
                                print("Ejecutado con exito")
                                ##guardará el resultado aquí de nuestro cursor en data con función fetchall
                                data = cur.fetchall()
                                #sacamos el conjunto de información devuelta y accesdemos a su primera posición, info_user guarda en un arreglo toda la info del usuario
                                info_user = data[0]

                                
                                
                                ##cerramos conexión y mandamos llamar boton de actualizar
                                connect_db.commit()
                                connect_db.close()
                                actualiza_check()
                                
                                
                        
                            

                        
                        except Exception as error:
                            messagebox.showinfo(message="Verifica tu información ID no existe", title="EXITO")
                            busqueda()
                            ide.config(state= "normal")
                        finally:
                            print('se termino el script')

                        
                        ## la función retornara toda la info del arreglo en cada uno de los entradas te texto, por ello al principio definimos StringVar
                        return  id_var.set(info_user[0]), name_var.set(info_user[1]),ape_var.set(info_user[2]),apem_var.set(info_user[3]), edad_var.set(info_user[4])
                    

                    ##borrar complete solamente requiere el id
                    def borrar_complete():

    
                        try:
                            user_id = str(ide.get())
                        

                            if user_id == "":
                                messagebox.showinfo(message="Campos Vacios", title="ERROR")
                            else:

                                ##conectamos con db

                                connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'mypass10', database='user_tk')
                                cur = connect_db.cursor()
                                ##Ejecutamos query pero solo con Delete
                                cur.execute( "delete from cliente where id_cliente="+user_id+"")
                                print("Ejecutado con exito")
                                
                                ##manda un mensaje de borrado exitoso
                                messagebox.showinfo(message="Eliminado", title="EXITO")
                                
                                
                                connect_db.commit()
                                connect_db.close()
                                display()
                                
                                ide.config(state= "normal")
                                name.config(state="normal")
                                ap.config(state="normal")
                                am.config(state="normal")
                                age.config(state="normal")
                                clear_text()
                                borrar()
                                busqueda()
                                
                                

                        
                        except Exception as error:
                            messagebox.showinfo(message="Verifica tu información ID no existe", title="EXITO")

                        finally:
                            print('se termino el script')


                    ##borrar 2 sirve para poder mandar llamar el boton de borrar complete
                    
                    def borrar2():
                        #limpia el texto que haya en las cajas     
                        clear_text()
                        ##habilita solamente la entrada 1 como normal
                        ide.config(state= "normal")
                        ##las demas la inhabilita
                        name.config(state="disabled")
                        ap.config(state="disabled")
                        am.config(state="disabled")
                        age.config(state="disabled")
                        ide.delete(0, END)
                        ##manda llamar el boton de eliminar complete
                        botton_mas = tk.Button(root,text='ELIMINAR',width=15, command=borrar_complete, font='Arial', background="#FF0000" , foreground="black").place(x=180, y = 250)  
                    ## boton borrar solo dara la opción a eliminar
                    def borrar():   
                        botton_mas = tk.Button(root,text='Opcion Eliminar',width=15, command=borrar2, font='Arial', background="#F9B900" , foreground="black").place(x=180, y = 250)

                    ##busqueda nos manda a la función buscar
                    def busqueda():
                        ide.delete(0,END)
                        botton_update = tk.Button(root,text='Buscar',width=15, command=buscar, font='Arial', background="#F9B900" , foreground="black").place(x=180, y = 300)
                    
                    def actualiza_check():
                        ide.config(state='disabled')
                        botton_update = tk.Button(root,text='ACTUALIZAR',width=15, command=actualizar, font='Arial', background="#7AED00" , foreground="white").place(x=180, y = 300)

                    borrar()
                    busqueda()

                    ##display
                    ##en esta función lo que haremos sera actualizar el treeview
                    def display():
                        ## elimina los que esten mostrados
                        registros = treeview.get_children()
                        for elemento in registros:
                            treeview.delete(elemento)

                        ##ejecuta la query para visualizar
                        connect_db = mysql.connector.connect(host = 'localhost', user='root', passwd= 'mypass10', database='user_tk')
                        cursor = connect_db.cursor()
                        cursor.execute("SELECT * FROM cliente")
                        
                        # añade los datos al Treeview
                        for row in cursor:
                            treeview.insert("", tk.END, text="", values=row)
                        ##cierra conexiones
                        connect_db.commit()
                        connect_db.close()
    
                    # Creación del Treeview
                    treeview = ttk.Treeview(root)

                    # Configuración de las columnas
                    treeview["columns"] = ("ID", "Nombre", "Apellido Paterno", "Apellido Materno","Edad")
                    treeview.column("#0", width=0, stretch=tk.NO)
                    treeview.column("ID", anchor=tk.CENTER, width=50 )
                    treeview.column("Nombre", anchor=tk.W, width=65)
                    treeview.column("Apellido Paterno", anchor=tk.CENTER, width=100)
                    treeview.column("Apellido Materno", anchor=tk.W, width=100)
                    treeview.column("Edad", anchor=tk.W, width=50)


                    # Encabezados de las columnas
                    treeview.heading("#0", text="", anchor=tk.CENTER)
                    treeview.heading("ID", text="ID", anchor=tk.CENTER)
                    treeview.heading("Nombre", text="Nombre", anchor=tk.CENTER)
                    treeview.heading("Apellido Paterno", text="Apellido Paterno", anchor=tk.CENTER)
                    treeview.heading("Apellido Materno", text="Apellido Materno", anchor=tk.CENTER)
                    treeview.heading("Edad", text="Edad", anchor=tk.CENTER)

                    treeview.grid(row=0, column=0, padx=500, pady=20)

                    #mandamos llamar display para poder actualizar la info una vez ingresado el programa
                    display()

                    ##boton aceptar será el unico boton que este fijo y este mismo registrará todo
                    botton_aceptar = tk.Button(root,text='Registrar',width=15, command=registro, font='Arial', background="#F9B900" , foreground="black").place(x=180, y = 200)










                else:

                    global count
                    count  = count + 1
                    
                    messagebox.showinfo(message="Verifica tus datos, intentos : " +str(count)+ "" , title="Erroneo")

                    ## si son 3 los errores nos cerrara el programa y saltará un último mensaje 
                    ## ventana2.destroy cerrara el sistema
                    if count == 3:
                        messagebox.showinfo(message="Demasiados intentos >:c , cerrando programa" , title="Erroneo")

                        ventana2.destroy()



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
    botton_borrar = tk.Button(ventana2,text='Limpiar',width=9, command=clear_text , font='Arial', background="#F9B900" , foreground="black").place(x=125, y = 250)
    botton_aceptar = tk.Button(ventana2,text='Login',width=9, command=login ,font='Arial', background="#F9B900", foreground="black").place(x=270, y = 250)




def get_out():
    ventana.destroy()




botton_borrar = tk.Button(ventana,text='Ingresar',width=9, command=login_page , font='Arial', background="#F9B900" , foreground="black").place(x=125, y = 250)
botton_aceptar = tk.Button(ventana,text='Salir',width=9, command=get_out ,font='Arial', background="#F9B900", foreground="black").place(x=270, y = 250)



ventana.mainloop()