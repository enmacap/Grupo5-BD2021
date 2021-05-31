#!/usr/bin/env/ python3
#para la interfaz
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk    ###Libreria para usar el opcion multiple
#para la base de datos
import MySQLdb
#para la tarjeta rfid
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def write():
    reader = SimpleMFRC522()

    try:
        text=" hola"
        #text = input('Valor del NFC:')
        print(" Ponga su tarjeta para resgistrar")
        reader.write(text)
        print("Registro con Exito")
    finally:
        GPIO.cleanup()
def read():
    reader = SimpleMFRC522()

    try:
        id, text = reader.read()
    finally:
        GPIO.cleanup()
    print(id)
    return id


DB_HOST = 'localhost'
DB_USER = 'grupo5'
DB_PASS = '12345'
DB_NAME = 'bdfuncionario'

datos = [DB_HOST, DB_USER,  DB_PASS, DB_NAME]
miConexion =MySQLdb.connect(*datos)

root = Tk()
root.title(" Grupo 5")
root.geometry("1000x900")

#declacion de las variables para los campos
miId= IntVar()
miCi= StringVar()
miNombre= StringVar()
miApellido= StringVar()
miCorreo= StringVar()
miDepartamento= StringVar()
miInfectado=StringVar()
miTarjeta =StringVar()
micodigo_rfid= StringVar()
aux1=StringVar()
aux2=StringVar()


def conexionBBDD():
    DB_HOST = 'localhost'
    DB_USER = 'grupo5'
    DB_PASS = '12345'
    DB_NAME = 'bdfuncionario'

    datos = [DB_HOST, DB_USER,  DB_PASS, DB_NAME]
    miConexion =MySQLdb.connect(*datos)
    #miCursor = miConexion.cursor()

def eliminarBBDD():
    miCursor = miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente, Desea continuar?", title= "ADVERTENCIA"):
        miCursor.execute("DROP TABLE Funcionario")
    else:
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()
    
def salirAplicacion():
    valor = messagebox.askquestion("Salir","Esta seguro que desea salir de la Aplicacion?")
    if valor == "yes":
        root.destroy()#sirve para cerrar las ventanas
        pass
    
def limpiarCampos():
    miId.set("")
    miCi.set("")
    miNombre.set("")
    miApellido.set("")
    miCorreo.set("")
    miDepartamento.set("")
    miInfectado.set("")
    miTarjeta.set("")
    micodigo_rfid.set("")
    
    
def mensaje():
    acerca = '''Aplicacion Trabajo Base de Datos \n
                Integrantes:\n
                -\n
                -\n
                -\n
                -\n
                Tutores:
                -\n
                -\n
                -\n
                '''
    messagebox.showinfo(title="INFORMACION", message= acerca)

def crearFuncionario():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    miTarjeta.set(listaT.current()+1)
    miDepartamento.set(listaD.current()+1)
    try:
        sql = '''INSERT INTO funcionario( ci, nombre, apellido, correo, infectado, departamento_id, tarjeta_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s);'''
        miCursor.execute(sql, (miCi.get(), miNombre.get(), miApellido.get(), miCorreo.get(),miInfectado.get(),int(miDepartamento.get()),int(miTarjeta.get())))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()

def crearDepartamento():
    cmiDepartamento = StringVar()
    ventanaD = Toplevel()
    ventanaD.title("Crear Departamento")
    ventanaD.geometry("500x500")
    
    l1= Label(ventanaD,text= "Introduzca departamento")
    l1.place(x=30,y=10)
    e1= Entry(ventanaD, textvariable= cmiDepartamento, width=20)
    e1.place(x=30, y=40)
    
    def crear():
        miConexion= MySQLdb.connect(*datos)
        miCursor = miConexion.cursor()
        try:
            sql = '''INSERT INTO departamento(dpnombre) VALUES (%s)'''
            miCursor.execute(sql, (cmiDepartamento.get()))
            miConexion.commit()
            messagebox.showwarning("Mensaje","Datos guardados Exitosamente")
            ventanaD.destroy()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
            pass
        limpiarCampos()
        miCursor.close()   
    b1= Button(ventanaD, text="Guardar", command=crear)
    b1.place(x=30, y=80)
    
    ventanaD.mainloop()
#     #ventanaD = tk.Tk()
#     var=tk.StringVar(ventanaD)
#     var.set('Administracion')
#     opciones=['Finanzas','Atencion','Cobranzas']
#     opcion=tk.OptionMenu(ventanaD,var,*opciones)
#     opcion.pack(side='left')
    
    

def crearTarjeta():
    cmiTarjeta= StringVar()
    ventanaT = Toplevel()
    ventanaT.title("Crear Tarjeta")
    ventanaT.geometry("500x500")
    
    
    l1= Label(ventanaT, text= "Ponga su tarjeta para registrar")
    l1.place(x=30,y=10)
#     e1= Entry(ventanaT, textvariable= cmiTarjeta, width=20)
#     e1.place(x=30, y=40)
#   b1= Button(ventanaT, text="Guardar")
#   b1.place(x=30, y=80)
############Aca le llamo a la funcion del rfid ########3
    ###################
    #write()
    #miTarjeta.set(read())
#############################################
    
   
#     def sensor():
#         reader = SimpleMFRC522()
#         try:
#             text="Tarjeta"
#             #text = input('Valor del NFC:')
#             print(" Ponga su tarjeta para resgistrar")
#             reader.write(text)
#             messagebox.showwarning("Mensaje","Vuelva a pasar la tarjeta")
#             id, text = reader.read()
#             print("Registro con Exito")
#             cmiTarjeta.set(id)
#         finally:
#             GPIO.cleanup()
#             #messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
#             
#         print(cmiTarjeta.get())
#         return cmiTarjeta
   
   #e1= Entry(ventanaT, textvariable= miTarjeta, width=20)
   
#     b2= Button(ventanaT, text="Registrar", command=sensor)
#     b2.place(x=30, y=40)
    e1= Entry(ventanaT, textvariable= cmiTarjeta, width=20)
    e1.place(x=30, y=80)
    
    def crear():
        miConexion =MySQLdb.connect(*datos)
        miCursor = miConexion.cursor()
        print(miCursor)
        try:
            sql = '''INSERT INTO tarjeta(codigo_rfid)
                VALUES (%s);'''
            miCursor.execute(sql,(cmiTarjeta.get()))
            miConexion.commit()
            messagebox.showwarning("Mensaje","Datos guardados Exitosamente")
            ventanaT.destroy()
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
            pass
        limpiarCampos()
        #mostrar()
        miCursor.close()
        
    b1= Button(ventanaT, text="Guardar", command=crear)
    b1.place(x=30, y=120)
    #Button(self.edit_wind, text = 'Agregar', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
    ventanaT.mainloop()


    
    
    
    

def mostrar():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    #para evitar que se registre los registros a la hora de mostras
    
    registro= tree.get_children()# almacenamos todos los elemntos que se encuentre en nuestra tabla si es que lo hay
    for elemento in registro:
        tree.delete(elemento)
    #extraemos los valores de la base de datos
    try:
        miCursor.execute('''SELECT id_funcionario,ci,nombre, apellido,correo, infectado, dpnombre, codigo_rfid FROM funcionario 
                    INNER JOIN departamento ON funcionario.departamento_id= departamento.id_departamento
                    INNER JOIN tarjeta ON funcionario.tarjeta_id= tarjeta.id_tarjeta''')
        for row in miCursor:
            tree.insert("",0,text=row[0], values= (row[1],row[2],row[3], row[4], row[5], row[6], row[7]))
    except:
        pass
    miCursor.close()
    #### Funcion que trae  los datos departamento de la BD
def mostrarDepartamento():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('SELECT* FROM departamento')
        datos = miCursor.fetchall()
    except:
        pass
    miCursor.close()
    return datos
########### Tabla#########
tree= ttk.Treeview(height=10,columns=('#0','#1','#2','#3', '#4','#5','#6'))
tree.place(x=0,y=350)
tree.column('#0', width=50)
tree.heading('#0', text= "Id", anchor = CENTER)

tree.column('#1', width=100)
tree.heading('#1', text= "CI", anchor = CENTER)

tree.column('#2', width=150)
tree.heading('#2', text= "Nombre", anchor = CENTER)

tree.column('#3', width=150)
tree.heading('#3', text= "Apellido", anchor = CENTER)

tree.column('#4', width=200)
tree.heading('#4', text= "Correo", anchor = CENTER)

tree.column('#5', width=100)
tree.heading('#5', text= "Infectado", anchor = CENTER)

tree.column('#6', width=150)
tree.heading('#6', text= "Departamento", anchor = CENTER)


tree.column('#7', width=100)
tree.heading('#7', text= "Tarjeta", anchor = CENTER)

def seleccionarUsandoClick(event):
    item= tree.identify('item', event.x,event.y)
    miId.set((tree.item(item, "text")))
    #print(miId.get())
    miCi.set(tree.item(item, "values")[0])
    miNombre.set(tree.item(item, "values")[1])
    miApellido.set(tree.item(item, "values")[2])
    miCorreo.set(tree.item(item, "values")[3])
    miInfectado.set(tree.item(item, "values")[4])
    miDepartamento.set(tree.item(item, "values")[5])
    miTarjeta.set(tree.item(item, "values")[6])  
tree.bind("<Double-1>", seleccionarUsandoClick)    

def actualizarFuncionario():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        datos = miCi.get(),miNombre.get(),miApellido.get(), miCorreo.get(),miDepartamento.get(),miTarjeta.get()
        miCursor.execute("UPDATE funcionario SET CI=?, NOMBRE=?, APELLIDO=?, CORREO=?, DEPARTAMENTO=?, TARJETA=? WHERE Id" + miId.get(), (datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al actualizar un registro")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()

def borrarFuncionario():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message= "Realmente desea eliminar el registro?", title= "ADVERTENCIA"):
            miCursor.execute("DELETE FROM funcionario WHERE Id=" + miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al tratar de eliminar el registro")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()
    
########## Colocar widgets en la vista##########

####Crear los menus####
menubar= Menu(root)
menubasedat= Menu(menubar, tearoff=0)
menubasedat.add_command(label= "Conectar Base de datos", command= conexionBBDD)
menubasedat.add_command(label= "Salir", command= salirAplicacion)
menubar.add_cascade(label="Inicio", menu= menubasedat)

ayudamenu= Menu(menubar, tearoff= 0)
ayudamenu.add_command(label= "Resetear Campos", command= limpiarCampos)
ayudamenu.add_command(label= "Acerca", command= mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

#####Creando etiquetas y cajas de texto####
e1= Entry(root, textvariable= miId) #sirve para guardar el valor del id para luego reutilizarlo 

l2= Label(root, text= "CI:")
l2.place(x=30,y=10)
e2= Entry(root, textvariable= miCi, width=20)
e2.place(x=140, y=10)

l3= Label(root, text= "Nombre: ")
l3.place(x=30,y=40)
e3= Entry(root, textvariable= miNombre, width=50 )
e3.place(x=140, y=40)

l4= Label(root, text= "Apellido:")
l4.place(x=30,y=70)
e4= Entry(root, textvariable= miApellido, width=50)
e4.place(x=140, y=70)

l5= Label(root, text= "Correo:")
l5.place(x=30,y=100)
e5= Entry(root, textvariable= miCorreo, width=50)
e5.place(x=140, y=100)

l6= Label(root, text= "Infectado:")
l6.place(x=30,y=130)
e6= Entry(root, textvariable= miInfectado, width=50)
e6.place(x=140, y=130)

l7= Label(root, text= "Departamento:")
l7.place(x=30,y=160)
# e7= Entry(root, textvariable= miDepartamento, width=50)
# e7.place(x=140, y=160)
###=====Para agregar seleccion multiple
miConexion =MySQLdb.connect(*datos)
miCursor = miConexion.cursor()
try:
    miCursor.execute('SELECT* FROM departamento')
    d = miCursor.fetchall()
except:
    pass
miCursor.close()

listaD= ttk.Combobox(root, width=30,state='readonly')
listaD.place(x=140,y=155)
listaD['values']= d

miDepartamento.set(listaD.get())

# var=tk.StringVar(root)
# var.set(d[0])
# opcion=tk.OptionMenu(root,var,*d)
# opcion.pack(side='left',padx=30,pady=30)
# opcion.place(x=140,y=155,width=460)
# miDepartamento.set("")
# miDepartamento.set(var.get()[1])

l8= Label(root, text= "Tarjeta:")
l8.place(x=30,y=190)
# e8= Entry(root, textvariable= miTarjeta, width=50)
# e8.place(x=140, y=190)
###=====Para agregar seleccion multiple
miConexion =MySQLdb.connect(*datos)
miCursor = miConexion.cursor()
try:
    miCursor.execute('SELECT* FROM tarjeta')
    t = miCursor.fetchall()
except:
    pass
miCursor.close()

listaT= ttk.Combobox(root, width=30,state='readonly')
listaT.place(x=140,y=190)
listaT['values']= t
miTarjeta.set(listaT.get())
# varT=tk.StringVar(root)
# varT.set("rojo")
# op=['a','b']
# opcionT=tk.OptionMenu(root,varT,*op)
# opcionT.pack(side='left',padx=30,pady=30)
# opcionT.place(x=140,y=190,width=460)
# miTarjeta.set("")
# miTarjeta.set(varT.get()[1])

######creando botones######
b1= Button(root, text="Crear Registro", command=crearFuncionario)
b1.place(x=700, y=40)
b2= Button(root, text="Modificar Registro", command= actualizarFuncionario)
b2.place(x=700, y=80)
b3= Button(root, text="Mostrar Lista", command= mostrar)
b3.place(x=700, y=120)
b4= Button(root, text="Eliminar Registro", command= borrarFuncionario)
b4.place(x=700, y=160)
b5= Button(root, text="Agregar Tarjeta", command= crearTarjeta)
b5.place(x=700, y=200)
b6= Button(root, text="Agregar Departamento", command= crearDepartamento)
b6.place(x=700, y=240)
#### Boton para editar cambios
def editarFuncionario():
#     message = ''
#     try:
#         tree.item(tree.selection())['values'][0]
#     except IndexError as e:
#         message = 'Por favor selecciona un dato'
#         return
#     miNombre= tree.item(tree.selection())['text']
#     #old_price = self.tree.item(self.tree.selection())['values'][0]
    edit_wind = Toplevel()
    edit_wind.title("Ventana nueva")
    edit_wind.geometry("500x500")
b7= Button(root, text="Editar", command= editarFuncionario)
b7.place(x=700, y=280)

#ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)


root.config(menu=menubar)
# write()
# read()
root.mainloop()